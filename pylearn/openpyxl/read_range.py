import json
from openpyxl import load_workbook
from openpyxl.utils import coordinate_from_string, column_index_from_string

# For optimised reader: read_only=True
# For result by using the data_only=True
wb = load_workbook(filename = 'C:/temp/nxexcel/Calendars.xlsx', data_only = True)
worksheet = wb['TimeZones']

xy = coordinate_from_string('A4') # returns ('A',4)
print(column_index_from_string(xy[0]))
print(xy[1])

data = [worksheet.cell(row=i,column=2).value for i in range(7,16)]
print(data)

data = worksheet['B7':'C16']
print(type(data))


for r in data:
    print(r[0].value)
    print(r[1].value)