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

country_c = {}
for x in csv_data:
    if x[5] not in country_c:
        country_c[x[5]]= 1
    else:
        country_c[x[5]]+= 1
co = max(country_c, key = lambda x:country_c[x])
print()
print(country_c)
print("highest population:",co,country_c[co])