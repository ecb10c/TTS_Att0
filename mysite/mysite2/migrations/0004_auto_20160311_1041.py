# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-11 02:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite2', '0003_auto_20160311_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attrecord',
            name='attAbsence',
            field=models.BooleanField(verbose_name='是否旷工'),
        ),
        migrations.AlterField(
            model_name='attrecord',
            name='attCome',
            field=models.TimeField(null=True, verbose_name='签到时间'),
        ),
        migrations.AlterField(
            model_name='attrecord',
            name='attEarly',
            field=models.TimeField(null=True, verbose_name='早退时间'),
        ),
        migrations.AlterField(
            model_name='attrecord',
            name='attEnd',
            field=models.TimeField(null=True, verbose_name='下班时间'),
        ),
        migrations.AlterField(
            model_name='attrecord',
            name='attGo',
            field=models.TimeField(null=True, verbose_name='签退时间'),
        ),
        migrations.AlterField(
            model_name='attrecord',
            name='attID',
            field=models.IntegerField(verbose_name='考勤号'),
        ),
        migrations.AlterField(
            model_name='attrecord',
            name='attLate',
            field=models.TimeField(null=True, verbose_name='迟到时间'),
        ),
        migrations.AlterField(
            model_name='attrecord',
            name='attLeave',
            field=models.CharField(max_length=10, verbose_name='请假状态'),
        ),
        migrations.AlterField(
            model_name='attrecord',
            name='attName',
            field=models.CharField(max_length=10, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='attrecord',
            name='attRange',
            field=models.CharField(max_length=10, verbose_name='时段'),
        ),
        migrations.AlterField(
            model_name='attrecord',
            name='attSpecial',
            field=models.CharField(max_length=10, verbose_name='特殊情况'),
        ),
        migrations.AlterField(
            model_name='attrecord',
            name='attStart',
            field=models.TimeField(null=True, verbose_name='上班时间'),
        ),
    ]