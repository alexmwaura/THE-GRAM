from django.shortcuts import render
from .models import Post
# Create your views here.


def index(request):
    post = Post.objects.all()


    return render(request,'post/index.html',{'post':post})