import pandas as pd
import os
import fnmatch
import requests
import wget
from bs4 import BeautifulSoup
from pathlib import Path
from sqlalchemy import create_engine
# import psycopg2 
#import io


current_directory = os.getcwd()
print(current_directory)
files_and_dirs = os.listdir()

print("Files and directories in the current directory:")
print("Excel files in '", current_directory, "':")
for file in excel_files:
    print(file)





# class Anvisa:

#     url = "https://www.gov.br/anvisa/pt-br/assuntos/medicamentos/cmed/precos"
#     def __init__(self, conformity_site_file):
#         self.conformity_site_file = conformity_site_file

#     def file_exists(self):




# url = "https://www.gov.br/anvisa/pt-br/assuntos/medicamentos/cmed/precos"

# r = requests.get(url, allow_redirects=True)
# soup = BeautifulSoup(r.content, "html.parser")
# links_with_text = []
# for a in soup.find_all('a', href=True): 
#     if a.text: 
#         links_with_text.append(a['href'])
        
#        #xls_conformidade_site_ 
        

# k = [k for k in links_with_text if 'xls_conformidade_site' in k] 
# file_url = k[0]

# file_url = file_url.replace("/@@download/file", "")
# file_name = file_url.split('/')[-1]

# file_exists = Path(file_name)
# if file_exists.is_file():
#     #quit()
#     print("OK")
    
    
# print(file_name)
# filename = wget.download(file_url, file_name)

# df  = pd.read_excel(filename, header=None)
# df = df.iloc[41:,:]
