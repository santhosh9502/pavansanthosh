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

best_student_mathematics = ''
highest_marks_mathematics = 0

with open('Assignments/student_marks.csv','r') as file:
    data = csv.DictReader(file)
    for record in data:
        if int(record['Maths']) >= 90:
            Maths += 1
            if int(record['Maths']) > highest_marks_mathematics:
                highest_marks_mathematics = int(record['Maths'])
                best_student_mathematics = record['studentname']
        if int(record['Telugu']) >= 90:
            Telugu += 1
        if int(record['English']) >= 90:
            English += 1
        if int(record["Physics"]) >= 90:
            Physics += 1
        if int(record["Chemistry"]) >= 90:
            Chemistry += 1
        if int(record["Social"]) >= 90:
            Social += 1
        
    sub_faculty = {
        'Telugu': Telugu,
        'English': English,
        'Maths': Maths,
        'Physics': Physics,
        'Chemistry': Chemistry,
        'Social': Social
    }

print(f"Best Student in Mathematics is {best_student_mathematics} wih marks as {highest_marks_mathematics}.")