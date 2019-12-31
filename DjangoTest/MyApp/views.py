from django.shortcuts import render
import datetime
from django.shortcuts import HttpResponse
from MyApp import models


# Create your views here.
# request参数必须有，名字是类似self的默认规则
listStudents = {}


def index(request):
    # 不能直接返回字符串，必须是由HttpResponse类封装掐你的，这是django规则，不是python
    # return HttpResponse("Hello World")
    """

    当你想返回一个HTML文件时，就要用render方法来渲染
    render是django提供的方法和规则

    """
    s = 'Hello World'
    current_time = datetime.datetime.now()
    html = '<html><head></head><body><h1> %s </h1><p> %s </p></body></html>'%(s, current_time)
    return HttpResponse(html)


def Students(request):
    global listStudents
    if request.method == 'POST':
        name = request.POST.get('name', None)
        age = request.POST.get('age', None)
        print(name, age)
        stu = models.Student.objects.create(name=name, age=age)
        stu.save()
    return render(request, 'index.html')


def showData(request):
    listStudents = models.Student.objects.all()
    return render(request, 'index.html', {'data': listStudents})


def deleteUpdata(request):
    del_result = {}
    if request.method == 'POST' and request.POST:
        name = request.POST.get('name')
        nameIndb = models.Student.objects.filter(name=name).first()
        if nameIndb:
            nameIndb.delete()
            del_result['statu'] = 'success'
        else:
            del_result['statu'] = 'error'
    return render(request, 'index.html', {'del_result': del_result})


def changeUpdata(request):
    change_result = {}
    dbData = models.Student.objects.all()
    change_result['data'] = dbData
    if request.method == 'POST' and request.POST:
        name = request.POST.get('name')
        nameIndb = models.Student.objects.filter(name=name).first()
        if nameIndb:
            nameIndb.name = request.POST.get('name')
            nameIndb.age = request.POST.get('age')
            nameIndb.save()
            change_result['statu'] = 'success'
        else:
            change_result['statu'] = 'error'
    return render(request, 'index.html', {'change_result': change_result})


def showstudents(request):
    list = [{'id': '1', 'name': 'Tom', 'age': '15'}, {'id': '2', 'name': 'Jack', 'age': '14'}]
    return render(request, 'index.html', {'students': list})
