import csv

Telugu = 0
English = 0
Maths = 0
Physics = 0
Chemistry = 0
Social = 0

faculty = {
    'Telugu' : 'Amarnath',
    'English' : 'Samuel',
    'Maths' : 'Murali Krishna',
    'Physics' : 'Raja Gopal',
    'Chemistry' : 'Ravi',
    'Social' : 'Krishna Reddy'
}


sub_faculty = {}

with open('Assignments/student_marks.csv','r') as file:
    data = csv.DictReader(file)
    for record in data:
        if int(record['Telugu']) >= 90:
            Telugu+=1
        if int(record['English']) >= 90:
            English+=1
        if int(record["Maths"]) >= 90:
            Maths+=1
        if int(record["Physics"]) >= 90:
            Physics+=1
        if int(record["Chemistry"]) >= 90:
            Chemistry+=1
        if int(record["Social"]) >= 90:
            Social+=1
        
    sub_faculty['Telugu'] = Telugu
    sub_faculty["English"] = English
    sub_faculty['Maths'] = Maths
    sub_faculty['Physics'] = Physics
    sub_faculty["Chemistry"] = Chemistry
    sub_faculty["Social"] = Social


m = max(sub_faculty, key= sub_faculty.setdefault)
print(f"The faculty with the most high scores is {faculty[m]} with {sub_faculty[m]} students who scored more than 90%.")