from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from .forms import RegisterForm, MakeScrape
from .models import ScrapeConfig
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin, urlparse
import re
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
    scrapes = ScrapeConfig.objects.all().filter(owner=request.user)

    for item in scrapes:
        item.website_url = urlparse(item.website_url).netloc

    if request.method == 'POST':
        id = request.POST.get('post-id')

        post = ScrapeConfig.objects.filter(id=id).first()
        if post.owner == request.user:
            post.delete()
            return redirect('home')

    scrape = ScrapeConfig.objects.filter(id=item_id).first()
    headers = {'Accept-Encoding': 'identity'}
    page = requests.get(scrape.website_url, headers=headers).text

    soup = BeautifulSoup(page, "html.parser")

    css_links = [link["href"] for link in soup.find_all("link", rel="stylesheet")]
    css_content = {}

    for link in css_links:
        css_url = urljoin(scrape.website_url, link)
        css_data = requests.get(css_url).text
        css_content = css_data

    if css_content:
        css_content = css_content.replace('body', '#showpage')
        css_content = css_content.replace('html', '#showpage')

        css_content = add_prefix_to_selectors(css_content, '#showpage ')

    context = {
        'scrape': scrape,
        'page': page,
        'css_content': css_content,
        'scrapes': scrapes,
    }
    return render(request, 'ScrapeDashboard/viewScrape.html', context)



def add_prefix_to_selectors(css, prefix):
    def replacer(match):
        selectors = match.group(2)
        updated = ", ".join(prefix + s.strip() for s in selectors.split(","))
        return f"{match.group(1)} {updated}"

    return re.sub(r'(^|\})\s*([^{]+)', replacer, css)


@login_required(login_url='login')
def make_scrape(request):
    if request.method == 'POST':
        form = MakeScrape(request.POST)
        if form.is_valid():
            sform = form.save(commit=False)
            sform.owner = request.user
            sform.save()
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