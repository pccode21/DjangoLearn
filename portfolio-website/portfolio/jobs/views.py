from django.shortcuts import render
from django.http import HttpResponse

from .models import Job

# Create your views here.

def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs' : jobs} )
