from django.urls import path
from . import views




urlpatterns = [

    
    path('', views.index,name = 'insta-home'),
    path('post/update/<int:pk>',views.PostUpdateView.as_view(), name ='post-update'),

    path('post/<int:pk>/',views.PostDetailView.as_view(), name ='post-detail'),
    path('post/<int:pk>/update',views.PostUpdateView.as_view(), name ='post-update'),

    path('post/comment/<int:pk>/',views.CreateComment.as_view(), name ='post-comment'),


    path('post/new/', views.CreatePost.as_view(), name='create-post'),



]

