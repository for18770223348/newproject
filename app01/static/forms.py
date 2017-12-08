from django.forms import ModelForm
from django.forms import widgets
from django.forms import fields

from django.forms import widgets as wd
from app01 import models



class QuestionModelForm(ModelForm):
    question_choice=fields.CharField(widget=widgets.Select(choices=(('1', '打分'),('2', '单选'),('3', '建议'))))
    class Meta:
        model = models.Question
        fields = ['title','question_choice']


class OptionModelForm(ModelForm):
    class Meta:
        model = models.Options
        fields = ['captions','score']

class Login(ModelForm):
    class Meta:
        model = models.UserInfo
        fields ="__all__"

# class Question_form(Form):
#     title=fields.CharField(widget=widgets.TextInput)
#
#     type=fields.CharField(widget=widgets.Select(choices=(('1', '打分'),('2', '单选'),('3', '建议'))))
#
#
#
#


