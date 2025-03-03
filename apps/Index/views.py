from django.shortcuts import render
from django.views.generic import View
from apps.Index.models import Admin
from django.shortcuts import redirect
from apps.Book.models import Book
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def login_auth(func):
    def inner(request, *args, **kwargs):
        url = request.get_full_path()
        session_name = request.session.get('username')
        print(session_name)
        if request.session.get('username'):
            res = func(request, *args, **kwargs)
            return res
        else:
            return redirect('/login')

    return inner


class IndexView(View):
    def get(self, request):
        # 显示首页,使用模板
        return render(request, 'index.html')


class AdminView(View):
    def get(self, request):
        # username = request.session.get('username', '')
        result = Book.objects.all()
        return render(request, 'admin.html', {"result": result})


class LoginView(View):
    # 后台登录页面
    def get(self, request):
        error_msg = ''
        return render(request, 'login.html', {'error_msg': error_msg})

    def post(self, request):
        # 登录校验接收数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            admin = Admin.objects.get(username=username, password=password)
            request.session['username'] = username
            data = {'msg': '登录成功', 'success': True}
            error_msg = '登录成功'
            return redirect("Index:adminView")
        except Admin.DoesNotExist:
            # 用户名密码错误
            data = {'msg': '登录失败', 'success': False}
            error_msg = '用户名或密码错误'
            return render(request, 'login.html', {'error_msg': error_msg})

