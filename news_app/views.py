from django.shortcuts import render
from . import models

def home(request):
    news_list = models.News.objects.all()
    return render(request,'news_app/news.html',{'newslist':news_list})
