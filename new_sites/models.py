from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):

    title = models.CharField(max_length = 200)
    text = models.TextField()
    image = models.ImageField(upload_to = 'image/set/', null = True, blank = True)
    urllink = models.CharField(max_length=5000, null = True, blank = True)

    date_added = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):

        return self.title[:50]

class TopicHome(models.Model):
     
    title = models.CharField(max_length = 200)
    text = models.TextField()
    image = models.ImageField(upload_to = 'image/set/', null = True, blank = True)
    urllink = models.CharField(max_length=5000, null = True, blank = True)

    date_added = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):

        return self.title[:50]

    

class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    link = models.CharField(max_length=5000)
    pdf = models.FileField(upload_to ='books/pdfs/')
    cover = models.ImageField(upload_to = 'books/cover/', null = True, blank = True)
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return self.title

