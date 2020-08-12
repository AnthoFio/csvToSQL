import csv
import sys

with open('MOCK_DATA.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            sql_etablissement = f'Insert into ETABLISSEMENT ({row[0]},{row[1]})'
            sql_adresse = f'Insert into ADRESSE ({row[2]},{row[3]})'
            line_count += 1
        else:
            print(f'{sql_etablissement} VALUES (SEQ.NEXTVAL,{row[0]}, {row[1]})')
            print(f'{sql_adresse} VALUES (SEQ.NEXTVAL,{row[2]}, {row[3]})')
            line_count += 1
    print(f'Processed {line_count} lines.')