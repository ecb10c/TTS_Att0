import xlrd

#打开指定文件路径的excel文件
xlsfile = r'D:\test.xls'
book = xlrd.open_workbook(xlsfile)          #获得excel的book对象

#通过sheet名或索引值获取sheet对象
sheet_name=book.sheet_names()[0]            #获得指定索引的sheet名字
sheet0 = book.sheet_by_name(sheet_name)     #通过sheet名获取sheet
sheet1 = book.sheet_by_index(0)             #也可通过sheet索引获取sheet

nrows = sheet0.nrows                        #行总数
ncols = sheet0.ncols                        #列总数

row_data = sheet0.row_values(0)             #获得第1行的数据列表
col_data = sheet0.col_values(0)             #获得第一列的数据列表，然后就可以迭代里面的数据了

#通过cell的位置坐标获得指定cell的值
cell_value = sheet0.cell_value(0,0)
#cell_value1 = sheet0.cell_value(0,0)         #只有cell的值内容，如：http://xxx.xxx.xxx.xxx:8850/2/photos/square/
#cell_value2 = sheet0.cell(0,0)               #除了cell值内容外还有附加属性，如：text:u'http://xxx.xxx.xxx.xxx:8850/2/photos/square/'

print(cell_value)                             #输出测试