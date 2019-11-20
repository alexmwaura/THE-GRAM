from django.shortcuts import render,get_object_or_404,redirect,reverse,HttpResponseRedirect
from .models import *
from users.models import *
from django.contrib import messages
from django.http import JsonResponse
import json
from django.conf import settings
from django.http import HttpResponse
from . forms import PostForm
from django.views.generic import  DetailView,UpdateView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

from . forms import CommentForm


@login_required
def index(request):
    post = Post.objects.all()
    comment = Comment.objects.all()
    
             
    return render(request,'post/index.html',{'post':post,'comment':comment})


class PostDetailView(DetailView):
    model = Post






class PostUpdateView(LoginRequiredMixin, UpdateView,UserPassesTestMixin):
    model = Post
    fields = ['title','cover']

    def form_valid(self, form):
        form.instance.account_user= self.request.user
              
        # print(form.instance.date_posted)
        # return super().form_valid(form)
        form.save()
        # print(form.instance.title)
        # obj1=Post.objects.create(profile_user)


       
        return redirect('insta-home')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False    



@login_required
def comment(request,pk):
    current_user = request.user
    post = Post.objects.get(pk=pk)
    comments = Comment.get_comments(post.id)
    form = CommentForm(request.POST)
    if request.method == 'POST':
        if form.is_valid:
            comment = form.save(commit=False)
            comment.user = current_user
            comment.post = post
            comment.post_id = post.id
            comment.save()
            return redirect('insta-home')

        else:
            form = CommentForm()

    return render(request, 'Post/comment_form.html',{'form':form, 'post':post, 'comments':comments})            



class CreatePost(LoginRequiredMixin, CreateView,UserPassesTestMixin):
    model = Post
    fields = ['title','cover']
    

    def form_valid(self, form):

        form.instance.account_user= self.request.user
        form.instance.profile_user= Profile.objects.get(id=self.request.user.profile.id)
        

        form.save()


        return redirect('insta-home')



@login_required
def search_results(request):
    if 'username' in request.GET and request.GET['username']:
        user = request.GET.get("username")
        searched_user = Post.get_user(user) 
        message = f'{user}'
        return render (request,'post/search.html',{"message":message,"post":searched_user})

    else:
        message = "You haven't searched for any name"

    return render(request,'post/search.html',{'message':message})

@login_required
def upvote(request,id):
    post = Post.objects.get(id =id)
    post.like += 1

    post.save()
    

    return redirect('insta-home')   
@login_required
def downvote(request,id):
    post = Post.objects.get(id =id)

    post.dislike += 1
    post.save()
    

    return redirect('insta-home')


def user_detail(request, username):
    query = request.user.rel_from_set.all()    
    template = 'post/detail.html'
    return render(request, template, {'query':query})





