### 1、Django官方文档
```https://docs.djangoproject.com/zh-hans/3.0/intro/tutorial01/```

### 2、创建Django项目
```
django-admin startproject 项目名称
```

### 3、启动Django项目
```
1、cd到manage.py文件所在目录
2、输入python manage.py runserver回车
3、访问127.0.0.1:8000地址
```

### 4、创建应用
```
1、python manage.py startapp 应用名称
2、将应用名称添加到settings.py文件的INSTALLED_APPS列表中
```

### 5、Django的处理流程
```
1、指定URL路径，如：hello
2、在settings.py文件匹配到URL的配置文件
3、urls.py匹配路径hello，把请求指到views.py文件
4、在views.py文件中写入response的处理，把templates目录下的html文件返回给客户端
```

