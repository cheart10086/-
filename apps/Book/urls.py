from apps.Book.views import FrontAddView, FrontListView, UpdateView, DeletesView, FrontShowView, AddView, \
    ListView, OutToExcelView, BackModifyView, FrontModifyView,FrontAllView
from django.urls import path, re_path

# 正在部署的应用的名称
app_name = 'Book'

urlpatterns = [
    path('frontList/', FrontListView.as_view(), name='frontList'),  # 前台图书查询列表
    path('frontAdd/', FrontAddView.as_view(), name='frontAdd'),  # 前台图书添加
    path('frontAll/', FrontAllView.as_view(), name='frontAll'),
    path('frontShow/<str:barcode>/', FrontShowView.as_view(), name='frontShow'),  # 前台显示图片详情页
    path('update/<int:barcode>/', UpdateView.as_view(), name='update_book'),  # Ajax方式图书更新
    # path('^add$', AddView.as_view(), name='add'),  # 后台添加图书
    # url(r'^backModify/(?P<barcode>.+)$', BackModifyView.as_view(), name="backModify"),  # 后台更新图书
    # url(r'^list$', ListView.as_view(), name='list'),  # 后台图书列表
    path('deletes/', DeletesView.as_view(), name="delete_books"),  # 删除图书信息
    # url(r'^OutToExcel$', OutToExcelView.as_view(), name='OutToExcel')  # 导出图书信息到excel并下载
]
