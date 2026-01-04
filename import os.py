import os
import shutil
import re
import requests
from bs4 import BeautifulSoup

def moving_files(src,dst):
    moved = 0 
    os.makedirs(dst,exist_ok= True)
    for i in os.listdir(src):
        if i.lower().endswith(".jpg"):
            shutil.move(os.path.join(src,i),os.path.join(dst,i))
            moved += 1
    print(f'Total {moved} jpg Files moved ')

def extract_mails(input,output = "email.txt"):
    with open(input,'r',encoding= 'utf-8') as f:
        f1 = f.read()
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = sorted(set(re.findall(pattern,f1)))
    with open(output,'w',encoding= 'utf-8') as f:
        f.write('/n'.join(emails))
    print(f'No.of mails {emails}')

def scrape_title(url,data_file = "datas.txt"):
    try:
        req = requests.get(url,timeout=10)
        req.raise_for_status()
        parse = BeautifulSoup(req.text,'html.parser')
        title_elem = parse.find('title')
        title = title_elem.string.strip() if title_elem and title_elem.string else "No title"
        
        with open(data_file, 'w', encoding='utf-8') as f: 
            f.write(title)
        print(f' Saved: "{title}"')
    except Exception as e:
        print(f' Error: {e}')

if __name__== "__main__":
    print(f"1.To move files{'\n'}2.extract Mails{'\n'}3.Parse Webpage Title{'\n'}")
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        src = r"C:\Users\THARUNESH\OneDrive\Desktop\codealpha\Diiff modules\dst"
        dst = r"C:\Users\THARUNESH\OneDrive\Desktop\codealpha\Diiff modules\src"
        moving_files(src,dst)
    elif choice == 2:
        extract_mails("untitled.txt")
    elif choice == 3:
        scrape_title("https://www.dummies.com")
    else:
        print("invalid")