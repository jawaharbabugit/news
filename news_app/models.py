from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category = models.CharField(max_length=15)
    def __str__(self):
        return self.category

class Publisher(models.Model):
    publisher = models.CharField(max_length=150)
    def __str__(self):
        return self.publisher

class userProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=13)
    category = models.ManyToManyField(Category,through="usercat")
    publisher = models.ManyToManyField(Publisher,through="userpub")
    def __str__(self):
        return self.user.name

class News(models.Model):
    title = models.CharField(max_length=400)
    short_desc = models.CharField(max_length=600)
    published = models.CharField(max_length=10)
    category = models.ManyToManyField(Category)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class newsDetail(models.Model):
    news = models.OneToOneField(News,on_delete=models.CASCADE)
    description = models.CharField(max_length=10000)
    pictures = models.ImageField(null=True)
    def __str__(self):
        return self.news.title

class usercat(models.Model):
    user = models.ForeignKey(userProfile,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)


class userpub(models.Model):
    user = models.ForeignKey(userProfile,on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher,on_delete=models.SET_NULL,null=True)


class newscat(models.Model):
    news = models.ForeignKey(News,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)