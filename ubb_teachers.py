import requests
from bs4 import BeautifulSoup

URL = "http://www.cs.ubbcluj.ro/despre-facultate/structura/departamentul-de-informatica/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

teachers_table = soup.find(id='post-553')
#print(teachers_table)

teacher_rows = teachers_table.find_all(style='margin-bottom: 15px; margin-right: 15px; width: 630px')
STYLE = 'vertical-align: middle; text-align: left; display: table-cell; padding-left: 12px; padding-right: 12px; width: 503px; border-top: 1px solid #dddddd; border-bottom: 1px solid #dddddd; border-right: 1px solid #dddddd; border-left: 1px solid #dddddd'

teachers = []

for teacher in teacher_rows:
    teacher_info = teacher.find(style=STYLE).text.strip().split("\n")
    #for info in teacher_info:
       # print(info)


    try:
        nume = teacher_info[0].split(", ")[0]
        email = teacher_info[1].split(": ")[1]
        web = teacher_info[2].split(": ")[1]
        adresa = teacher_info[3].split(": ")[0]
        domenii_de_interes = teacher_info[4].split(": ")[1]
    except IndexError as error:
        pass

    teachers.append(
        {
            "nume": nume,
            "email": email,
            "web": web,
            "adresa": adresa,
            "domenii de interes": domenii_de_interes
        }
    )
    #print(teacher_info)

for teacher in teachers:
    print(teacher["nume"])
