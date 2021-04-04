from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    context_dict = {'test': 'Test'}
    return render(request, 'article_web_app/index.html', context=context_dict)

def contact_us(request):
    return HttpResponse("This is contact us page")


def sign_up(request):
    return HttpResponse("This is sign up page")


def login(request):
    return HttpResponse("This is login page")


def my_account(request):
    return HttpResponse("This is my account page")


def category(request):
    return HttpResponse("This is category page")


def article(request):
    return HttpResponse("This is article page")


def add_article(request):
    return HttpResponse("This is add article page")


def make_rating(request):
    return HttpResponse("This is make rating page")