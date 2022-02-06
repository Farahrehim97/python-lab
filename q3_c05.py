import csv
with open("c1.csv","r") as csvfile:
    csvreader=csv.reader(csvfile)
    fields=next(csvreader)
    print('Field names are:')
    print(', '.join(field for field in fields))
    print('data are:')
    for row in csvreader:
        print(','.join(row))
        
