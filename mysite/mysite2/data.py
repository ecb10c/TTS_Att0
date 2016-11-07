from mysite2.models import attRecord
import datetime


def deleteAll():
    attRecord.objects.all().delete()


def readAll():
    list = attRecord.objects.all()
    return list


def readDate(date):
    list = attRecord.objects.filter(attDate=date)
    return list


def readRange(starttime, endtime):
    # 按时间段查询
    list_query = attRecord.objects.filter(attDate__range=(starttime, endtime))
    # 按姓名分组
    list_query.group_by = ['attName']
    list = readRangeHead(starttime, endtime)
    # for index,i in list_query:
    # 有空学习一下query的用法
    return list


def readRangeHead(starttime, endtime):
    list = []
    # 这里有字符串日期转化和一个日期循环
    begin = datetime.datetime.strptime(starttime, '%Y-%m-%d')
    end = datetime.datetime.strptime(endtime, '%Y-%m-%d')
    for i in range((end - begin).days + 1):
        day = begin + datetime.timedelta(days=i)
        day_str1 = day.strftime('%m-%d') + '上'
        day_str2 = day.strftime('%m-%d') + '下'
        list.append(day_str1)
        list.append(day_str2)
    return list
