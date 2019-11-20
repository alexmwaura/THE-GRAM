from django.urls import path
from . import views




urlpatterns = [

    
    path('', views.index,name = 'insta-home'),
    path('post/update/<int:pk>',views.PostUpdateView.as_view(), name ='post-update'),

    path('post/<int:pk>/',views.PostDetailView.as_view(), name ='post-detail'),
    path('post/<int:pk>/update',views.PostUpdateView.as_view(), name ='post-update'),

    path('post/comment/<int:pk>/',views.comment, name ='post-comment'),


    path('post/new/', views.CreatePost.as_view(), name='create-post'),

    path (r'^search/',views.search_results,name= 'search_results'),
    path('like/<int:id>',views.upvote,name='like'),
    path('dislike/<int:id>',views.downvote,name='dislike'),
    path('home/<username>/',views.user_detail, name = 'user_follow'),


    path(r"^friend<username>",views.friendship_add_friend, name="friendship_add_friend",),

]

