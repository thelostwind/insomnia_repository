from django.shortcuts import render, get_object_or_404

from .models import User, Post, Navigation, Category, Comments, Info

info = Info()

def index(request):
    latest_post_list = Post.objects.order_by('-post_timestamp')[:5]
    context = {'latest_post_list' : latest_post_list}
    return render(request, 'blog/index.html', context)

def blog(request):
    navigation_list = Navigation.objects.order_by('-nav_seq')
    post_list = Post.objects.order_by('post_timestamp')
    category_list = Category.objects.order_by('id')
    recent_comments = Comments.objects.order_by('comment_date')
    headinfo = info.get_head_info()
    context = {'navigation_list' : navigation_list,
                'headinfo' : headinfo,
 		'post_list' : post_list,
                'category_list' : category_list,
                'recent_comments' : recent_comments,}
    return render(request, 'blog/header.html', context)
