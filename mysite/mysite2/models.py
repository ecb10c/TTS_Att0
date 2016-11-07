from django.db import models
import datetime
from django import forms


# 现在无效数据使用的是None判断，最好改成置0，但是时间又不好置0
class attRecord(models.Model):
    attDate = models.DateField('日期', null=True)
    attID = models.IntegerField('考勤号', default=0)
    attName = models.CharField('姓名', max_length=10, default='未知')
    attRange = models.CharField('时段', max_length=10, default='上午')
    attStart = models.TimeField('上班时间', null=True)
    attEnd = models.TimeField('下班时间', null=True)
    attCome = models.TimeField('签到时间', null=True)
    attGo = models.TimeField('签退时间', null=True)
    attLate = models.TimeField('迟到时间', null=True)
    attEarly = models.TimeField('早退时间', null=True)
    attAbsence = models.BooleanField('是否旷工', default=True)
    attLeave = models.CharField('请假状态', max_length=10, default='无')  # 请假状态（无，间出，公出，事假，病假）
    attSpecial = models.CharField('特殊情况', max_length=10, default='无')  # 特殊情况（无，迟到，早退，旷工，间出，公出，事假，病假）

    def __str__(self):
        # 还没搞清楚这个东西的用法
        # strReturn = str(self.attDate) + ' ' + str(self.attRange) + ' ' + str(self.attID) + ' ' + str(self.attName)
        return self.attName
