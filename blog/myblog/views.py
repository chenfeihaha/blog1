from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from myblog.models import Article
# Create your views here.
#def home(request):
#    return HttpResponse("Hello World, Django")

def home(request):
    post_list = Article.objects.all()  #获取全部的Article对象
    return render(request, 'home.html', {'post_list': post_list})
