from file_managment import file_managment 
import os
import re
import time
from multiprocessing import Process, Queue
from multiprocessing import Value
import multiprocessing
import pytesseract
from pdf2image.exceptions import (
 PDFPageCountError
)
from PIL import Image
from pdf2image import convert_from_path

class multiprocessing_(file_managment):
    
    _app_path = ""
    
    def __init__(self):
        print("My constructor")
        #call parent's constructor
        super().__init__()
        print("Number of cpu : ", multiprocessing.cpu_count())
        self._app_path = os.environ["GENERAL_PATH"]
        
    
    def teseeractOCR(self,count,path_test_train):
        try:
            entries = self.readFiles(count,path_test_train)
            fileTemp = ""
            for entry in entries[0]:
                if "pdf" in entry.lower():
                    print("Files procesing: ", entry)
                    isExist = self.filesExist(entry + ".txt", count,path_test_train)
                    if isExist == False:
                        pages = convert_from_path(entries[1] + "/" + entry, dpi=700, last_page=100, thread_count=5)
                        text = []
                        path_2 = os.environ["GENERAL_PATH"] + "/output-files/"
                        for pageNum, imgBlob in enumerate(pages):
                             text.append(pytesseract.image_to_string(imgBlob, lang='eng'))
                        with open(f'{path_2}{entry}.txt', 'w') as the_file:
                            the_file.write('-'.join(text))
                        print("Files Processed: ", entry, " count: ", count)
                    else:
                        print("already exists: ", entry)
                else:
                    print("other image")
                    
            print("Complete")
        except PDFPageCountError as ex:
            print("Method failed with status code :" + str(ex))
            #self.createEmtyFile(path, fileTemp)
            self.teseeractOCR(folderNum)


if __name__ == "__main__":
    start = time.time()
    obj = multiprocessing_()
    procs = []
    
    path_input_1 = os.path.join(os.environ['INPUT_PATH_1'],"input-files/OCR-inputs")
    path_input_2 = os.path.join(os.environ['INPUT_PATH_1'],"input-files/OCR-inputs")
    list_folder = [path_input_1,path_input_2]
    # instantiating process with arguments
    i = 1
    for folder_name in list_folder:
        proc = Process(target=obj.teseeractOCR, args=(i,folder_name,))
        proc.start()
        procs.append(proc)
        i = i + 1
    
    for p in procs:
        p.join()
    
    end = time.time()
    print(f"Runtime of the program is {end - start}")
    print('Finish!')