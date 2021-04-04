from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    
    class Meta:
        verbose_name_plural = 'Categories'

    
    def __str__(self):
        return self.name


##
##returns yrl of article and not the name(title)
class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE) ##links to category
    
    url = models.URLField(max_length = 100, unique = True)
    picture =  models.ImageField() ##define more about image 
    author  = models.CharField(max_length=30)
    averageRating = models.IntegerField(default=None)
    Reviews = models.CharField(max_length=100)
    
    title = models.CharField(max_length=128)
    
    #views = models.IntegerField(default=0)
    def __str__(self):
        return self.url
        
 
 
 # review page - what should it return, foreign keys and max length of raring ?        
class Review (models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE) #think this links it to article name
    
    commentID = models.IntegerField(max_length=None, unique=True)
    rating = models.IntegerField(default=0)
    author  = models.CharField(max_length=30)
    date =  models.DateField()
    comment = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.commentID
 
# more on image field 
#class below should it be included 
class User (models.Model):
   username =  models.CharField(max_length=30, unique=True)
   password = models.CharField(max_length=30)
   profilePicture = models.ImageField() ##define more about image 
   author = models.BooleanField()
    
   def __str__(self):
    return self.username
##
        
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ##website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    author = models.BooleanField()

    def __str__(self):
        return self.user.username