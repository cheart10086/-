from apps.BookType.views import FrontAddView, FrontListView, ListAllView, FrontEditView, FrontDeleteView
from django.urls import path, re_path

# 正在部署的应用的名称
app_name = 'BookType'

urlpatterns = [
    path(r'frontAdd', FrontAddView.as_view(), name='frontAdd'),  # 前台添加
    path(r'frontList', FrontListView.as_view(), name='frontList'),  # 前台查询列表
    path(r'listAll', ListAllView.as_view(), name='listAll'),  # 前台查询所有图书类型
    path(r'frontEdit', FrontEditView.as_view(), name='frontEdit'),  # 前台修改
    path(r'frontDelete', FrontDeleteView.as_view(), name='frontDelete'),  # 前台删除
]
