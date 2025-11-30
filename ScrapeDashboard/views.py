from urllib import request
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'ScrapeDashboard/home.html')


@login_required(login_url='/login')
def makeScrape(request):

    return render(request, 'ScrapeDashboard/base.html')

