from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from .forms import RegisterForm, MakeScrape
from .models import ScrapeConfig


def home(request):
    scrapes = None
    if request.user.is_authenticated:
        if request.method == 'POST':
            id = request.POST.get('post-id')

            post = ScrapeConfig.objects.filter(id=id).first()
            if post.owner == request.user:
                post.delete()
        else:
            scrapes = ScrapeConfig.objects.all().filter(owner=request.user)

    return render(request, 'ScrapeDashboard/home.html', { "scrapes": scrapes })

@login_required(login_url='login')
def view_scrape(request, item_id):

    if request.method == 'POST':
        id = request.POST.get('post-id')

        post = ScrapeConfig.objects.filter(id=id).first()
        if post.owner == request.user:
            post.delete()
            return redirect('home')

    scrape = ScrapeConfig.objects.filter(id=item_id).first()

    return render(request, 'ScrapeDashboard/viewScrape.html', { "scrape": scrape })



@login_required(login_url='login')
def make_scrape(request):
    if request.method == 'POST':
        form = MakeScrape(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MakeScrape()


    return render(request, 'ScrapeDashboard/MakeScrape.html', {'form': form})



def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')

    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {'form': form})

def LogOut(request):
    logout(request)
    return redirect('/login')