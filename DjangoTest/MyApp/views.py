from django.shortcuts import render
import datetime
from django.shortcuts import HttpResponse


# Create your views here.
# request参数必须有，名字是类似self的默认规则
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


def showstudents(request):
    list = [{'id': '1', 'name': 'Tom', 'age': '15'}, {'id': '2', 'name': 'Jack', 'age': '14'}]
    return render(request, 'index.html', {'students': list})
