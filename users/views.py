from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegestrationForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
# from friendship.models import Friend, Follow, Block
from .models import Profile


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegestrationForm(request.POST)


        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}! Your account has been created, Login!')

            user = form.save()
            user.save()
            profile = user.profile            

            return redirect('login')

    else:
        form = UserRegestrationForm()

    return render(request, 'users/register.html',{'form':form,})

@login_required
def profile(request):
    if request.method == 'POST':
    
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance = request.user.profile)


        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been updated!')
            return redirect('profile')


    else:
        
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)


    context = {
        'u_form':u_form,
        'p_form':p_form,
    }

    return render(request,'users/profile.html',context,)        




   