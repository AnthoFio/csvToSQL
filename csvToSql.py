import csv
import sys

with open('MOCK_DATA.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    sqlFile = open(r"sqlQuery.sql","w+") 
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            sql_etablissement = f'Insert into ETABLISSEMENT ({row[0]},{row[1]})'
            sql_adresse = f'Insert into ADRESSE ({row[2]},{row[3]})'
            line_count += 1
        else:
            str1 = f'{sql_etablissement} VALUES (SEQ.NEXTVAL,{row[0]}, {row[1]});'
            str2 = f'{sql_adresse} VALUES (SEQ.NEXTVAL,{row[2]}, {row[3]});'
            print(str1)
            print(str2)
            L = ['\n',str1, str2,'\n']
            sqlFile.writelines(L)
            
            line_count += 1
    print(f'Processed {line_count} lines.')
    sqlFile.write('\nCOMMIT;')
    sqlFile.close