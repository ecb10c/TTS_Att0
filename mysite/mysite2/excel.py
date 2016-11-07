from mysite2.models import attRecord
import os
import xlrd
import time
# from django.shortcuts import render
# from django.shortcuts import HttpResponse
import datetime


# import random

def readExcel(excelDate):
    excelPath = os.path.join(os.path.dirname(__file__), 'excel/').replace('\\', '/')  # 相对路径寻取方法
    xlsfile = excelPath + excelDate + r'.xls'
    book = xlrd.open_workbook(xlsfile)
    # sheet_name=book.sheet_names()[0]            #获得指定索引的sheet名字
    # sheet0 = book.sheet_by_name(sheet_name)     #通过sheet名获取sheet
    # row_data = sheet0.row_values(0)             #获得第1行的数据列表
    # col_data = sheet0.col_values(0)             #获得第1列的数据列表
    # cell_value = sheet0.cell_value(0, 0)        #获得某单元格数据
    sheet0 = book.sheet_by_index(0)
    colnames = sheet0.row_values(0)
    nrows = sheet0.nrows
    # ncols = sheet0.ncols
    list = []
    for rownum in range(0, nrows):
        row = sheet0.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[i] = row[i]
            list.append(app)
    return list


def inputExcel(excelDate):
    excel = readExcel(excelDate)
    # 选择要用的列并建立对应关系
    columnPicks = {5, 1, 3, 6, 7, 8, 9, 10, 13, 14, 15}
    columnNames = {'日期': 5, '考勤号': 1, '姓名': 3, '时段': 6, '上班时间': 7, '下班时间': 8, '签到时间': 9, '签退时间': 10, '迟到时间': 13,
                   '早退时间': 14, '是否旷工': 15}
    for listNum in range(1, len(excel)):
        # 下面的循环是将数据转化为符合存储条件的格式，包括空dateTime字符串替换为null，空attAbsence替换为False
        for columnPick in columnPicks:
            if excel[listNum][columnPick] == '':
                excel[listNum][columnPick] = None
        if excel[listNum][columnNames['是否旷工']] == None:
            excel[listNum][columnNames['是否旷工']] = False
        # 下面开始写入
        recordTemp = attRecord()
        # recordTemp.attDate = time.strptime(excel[listNum][columnNames['日期']],"%Y - %m - %d")
        recordTemp.attDate = excel[listNum][columnNames['日期']]
        recordTemp.attID = excel[listNum][columnNames['考勤号']]
        recordTemp.attName = excel[listNum][columnNames['姓名']]
        recordTemp.attRange = excel[listNum][columnNames['时段']]
        recordTemp.attStart = excel[listNum][columnNames['上班时间']]
        recordTemp.attEnd = excel[listNum][columnNames['下班时间']]
        recordTemp.attCome = excel[listNum][columnNames['签到时间']]
        recordTemp.attGo = excel[listNum][columnNames['签退时间']]
        recordTemp.attLate = excel[listNum][columnNames['迟到时间']]
        recordTemp.attEarly = excel[listNum][columnNames['早退时间']]
        recordTemp.attAbsence = excel[listNum][columnNames['是否旷工']]
        recordTemp.attSpecial = judgeSpecial(recordTemp)
        recordTemp.save()
    return 1

# 迟到早退未签到未签退旷工只记录一种
def judgeSpecial(recordTemp):
    a = '无'
    if (recordTemp.attLate != None) and (recordTemp.attLate != ''):
        a = '迟到'
    if (recordTemp.attEarly != None) and (recordTemp.attEarly !=''):
        a = '早退'
    if (recordTemp.attCome==None) or (recordTemp.attCome==''):
        a = '未签到'
    if (recordTemp.attGo==None) or (recordTemp.attGo==''):
        a = '未签退'
    if (a=='未签退') and ((recordTemp.attCome==None) or (recordTemp.attCome=='')):
        a = '旷工'
    return a


def uploadExcel(file_obj, file_name):
    # 写入文件
    if not os.path.exists('mysite2/excel/'):
        os.mkdir('mysite2/excel/')
    with open('mysite2/excel/' + file_name, 'wb+') as destination:  # 使用withas句型可以自动处理文件异常和自动关闭
        for chunk in file_obj.chunks():  # 使用chunks而不使用read可以节省内存
            destination.write(chunk)
