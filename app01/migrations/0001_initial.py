# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-07 08:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='答案')),
                ('score', models.IntegerField()),
                ('content', models.CharField(max_length=255, verbose_name='回答内容')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='班级名称')),
                ('stu_num', models.IntegerField(verbose_name='班级人数')),
            ],
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('captions', models.CharField(max_length=64, verbose_name='问题的内容')),
                ('score', models.IntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='问题名称')),
                ('question_choice', models.IntegerField(choices=[('1', '打分'), ('2', '单选'), ('3', '建议')], verbose_name='选择问题形式')),
            ],
        ),
        migrations.CreateModel(
            name='Questionanire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='问卷名称')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Group', verbose_name='所属班级')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='学生姓名')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Group', verbose_name='所属班级')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='用户姓名')),
                ('password', models.CharField(max_length=32, verbose_name='用户密码')),
            ],
        ),
        migrations.AddField(
            model_name='questionanire',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.UserInfo', verbose_name='所属用户'),
        ),
        migrations.AddField(
            model_name='question',
            name='qs_anire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Questionanire', verbose_name='所属问卷'),
        ),
        migrations.AddField(
            model_name='options',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Question', verbose_name='所属问题'),
        ),
        migrations.AddField(
            model_name='answer',
            name='Stu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Student'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Question', verbose_name='所属问题'),
        ),
    ]
