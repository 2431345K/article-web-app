from django import forms
from django.contrib.auth.models import User

from article_reviewer.models import UserProfile, Article, Review


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', )


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('picture', )


class ArticleForm(forms.ModelForm):
    title = forms.CharField(label ="", widget = forms.Textarea(
    attrs ={
        'class':'form-control',
        'placeholder':'Title',
        'rows':1,
        'cols':50
    }))

    author = forms.CharField(label ="", widget = forms.Textarea(
    attrs ={
        'class':'form-control',
        'placeholder':'Author',
        'rows':1,
        'cols':50
    }))

    url = forms.CharField(label ="", widget = forms.Textarea(
    attrs ={
        'class':'form-control',
        'placeholder':'Article URL',
        'rows':3,
        'cols':50
    }))

    class Meta:
        model = Article
        fields = ('title', 'category', 'author', 'url', 'picture')


class ReviewForm(forms.ModelForm):
    comment = forms.CharField(label ="", widget = forms.Textarea(
    attrs ={
        'class':'form-control',
        'placeholder':'Comment here !',
        'rows':4,
        'cols':50
    }))
    rating = forms.IntegerField(label ="", widget = forms.Textarea(
    attrs ={
        'class':'form-control',
        'placeholder':"Rating(1-5)",
        'rows':1,
        'cols':50
    }))

    class Meta:
        model = Review
        fields = ('rating', 'comment')