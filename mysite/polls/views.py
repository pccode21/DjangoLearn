from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question
# from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404


def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    # template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list}
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)
    """该render()函数将请求对象作为其第一个参数，将模板名称作为其第二个参数，并将字典作为其可选的第三个参数。
    它返回使用HttpResponse 给定上下文呈现的给定模板的对象"""


def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)
    # try:
    #    question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #    raise Http404('Question does not exist')  # 此处的新概念：Http404如果不存在具有所请求ID的问题，则视图引发异常。
    question = get_object_or_404(Question, pk=question_id)
    """该get_object_or_404()函数将Django模型作为其第一个参数，并将任意数量的关键字参数作为参数传递给get()模型管理器的函数。
    Http404如果对象不存在，它将引发。"""
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
