# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
# from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.urls import reverse


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
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # request.POST是类似于字典的对象，可让您通过键名访问提交的数据。在这种情况下，
        # request.POST['choice']以字符串形式返回所选选项的ID。request.POST值始终是字符串
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
