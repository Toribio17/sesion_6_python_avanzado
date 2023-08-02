from file_managment import file_managment 
import os
import re
import time

class secuencial(file_managment):
    
    _app_path = ""
    
    def __init__(self):
        print("My constructor")
        #super().__init__()
        self._app_path = os.environ["GENERAL_PATH"]
        
        
    def get_text_html(self,folder_path):
        #list_files = self.list_folder_files(self._app_path,"input-files/html-examples")
        list_files = self.list_folder_files(self._app_path,folder_path)
        list_files.remove('.DS_Store')
        for file_name in list_files: 
            complete_path = os.path.join(self._app_path,folder_path)
            html_content = self.read_file(complete_path,file_name,"r")
            self.regex_email(file_name,html_content.lower())
            self.regex_phone(file_name,html_content.lower())
            
            
    def regex_email(self,file_name,text):
        regex_rule_email = re.findall(r'[\w.-]+@[\w.-]+', text)
        
        print("File names: ",file_name,regex_rule_email)
        
    def regex_phone(self,file_name,text):
        regex_rule_phone = re.findall(r'\d{10}', text)
        
        print("File names: ",file_name,regex_rule_phone)


if __name__ == "__main__":
    start = time.time()
    
    obj = secuencial()
    obj.get_text_html("input-files/html-examples")
    obj.get_text_html("input-files/html-examples_2")
    obj.get_text_html("input-files/html-examples_3")
    
    end = time.time()
    print(f"Runtime of the program is {end - start}")
    print('Finish!')
    