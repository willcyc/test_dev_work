from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app_manage.models import Project
from app_manage.forms import ProjectForm, ProjectEditForm
from django.http import HttpResponseRedirect
# Create your views here.


@login_required
def list_project(request):
    """项目管理"""
    username = request.COOKIES.get('user', '')  # 登录后显示用户名
    projects_list = Project.objects.all()
    return render(request, "project/list.html",{"projects": projects_list, "user":  username})


@login_required
def add_project(request):
    """创建项目"""
    # print("创建项目")
    if request.method == "POST":
        form = ProjectForm(request.POST)
        print("-------->form:", form)
        if form.is_valid():
            name = form.cleaned_data['name']
            describe = form.cleaned_data["describe"]
            status = form.cleaned_data["status"]
            Project.objects.create(name=name, describe=describe, status=status)
        return HttpResponseRedirect("/app_manage/project")
    else:
        form = ProjectForm()
    return render(request, "project/add.html", {'form': form})


@login_required
def edit_project(request, pid):
    """编辑项目"""
    print("------>pid:", pid)
    if request.method == "POST":
        # 更新数据
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            describe = form.cleaned_data["describe"]
            status = form.cleaned_data["status"]
            p = Project.objects.get(id=pid)
            p.name = name
            p.describe = describe
            p.status = status
            p.save()
        return HttpResponseRedirect("/app_manage/project")
    else:
        if pid:
            project = Project.objects.get(id=pid)
            form = ProjectEditForm(instance=project)
        else:
            form = ProjectForm()
        return render(request, "project/edit.html", {"form": form, "id": pid})


@login_required
def delete_project(request, pid):
    if request.method == "GET":
        p = Project.objects.get(id=pid)
        p.delete()
        return HttpResponseRedirect("/app_manage/project")
    else:
        return HttpResponseRedirect("/app_manage/project")
