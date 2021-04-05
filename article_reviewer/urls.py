from django.urls import path
from article_reviewer import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'article_reviewer'

urlpatterns = [
    path('contact_us/', views.contact_us, name='contact_us'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('login/my_account/', views.my_account, name='my_account'),
    path('category/', views.category, name='category'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('category/<slug:category_name_slug>/<slug:article_name_slug>', views.article, name='article'),
    path('login/my_account/add_article/', views.add_article, name='add_article'),
    path('category/article/make_rating', views.make_rating, name='make_rating'),
    path('', views.index, name='index'),
]