import csv
with open("c2.csv","r")as csvfile:
    csvreader=csv.DictReader(csvfile)
    print("ID Department Name")
    print("-------------------")
    for row in csvreader:
        print(row['department_id'],row['department_name'])
