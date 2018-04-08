#!/usr/bin/env python
#_*_coding:utf-8_*_
import xlrd
import sys
excel=sys.argv[1]
data = xlrd.open_workbook(excel)
# table.row_values()
# table.col_values()
# table = data.sheet_by_name(u'Page 1')
# table = data.sheets()[0]
table = data.sheet_by_index(0)
# table = data.sheet_by_name(u'Page 1')
nrows = table.nrows
ncols = table.ncols
text = open('test.txt','w+')
for i in range(nrows):
    if i == 0:
        continue
    for c in range(ncols):
    # print table.row_values(i)
        cell = table.cell(i,c).value
        if c < 6:
            cell = cell+","
        else:
            cell = cell +"\n"
        # print cell
        text.write(cell)
    # type(table.row_values(i))
    # text.write(table.row_values(i))
text.close()
print("Conversion is complete, please see the test.txt")
# table.col_values(i)
