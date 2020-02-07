from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')


def about(request):
    return HttpResponse("This is the About Page")


def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    wordfrequenter = {}

    for word in wordlist:
        if word in wordfrequenter:
            wordfrequenter[word] += 1
        else:
            wordfrequenter[word] = 1

    sortedwords = sorted(wordfrequenter.items(), key=operator.itemgetter(1), reverse=True)


    context = {
        "fulltext"       : fulltext,
        "count"          : len(wordlist),
        'sortedwords'    : sortedwords
    }
    return render(request, 'count.html', context=context)
