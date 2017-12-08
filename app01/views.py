from django.shortcuts import render,HttpResponse,redirect
from app01.static.forms import QuestionModelForm,OptionModelForm,Login
from app01 import models
import json
from django.db.models import Sum,Count


def login(request):
    tag = {'is_login': None,'is_name':None,'is_password':None}
    if request.method=='GET':

        return render(request,'login.html')
    else:
        name=request.POST.get('name')
        pwd=request.POST.get('password')
        if name:
            tag['is_name']=True
            if pwd:
                tag['is_password']=True
                user_obj=models.UserInfo.objects.filter(name=name,password=pwd).first()

                if user_obj:
                    request.session['name']=name
                    tag['is_login']=True
                    print(name)
        return HttpResponse(json.dumps(tag))


def index(request):


    return render(request, 'index.html', {'questionAnire':questionAnire})

#问卷调查页面
class foo(object):
    def __init__(self,arg):
        self.arg=arg
    def __iter__(self):
        for item in self.arg:   #item 是没一个questionAnire对象
            # groups=models.Group.objects.filter(questionanire__id=item.id).first()  #找到该questionAnire对象的班级
            # p=models.Student.objects.filter(group__questionanire=item).annotate(c=Count('id')).values_list('c')

            # stu_count=models.Student.objects.filter(group=groups).count()

            yield  item                     #{'item':item,'stu_count':stu_count}
def questionAnire(request):

    questionAnire = models.Questionanire.objects.all()
    obj=foo(questionAnire)
    #1,首先要找班级人数.
    c=models.Student.objects.filter(group__questionanire__id=1).annotate(c=Count('id')).values_list('c')


    #2,做问卷调查的人数


    return render(request, 'questionAnire.html', {'obj': obj})




#增加问卷调查  没做
def add_questionAnire(request):

    return render(request,'add_questionAnire.html')



#编辑问卷调查页面
def edit_questionAnire2(request,nid):
    question_obj=models.Question.objects.filter(qs_anire=nid)

    def inner():   #如果没有问题就直接为空
        if not question_obj:
            form=QuestionModelForm()
            yield {'form':form,'question':None,'is_hide':'hide','option':None}

        else:
            for question in question_obj:  #遍历所有问题对象

                form=QuestionModelForm(instance=question)   #让form对象里面存了问题的对象

                temp={'form': form, 'question': question,'is_hide':'hide','option':None}

                if question.question_choice==2:
                    temp['is_hide']=''

                    def option_inner(ques):

                        option_obj=models.Options.objects.filter(question=ques)

                        for option in option_obj:

                            option_form=OptionModelForm(instance=option)
                            yield {'option_form':option_form,'obj':option}
                    temp['option']=option_inner(question)
                yield temp
    return render(request,'edit_questionAnire2.html',{'form_list':inner()})


# def edit_questionAnire2(request,nid):
#     question_obj=models.Question.objects.filter(qs_anire__id=nid)
#     question_list=[]
#     for question in question_obj:
#         form=Question_form(initial={'title':question.title,'type':question.question_choice})
#         question_list.append(form)
#
#
#
#     return render(request,'edit_questionAnire2.html',{'question_list':question_list})


#添加问题  PS:首先是隐藏添加内容按钮, 2,添加问题,当内容是单选,后面要显示一些内容 3, 要加上保存按钮
def add_question(request):

    form=QuestionModelForm()
    # ques=models.Question.objects.all().first()




    return render(request,'add_question.html',{'form':form})


#测试form
def logintst(request):
    user_obj=models.UserInfo.objects.all()
    if request.method=='GET':

        form=Login()
        return render(request,'logintst.html',{'form':form})
    else:

        form=Login(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/logintst/')
        else:
            return HttpResponse('not login')


#删除是直接点击X按钮,然后在页面上remove整个li,页面上就没有
#当你点击保存的时候才到后端处理数据.

def save(request):
    '''
    1:数据库直接更新,新添加数据到数据库.
    2:比对数据库,如果数据库和前端传过来的数据不匹配,那么就删除
    3.没有更改id,那么直接更新
    4,删除了某个id,比对数据库有没有这个id.
    :param request:
    :return:
    '''
    lst=json.loads(request.POST.get('lst'))
    print(lst)
    for content_list in lst:
        print(content_list)
        if content_list.get('quest_id'):

            content=models.Question.objects.filter(id=content_list['quest_id'])
            if content:
                if not content_list['option']:

                        #返回的是数字1   为什么
                    models.Question.objects.filter(id=content_list['quest_id']).update(title=content_list['quest_name'],question_choice=content_list['type_name'])

                else:  #不止改变的title 还改变了option
                    models.Question.objects.filter(id=content_list['quest_id']).update(title=content_list['quest_name'],
                                                                                       question_choice=content_list[
                                                                                           'type_name'])









    return HttpResponse('ok')








