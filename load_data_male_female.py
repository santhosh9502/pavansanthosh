import csv

with open('data.csv', newline='\n') as csvfile:
    # datareader = csv.reader(csvfile, delimiter=';', quotechar='|')
    # data extracted to data reader and retruns a reader object
    
    datareader = csv.reader(csvfile, delimiter=',')
    
    data_iter = iter(datareader)
    col_names = next(data_iter)

    csv_data = []

    for row in data_iter:
        csv_data.append(row)

print(col_names)
print(csv_data)

m = 0
f = 0
for x in csv_data:
    if x[4]== 'Male':
        m+=1
    if x[4]== 'Female':
        f+= 1
print("no of Male",m)
print("no of Female",f)
print("ratio to Male and Female",m/f)