from django.contrib import admin
from article_reviewer.models import Category, Article, Review,User,UserProfile
# Register your models here.
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Review)
admin.site.register(User)
admin.site.register(UserProfile)