from django.db import models

# Create your models here.


#用户列表
class UserInfo(models.Model):
    '''
    用户表
    '''
    name=models.CharField(max_length=32,verbose_name='用户姓名')
    password=models.CharField(max_length=32,verbose_name='用户密码')


#班级表
class Group(models.Model):
    '''
    班级表
    '''
    title=models.CharField(max_length=32,verbose_name='班级名称')
    stu_num=models.IntegerField(verbose_name='班级人数')

#问卷表:关联用户
class Questionanire(models.Model):
    '''
    问卷表,对哪个班级的问卷
    '''
    title=models.CharField(verbose_name='问卷名称',max_length=64)
    group=models.ForeignKey(verbose_name='所属班级',to=Group)
    user=models.ForeignKey(verbose_name='所属用户',to=UserInfo)

#问题:
class Question(models.Model):
    '''
    问题表
    '''
    title=models.CharField(max_length=255,verbose_name='问题名称')
    question_content = (
        ('1', '打分'),
        ('2', '单选'),
        ('3', '建议'),
    )
    question_choice = models.IntegerField(choices=question_content, verbose_name='选择问题形式')
    qs_anire=models.ForeignKey(verbose_name='所属问卷',to=Questionanire)

    def __str__(self):
        return self.title

#答案表
class Answer(models.Model):
    '''
    答案表
    '''
    title=models.CharField(max_length=255,verbose_name='答案')
    score=models.IntegerField()
    content=models.CharField(max_length=255,verbose_name='回答内容')

    Stu=models.ForeignKey(to='Student')
    question=models.ForeignKey(verbose_name='所属问题',to=Question)

#内容表:关联question
class Options(models.Model):
    '''
    内容表
    '''
    captions=models.CharField(max_length=64,verbose_name='问题的内容')
    score=models.IntegerField(default=10)
    question=models.ForeignKey(to=Question,verbose_name='所属问题')




#学生表
class Student(models.Model):
    '''
    学生表
    '''
    name=models.CharField(max_length=32,verbose_name='学生姓名')
    password=models.CharField(max_length=32,verbose_name='密码')
    group=models.ForeignKey(verbose_name='所属班级',to=Group)
