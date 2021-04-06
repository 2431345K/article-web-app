from django import forms
from django.contrib.auth.models import User

from article_reviewer.models import UserProfile, Article, Review


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('picture', 'author')


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'category', 'author', 'url', 'picture')


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('rating', 'comment')