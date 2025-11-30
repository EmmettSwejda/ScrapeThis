from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from .forms import RegisterForm, MakeScrape


def home(request):
    return render(request, 'ScrapeDashboard/home.html')


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