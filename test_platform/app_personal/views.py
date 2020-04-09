from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
# 用来写请求的处理逻辑


def hello(request):
    return HttpResponse("willcheng")


def hello2(request):
    return HttpResponse('<h1 style="color:red">willcheng2</h1>')


def hello3(request):
    return render(request, "hello.html")


def login(request):
    print("请求方法:", request.method)

    # 返回登录页
    if request.method == "GET":
        return render(request, "login.html")

    # 登录动作的处理
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        print("======>", username)
        print("======>", password)
        user = auth.authenticate(username=username, password=password)
        print("用户是否存在：", user)
        if username == "" or password == "":
            return render(request, "login.html", {"error": "用户名或密码不能为空"})
        if user is not None:
            auth.login(request, user)  # 记录用户的登录状态
            return HttpResponseRedirect("manage")
        else:
            return render(request, "login.html", {"error": "用户名或密码错误！"})


@login_required
def manage(request):
    return render(request, "manage.html")


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("login")
