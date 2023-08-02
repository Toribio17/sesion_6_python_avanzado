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
        #print("Number of cpu : ", multiprocessing.cpu_count())
        self._app_path = os.environ["GENERAL_PATH"]
        
        
        
    def get_text_html(self,queue,folder_path):
        list_files = self.list_folder_files(self._app_path,folder_path)
        list_files.remove('.DS_Store')
        temp_emails = []
        temp_phones = []
        for file_name in list_files: 
            complete_path = os.path.join(self._app_path,folder_path)
            html_content = self.read_file(complete_path,file_name,"r")
            v1 = self.regex_email(html_content.lower())
            v2 = self.regex_phone(html_content.lower())
            temp_emails.append(v1)
            temp_phones.append(v2)
        result = dict({"Emails":temp_emails,"Phones":temp_phones})
        queue.put(result)
            
            
    def regex_email(self,text):
        regex_rule_email = re.findall(r'[\w.-]+@[\w.-]+[.com|.mx]', text)
        
        #print("Email : ",file_name,regex_rule_email)
        return regex_rule_email
        
    def regex_phone(self,text):
        regex_rule_phone = re.findall(r'\d{10}', text)
        
        #print("Phone : ",file_name,regex_rule_phone)
        return regex_rule_phone


if __name__ == "__main__":
    start = time.time()
    obj = multiprocessing_()
    procs = []
    
    list_folder = [os.environ['INPUT_PATH_1'],os.environ['INPUT_PATH_2'],os.environ['INPUT_PATH_3']]
    # instantiating process with arguments
    q = Queue()
    for folder_name in list_folder:
        proc = Process(target=obj.get_text_html, args=(q,folder_name,))
        proc.start()
        procs.append(proc)
        #result = q.get()
        
    for p in procs:
        p.join()
        
    #file_path = os.path.join(os.environ['GENERAL_PATH'],"output-files")
    #obj.write_json_file(file_path,'output-regex-eamil.json','w',result)
    
    end = time.time()
    print(f"Runtime of the program is {end - start}")
    print('Finish!')
    