from django.shortcuts import render
from django.http import HttpResponse
from article_reviewer.forms import UserForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.
from article_reviewer.models import UserProfile, Article, Category


def index(request):
    category_list = Category.objects.all()
    article_list = Article.objects.order_by('-averageRating')[:5]

    context_dict = {}
    context_dict['categories'] = category_list
    context_dict['articles'] = article_list

    return render(request, 'article_web_app/index.html', context=context_dict)


def show_category(request, category_name_slug):

    context_dict = {}
    try:

        category = Category.objects.get(slug=category_name_slug)
        articles = Article.objects.filter(category=category)

        context_dict['articles'] = articles
        context_dict['category'] = category
    except Category.DoesNotExist:

        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'article_web_app/category.html', context=context_dict)


def contact_us(request):
    return render(request, 'article_web_app/contact_us.html')


def sign_up(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        # profile_form = UserProfileForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            # profile = profile_form.save(commit=False)
            # profile.user = user

            # if 'picture' in request.FILES:
            #     profile.picture = request.FILES['picture']
            #
            # profile.save()
            registered = True
        else:
            print(user_form.errors)
            return HttpResponse("Register failed")
    else:
        user_form = UserForm()
        # profile_form = UserProfileForm()

    return render(request, 'article_web_app/sign_up.html', context={'user_form': user_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('article_reviewer:index'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'article_web_app/login.html')
    return render(request, 'article_web_app/login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('article_reviewer:index'))


@login_required
def my_account(request):
    context_dict = {}
    # user_profile = UserProfile.objects.get(user=request.user)
    context_dict['picture'] = ""#user_profile.picture
    return render(request, 'article_web_app/my_account.html', context=context_dict)


def category(request):
    return render(request, 'article_web_app/category.html')

@login_required
def article(request):
    return HttpResponse("This is article page")


def add_article(request):
    return render(request, 'article_web_app/add_article.html')


def make_rating(request):
    return HttpResponse("This is make rating page")
