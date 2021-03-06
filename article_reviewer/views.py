from django.shortcuts import render
from django.http import HttpResponse
from article_reviewer.forms import UserForm, ArticleForm, UserProfileForm, ReviewForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from article_reviewer.models import UserProfile, Article, Category, Review


def index(request):
    category_list = Category.objects.all()
    article_list = Article.objects.order_by('-averageRating')

    context_dict = {}
    context_dict['categories'] = category_list
    context_dict['articles'] = article_list

    return render(request, 'article_web_app/index.html', context=context_dict)


def category(request):
    category_list = Category.objects.all()
    article_list = Article.objects.order_by('-averageRating')

    context_dict = {}
    context_dict['categories'] = category_list
    context_dict['articles'] = article_list

    return render(request, 'article_web_app/category.html', context=context_dict)


def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        articles = Article.objects.filter(category=category)

        context_dict['articles'] = articles
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['articles'] = None
    return render(request, 'article_web_app/category.html', context=context_dict)


def show_article(request, article_name_slug):
    context_dict = {}
    try:
        article = Article.objects.get(slug=article_name_slug)
        reviews = Review.objects.filter(article=article)
        context_dict['article'] = article
        context_dict['reviews'] = reviews
    except Category.DoesNotExist:
        context_dict['article'] = None
    return render(request, 'article_web_app/article.html', context=context_dict)


def contact_us(request):
    return render(request, 'article_web_app/contact_us.html')


def sign_up(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
            login(request, user)
        else:
            print(user_form.errors)
            return HttpResponse("Register failed")
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'article_web_app/sign_up.html', context={'user_form': user_form, 'profile_form': profile_form,'registered': registered})


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
    user_profile = UserProfile.objects.get(user=request.user)
    context_dict['user_profile'] = user_profile
    return render(request, 'article_web_app/my_account.html', context=context_dict)


@login_required
def add_article(request):

    form = ArticleForm()
    context_dict = {'article_form': form}

    if request.method == 'POST':

        form = ArticleForm(request.POST)

        if form.is_valid():
            article = form.save(commit=False)
            if 'picture' in request.FILES:
                article.picture = request.FILES['picture']
            article.save()
            return redirect(reverse('article_reviewer:my_account'))
        else:
            print(form.errors)

    return render(request, 'article_web_app/add_article.html', context=context_dict)


def make_rating(request, article_name_slug):

    form = ReviewForm()
    context_dict = {'review_form': form}
    article = Article.objects.get(slug=article_name_slug)
    context_dict['article'] = article

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            comment = request.POST.get('comment')
            rating = request.POST.get('rating')
            review = Review.objects.create(article = article, author = request.user.username, comment = comment, rating = rating)
            review.save()

            review.article.totalRating = review.article.totalRating + int(review.rating)
            review.article.amountOfRatings = review.article.amountOfRatings + 1
            review.article.averageRating = review.article.totalRating/review.article.amountOfRatings
            review.article.save()
            return redirect(reverse('article_reviewer:index'))
        else:
            print(form.errors)

    return render(request, 'article_web_app/review.html', context=context_dict)