from django.shortcuts import render,get_object_or_404,redirect,reverse,HttpResponseRedirect
from .models import Post,Comment
from users.models import *
from django.contrib import messages
from django.http import JsonResponse
import json
from django.http import HttpResponse
from . forms import PostForm
from django.views.generic import  DetailView,UpdateView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

from . forms import CommentForm

# Create your views here.



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


# class CreateComment(LoginRequiredMixin, CreateView,UserPassesTestMixin):
#     model = Comment
#     fields = ['text']

#     def form_valid(self, form):
#         form.instance.user= self.request.user
#         form.instance.post = Post.objects.get(id=self.request.user.pk)

#         form.save()
#         return redirect('insta-home')

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

# def product_like(request, id):
# 	get_product = get_object_or_404(Post, id=id)
# 	rating_status = {}
# 	if request.is_ajax:
# 		if request.user in get_product.user.all():
# 			get_product.rating_count -= 1
# 			get_product.user.remove(request.user)
# 			get_product.save()
# 			rating_status['Removed'] = "True"
# 			rating_status['count'] = get_product.rating_count
# 			return HttpResponse(JsonResponse(rating_status))
# 		else:
# 			get_product.rating_count += 1
# 			get_product.user.add(request.user)
# 			get_product.save()
# 			rating_status['Success'] =  "True"
# 			rating_status['count'] = get_product.rating_count
# 			return HttpResponse(JsonResponse(rating_status))
# 	else:
# 		rating_status['Success'] =  "False"
# 		return HttpResponse(JsonResponse(rating_status))
# 	return request       

 

# def get_followers(request):

#     user_ids = FollowersAndFollowing.objects.filter(followed_by=request.user).values_list('id',flat=True)
#     Post.objects.filter(post_created_user__in = user_ids)

#     return redirect ('profile')    


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


def upvote(request,id):
    post = Post.objects.get(id =id)
    post.like += 1

    post.save()
    

    return redirect('insta-home')   

def downvote(request,id):
    post = Post.objects.get(id =id)

    post.dislike += 1
    post.save()
    

    return redirect('insta-home')


  