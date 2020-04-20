from app_manage.models import Module
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from app_manage.forms import ModuleForm


@login_required
def list_module(request):
    """模块管理"""
    module_list = Module.objects.all()
    return render(request, "module/list.html", {"modules": module_list})


@login_required
def add_module(request):
    """创建模块"""
    if request.method == "POST":
        form = ModuleForm(request.POST)
        print("-------->form:", form)
        if form.is_valid():
            project = form.cleaned_data["project"]
            name = form.cleaned_data['name']
            describe = form.cleaned_data["describe"]
            Module.objects.create(name=name, describe=describe, project=project)
        return HttpResponseRedirect("/app_manage/module")
    else:
        form = ModuleForm()
    return render(request, "module/add.html", {'form': form})


@login_required
def edit_module(request, mid):
    """编辑模块"""
    if request.method == "POST":
        # 更新数据
        form = ModuleForm(request.POST)
        if form.is_valid():
            project = form.cleaned_data["project"]
            name = form.cleaned_data["name"]
            describe = form.cleaned_data["describe"]
            m = Module.objects.get(id=mid)
            m.name = name
            m.describe = describe
            m.project = project
            m.save()
        return HttpResponseRedirect("/app_manage/module")
    else:
        if mid:
            module = Module.objects.get(id=mid)
            form = ModuleForm(instance=module)
        else:
            form = ModuleForm()
        return render(request, "module/edit.html", {"form": form, "id": mid})


@login_required
def delete_module(request, mid):
    """删除模块"""
    if request.method == "GET":
        m = Module.objects.get(id=mid)
        m.delete()
        return HttpResponseRedirect("/app_manage/module")
    else:
        return HttpResponseRedirect("/app_manage/module")
