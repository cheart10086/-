from django.urls import path, re_path
# from apps.Index.views import IndexView,FrontLoginView,FrontLoginOutView,LoginView,LoginOutView,MainView,ChangePasswordView
from apps.Index.views import IndexView,AdminView,LoginView
# 正在部署的应用的名称
app_name = 'Index'

urlpatterns = [
    path(r'', IndexView.as_view(), name='index'),  # 首页
    # url(r'^frontLogin$', FrontLoginView.as_view(), name='frontLogin'),  # 前台登录
    path(r'adminView/', AdminView.as_view(), name='adminView'),  # 管理中心
    # url(r'^frontLoginout$', FrontLoginOutView.as_view(), name='frontLoginout'),  # 前台退出
    path(r'login/', LoginView.as_view(), name="login"),  # 后台登录
    # url(r'^loginout$', LoginOutView.as_view(), name="loginout"),  # 后台退出
    # url(r'^changePassword$', ChangePasswordView.as_view(), name='changePassword'),  # 管理员修改密码
]
