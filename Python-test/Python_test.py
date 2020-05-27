import xlrd
import csv
import pyodbc
import pandas as ps

#db connect
conn = pyodbc.connect('DRIVER={SQL Server}; SERVER=10.10.3.26; DATABASE=chrisTest; UID=sa; PWD=yfyoljk@')
cursor = conn.cursor()

query = "select * from [chrisTest].[dbo].[chrisTable4]"
cursor.execute(query)

data = cursor.fetchall()

with open('Qoo.csv', 'w', newline='') as fp:
    a= csv.writer(fp, delimiter=',')
    for line in data:
        a.writerow(line)
        
for row in data:
    print (row[0],row[1],row[2])
cursor.close()
conn.close()   