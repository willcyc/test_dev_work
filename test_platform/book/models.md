### 1、Django MTV
M：models数据库的操作
T：templates 模版 HTML页面
V：view 视图，处理请求

### 2、python操作数据库流程
```python------>django ORM----->驱动（pymysql）---->数据库```

### 3、官方文档地址
```https://docs.djangoproject.com/zh-hans/3.0/intro/tutorial02/```

### 4、数据库创建
```
class Project(models.Model):
    """项目表"""
    name = models.CharField("名称", max_length=100, null=False, default="")
    describe = models.TextField("描述", default="")
    status = models.BooleanField("状态", default=True)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    update_time = models.DateTimeField("更新时间", auto_now=True)

```
**参数说明：**<br>
* max_length最大长度
* default 默认值
* null针对数据库，null=True表示该字段允许为空
* blank针对表单，blank=True表示表单该字段允许为空
* auto_now每次更新数据，都会获得最新时间
* auto_now_add获取数据被创建时间
* on_delete指定关联数据，models CASCADE表示删除关联数据时，与之关联也删除

### 5、数据库操作
**新增：**
* Project.objects.create(name="项目",describe="描述")
* Project(name="项目",describe="描述").save()


**查询：**
* Project.objects.all()   
* Project.objects.get(pk=1)
* Project.objects.filter(status=1)
* Project.objects.filter(name__contains='项目')

**更新**<br>
*方式一：*
```
a = Project.objects.get(name="project_name")
a.status = 0
a.save()
```
*方式二：*
* Project.objects.select_for_update().filter(name__contains="project").update(describe="00000")
方式一适合单条修改，方式二适合多条修改

**删除**<br>
* Project.objects.get(name="名称").delete()





