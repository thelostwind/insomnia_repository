from django.shortcuts import render

from .models import User, Post

def index(request):
    latest_post_list = Post.objects.order_by('-post_timestamp')[:5]
    context = {}

