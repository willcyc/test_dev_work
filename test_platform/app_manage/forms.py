from django import forms
from django.forms import widgets
from app_manage.models import Project, Module


# Django form表单设计，如：登录时提交的的form表单
class ProjectForm(forms.Form):
    name = forms.CharField(label="名称", max_length=100, widget=widgets.TextInput(attrs={"class": "form-control"}))
    describe = forms.CharField(label="描述", widget=widgets.Textarea(attrs={"class": "form-control"}))  # 文本框
    status = forms.BooleanField(label="状态", required=False, widget=widgets.CheckboxInput())  # 布尔型


class ProjectEditForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'describe', 'status']


class ModuleForm(forms.ModelForm):
    # project = forms.CharField(label="项目", widget=widgets.Select(attrs={"class": "form-control"}))
    # name = forms.CharField(label="名称", max_length=100, widget=widgets.TextInput(attrs={"class": "form-control"}))
    # describe = forms.CharField(label="描述", widget=widgets.Textarea(attrs={"class": "form-control"}))  # 文本框
    class Meta:
        model = Module
        fields = ['project', 'name', 'describe']
