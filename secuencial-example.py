from file_managment import file_managment 
import os
import re
import time

class secuencial(file_managment):
    
    _app_path = ""
    
    def __init__(self):
        print("My constructor")
        super().__init__()
        self._app_path = os.environ["GENERAL_PATH"]
        
        
    def get_text_html(self,folder_path):
        #list_files = self.list_folder_files(self._app_path,"input-files/html-examples")
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
    
        return result
            
            
    def regex_email(self,text):
        regex_rule_email = re.findall(r'[\w.-]+@[\w.-]+[.com|.mx]', text)
        
        #print("File names: ",file_name,regex_rule_email)
        
        return regex_rule_email
        
    def regex_phone(self,text):
        regex_rule_phone = re.findall(r'\d{10}', text)
        
        #print("File names: ",file_name,regex_rule_phone)
        
        return regex_rule_phone
        
    def save_document(self,result,val):
        file_path = os.path.join(os.environ['GENERAL_PATH'],"output-files")
        self.write_json_file(file_path,'output-regex-eamil_secuencial_'+str(val)+'.json','w',result)


if __name__ == "__main__":
    start = time.time()
    
    obj = secuencial()
    result = obj.get_text_html(os.environ['INPUT_PATH_1'])
    obj.save_document(result,1)
    result =obj.get_text_html(os.environ['INPUT_PATH_2'])
    obj.save_document(result,2)
    result =obj.get_text_html(os.environ['INPUT_PATH_3'])
    obj.save_document(result,3)
    
    end = time.time()
    print(f"Runtime of the program is {end - start}")
    print('Finish!')
    