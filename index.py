import subprocess
import os

def create_file(res,name):
    location=str(os.path.abspath(__file__)).replace("index.py",'')
    path=location+name.split(" ")[0].replace("-"," ")+"/"
    os.makedirs(path, exist_ok = True)
    with open(path+"Elite "+name+".txt",'w') as fw:
            fw.writelines(res.json()['response']['files'][0]['contents'])
            try:
                fw.writelines(res.json()['response']['files'][1]['contents'])
            except:
                print("No answer found for ",name)
import requests as re
import getpass
from bs4 import BeautifulSoup as soup
se=re.session()
data={"username":str(input("Enter your username : ")),"password":str(getpass.getpass(prompt="Enter your password : "))}
se.post("http://ngitonline.com/login/index.php",data=data)
print("logging in",se)

location=os.path.abspath(__file__)
path = os.path.join(location)
res=se.get("http://ngitonline.com/student/dashboard.php")
res=soup(res.text,'html.parser')
for name,link in zip(res.find_all("h2",class_="course-date"),res.find_all("a",class_="btn btn-primary btn-lg pull-right")):
    if("Day" in name.text):
        print(name.text,link["href"],sep="\t")
        lnk=str(link["href"]).replace(".php",".json.php")
        res=se.post(lnk+"&action=load")
        create_file(res,name.text)