from django import forms
from django.contrib.admin import widgets

class uploadExcelForm(forms.Form):
    excelDate = forms.DateTimeField(widget=widgets.AdminDateWidget(), label=u'数据时间')#为了调用django日历的，widget属性可以标注表单样式class

class list0Form(forms.Form):
    list0Date = forms.DateTimeField(widget=widgets.AdminDateWidget(), label=u'查询时间')