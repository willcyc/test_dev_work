from django.urls import path
from app_manage.views import project_view, module_view

urlpatterns = [
    # 项目管理
    path('project', project_view.list_project, name='project'),
    path('project/add', project_view.add_project, name='add'),
    path('project/edit/<int:pid>', project_view.edit_project, name='edit'),
    path('project/delete/<int:pid>', project_view.delete_project, name='delete'),

    # 模块管理
    path('module', module_view.list_module, name='module'),
    path('module/add', module_view.add_module, name='add'),
    path('module/edit/<int:mid>', module_view.edit_module, name='edit'),
    path('module/delete/<int:mid>', module_view.delete_module, name='delete'),
]
