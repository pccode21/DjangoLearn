from django.shortcuts import HttpResponse

# Create your views here.
# request参数必须有，名字是类似self的默认规则
def index(request):
    # 不能直接返回字符串，必须是由HttpResponse类封装掐你的，这是django规则，不是python
    return HttpResponse("Hello World")
