# django的模版划分
* html页面中包含的基本内容
```
<html>
    <head></head>
    <body>
        <div>导航</div>
        <div>模块一</div>
        <div>模块二</div>
        <div>模块三</div>
    </body>
</html>
```

* 创建base.html文件
```
<html>
    <head></head>
    <body>
        <div>导航</div>
        {% block base %}

        {% endblock %}
    </body>
</html>
```

* 其他html文件继承base.html文件
page1.html
```
{% extends "base.html" %}
{% block base %}
    <div>模块一</div>
{% endblock %}
```

* page2.html
```
{% extends "base.html" %}
{% block base %}
    <div>
    模块二
    {% block page %}
        <!-- 子模块 -->
    {% endblock %}
    </div> 
{% endblock %}
```

* page2-module2.html
```
{% extends "page2.html" %}
{% block page %}
<div>模块3</div>
{% endblock %}
```

