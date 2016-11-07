import os
import datetime
import mysite2.excel
import mysite2.data
from django.http import HttpResponse
from django.shortcuts import render
from mysite2.models import attRecord
# import types


# 这个import是引用django日历时要用django表格
# from .forms import uploadExcelForm

def listPick(request):
    if request.method == 'POST':
        if request.POST['viewChoice'] == '总视图':
            list = mysite2.data.readAll()
            return render(request, 'list0.html', {'list': list})
    return render(request, 'listPick.html')


def list0(request):
    if request.method == 'POST':
        list0Date = request.POST['list0Date']
        if list0Date != '':
            list = mysite2.data.readDate(list0Date)
        else:
            list = mysite2.data.readAll()
    else:
        list = mysite2.data.readAll()
    return render(request, 'list0.html', {'list': list})

    # 这两行是直接读excel不通过数据库
    # list = mysite2.excel.readExcel()
    # m = mysite2.excel.inputExcel()
    # 这一行是使用django日历时要通过django表格传递
    # return render(request, 'list0.html', {'list': list, 'form': list0Form1})


def list1(request):
    list=[]
    if request.method == 'POST':
        if ((request.POST['startTime'] != '') and (request.POST['endTime'] != '') and (
                    request.POST['startTime'] <= request.POST['endTime'])):
            starttime = request.POST['startTime']
            endtime = request.POST['endTime']
            list = mysite2.data.readRange(starttime, endtime)
            head = mysite2.data.readRangeHead(starttime,endtime)
            return HttpResponse(head)
        else:
            return HttpResponse('请输入正确的起止日期')
    return render(request, 'list1.html', {'list': list})


# BUG:没有加数据验证，如excel没有头，数据错乱，已经存在日期的数据等等,所以现在采用的时每次上传删除之前数据，该数据库还不能起到备份作用
def inputExcel(request):
    if request.method == 'POST':
        if request.POST['inputChoice'] == '是':
            excelDate = str(request.POST['excelDate'])
            mysite2.data.deleteAll()
            # 先让它每次都要重新上传所有数据吧,把原来的数据删除
            a = mysite2.excel.inputExcel(excelDate)
            if a == 1:
                return HttpResponse(excelDate + '的数据已经上传')
            else:
                return HttpResponse('数据上传失败')
        else:
            HttpResponse('数据未上传')
            # BUG:点否会直接跳到inputExcel里的else，这里的判断无效
    else:
        return render(request, 'uploadExcel.html')
    return render(request, 'inputExcel.html')


def uploadExcel(request):
    if request.method == 'POST':  # 当提交表单时
        file_obj = request.FILES.get('excelFile', 1)  # 获取文件对象
        # 这里试验过一种try
        # try:
        #     file_obj = request.POST['excelFile']
        # except MultiValueDictKeyError:
        #     file_obj = True
        if file_obj == 1:
            return HttpResponse('您上传的文件不存在')
        else:
            file_name, file_suffix = os.path.splitext(file_obj.name)  # file_obj.name获取文件名，使用os将其分为文件名和后缀
            if file_suffix == '.xls':
                mysite2.excel.uploadExcel(file_obj, str(datetime.date.today()) + file_suffix)  # 下一步开发使用文件系统管理excel上传文件夹
                return render(request, 'inputExcel.html', {'excelDate': str(datetime.date.today())})
            else:
                return HttpResponse('您上传的文件是' + str(file_suffix) + '格式，请上传xls格式的文件！')
    return render(request, 'uploadExcel.html')


def test(request):
    return render(request, 'test.html')
