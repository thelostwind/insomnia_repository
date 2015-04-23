from django.shortcuts import render, get_object_or_404

from .models import User, Post, Navigation, Info

info = Info()

def index(request):
    latest_post_list = Post.objects.order_by('-post_timestamp')[:5]
    context = {'latest_post_list' : latest_post_list}
    return render(request, 'blog/index.html', context)

def blog(request):
    navigation_list = Navigation.objects.order_by('-nav_seq')
    headinfo = info.get_head_info()
    context = {'navigation_list' : navigation_list,
                'headinfo' : headinfo,}
    return render(request, 'blog/header.html', context)
