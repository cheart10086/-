from django.views.generic import View
from django.shortcuts import render
from apps.BookType.models import BookType
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect


class FrontAddView(View):
    def get(self, request):
        return render(request, 'BookType/bookType_add.html')

    def post(self, request):
        print("添加图书类型************************")
        id = request.POST.get("bookType_Id")
        name = request.POST.get("bookType_Name")
        day = request.POST.get("bookType_Day")

        try:
            # 如果 bookTypeId 是由外部提供的，并且你想用它作为主键，请确保它是唯一的
            # 如果不是主键，只是一个普通字段，并且你想保留外部提供的值，那么可以保留这行代码
            # 但通常，主键应该由数据库自动管理（如使用 AutoField）
            # 这里我假设 bookTypeId 不是一个主键，并且你想保留它
            book_type = BookType.objects.create(bookTypeId=id, bookTypeName=name, days=day)
            print("图书类型添加成功:", book_type)
            return redirect("BookType:frontList")
        except Exception as e:
            # 捕获所有异常，但最好捕获具体的异常类型以进行更精确的处理
            print("添加图书类型时发生错误:", e)
            # 可以记录日志、发送错误通知等
            # 返回给用户一个友好的错误页面
            return HttpResponse("添加图书类型时发生错误，请检查图书类型ID，它应该唯一。", status=500)


class ListAllView(View):
    def get(self, request):
        bookTypes = BookType.objects.all()
        bookTypeList = []
        for bookType in bookTypes:
            bookTypeObj = {
                'bookTypeId': bookType.bookTypeId,
                'bookTypeName': bookType.bookTypeName,
            }
            bookTypeList.append(bookTypeObj)
        return JsonResponse(bookTypeList, safe=False)


class FrontEditView(View):
    def get(self, request):
        type_Id = request.GET.get("type_Id")
        type_Name = request.GET.get("type_Name")
        type_Day = request.GET.get("type_Day")
        return render(request, "BookType/bookType_edit.html",
                      {"bookType_Id": type_Id, "bookType_Name": type_Name, "bookType_Day": type_Day})

    def post(self, request):
        id = request.POST.get("bookType_Id")
        name = request.POST.get("bookType_Name")
        day = request.POST.get("bookType_Day")
        print(id, name, day)
        result = BookType.objects.filter(bookTypeId=id).update(bookTypeId=id, bookTypeName=name, days=day)
        print(id, name, day)
        return redirect("BookType:frontList")


class FrontDeleteView(View):
    def get(self, request):
        type_Id = request.GET.get("type_Id")
        BookType.objects.filter(bookTypeId=type_Id).delete()
        return redirect("BookType:frontList")


class FrontListView(View):
    def get(self, request):
        pageSize = 5
        currentPage = request.GET.get("currentPage")
        bookTypes = BookType.objects.all()
        paginator = Paginator(bookTypes, pageSize)
        totalPage = paginator.num_pages
        recordNumber = paginator.count

        # 获取第page页的内容
        try:
            currentPage = int(currentPage)
        except Exception as e:
            currentPage = 1
        if currentPage > totalPage:
            currentPage = totalPage

        # 获取第page页的Page实例对象
        bookTypes_page = paginator.page(currentPage)

        startIndex = (currentPage - 1) * pageSize  # 计算起始序号

        startPage = currentPage - 5
        endPage = currentPage + 5
        if startPage < 1:
            startPage = 1
        if endPage > totalPage:
            endPage = totalPage;

        pageList = list(range(startPage, endPage + 1))

        context = {
            'bookTypes_page': bookTypes_page,
            'currentPage': currentPage,
            'totalPage': totalPage,
            'recordNumber': recordNumber,
            'startIndex': startIndex,
            'pageList': pageList,
        }

        print(pageList)

        # 使用模板
        return render(request, 'BookType/bookType_frontquery_result.html', context)

    def post(self, request):
        pass
