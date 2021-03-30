from django.urls import path
from article_reviewer import views

app_name = 'article_reviewer'

urlpatterns = [
    path('home/', views.index, name='index'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', views.login, name='login'),
    path('login/my_account', views.my_account, name='my_account'),
    path('category/', views.category, name='category'),
    path('category/article', views.article, name='article'),
    path('category/add_article', views.add_article, name='add_article'),
    path('category/article/make_rating', views.make_rating, name='make_rating'),
    path('', views.index, name='index'),
]