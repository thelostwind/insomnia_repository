from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string


from .models import User, Post, Navigation, Category, Comments, Info

info = Info()

def index(request):
    latest_post_list = Post.objects.order_by('-post_timestamp')[:5]
    context = {'latest_post_list' : latest_post_list}
    return render(request, 'blog/index.html', context)


def blog(request):
    post_list = Post.objects.order_by('post_timestamp')
    category_list = Category.objects.order_by('id')
    recent_comments = Comments.objects.order_by('comment_date')
    context = { 'header' : render_header(request),
                'content' : render_content(request),
                'sidebar' : render_sidebar(request),
                'footer' : render_footer(request),
                }
    return render(request, 'blog/index.html', context)


def render_header(request):
    
    navigation_list = Navigation.objects.order_by('-nav_seq')
    headinfo = info.get_head_info()
    
    context = {'navigation_list' : navigation_list,
                'headinfo' : headinfo,
            }

    return render_to_string('header.html', context)


def render_content(request):
    post_list = Post.objects.order_by('post_timestamp')
    
    context = {'post_list' : post_list, 
            }

    return render_to_string('content.html', context)


def render_sidebar(request):
    category_list = Category.objects.order_by('id')
    recent_comments = Comments.objects.order_by('comment_date')

    context = {'category_list' : category_list,
                'recent_comments' : recent_comments,
                }

    return render_to_string('sidebar.html', context)



def render_footer(request):
    return render_to_string('footer.html')
