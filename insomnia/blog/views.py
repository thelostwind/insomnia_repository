from django.shortcuts import render, get_object_or_404

from .models import User, Post

def index(request):
    latest_post_list = Post.objects.order_by('-post_timestamp')[:5]
    context = {'latest_post_list' : latest_post_list}
    return render(request, 'blog/index.html', context)

