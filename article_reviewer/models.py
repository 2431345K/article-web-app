from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
import uuid


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(unique=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name



class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  
    url = models.CharField(max_length=5000, unique=True)
    picture = models.ImageField(upload_to='article_images', blank=True)  
    author = models.CharField(max_length=30)
    averageRating = models.FloatField(default=3, validators=[MinValueValidator(1), MaxValueValidator(5)])
    reviews = models.CharField(max_length=280, blank=True)
    amountOfRatings = models.IntegerField(default = 0)
    totalRating = models.IntegerField(default = 0)

    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):

        return self.url


class Review(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE) 

    commentID = models.CharField(max_length=64, unique=True, default=uuid.uuid4)
    rating = models.IntegerField(default=3, validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(max_length=30)
    date = models.DateField(default=datetime.date.today())
    comment = models.CharField(max_length=280)

    def __str__(self):
        return self.comment


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    author = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username