from django.shortcuts import render, get_object_or_404, render_to_response
from django.template.loader import render_to_string 


from django.core.paginator import Paginator, Page, EmptyPage, PageNotAnInteger

from .models import User, Post, Navigation, Category, Comments, Info

info = Info()

def index(request):
    latest_post_list = Post.objects.order_by('-post_timestamp')[:5]
    context = {'latest_post_list' : latest_post_list}
    return render(request, 'blog/index.html', context)

'''
def blog(request):
    post_list = Post.objects.order_by('post_timestamp')
    category_list = Category.objects.order_by('id')
    recent_comments = Comments.objects.order_by('comment_date')
    context = { 'header' : render_header(request),
                'content' : render_contents(request),
                'sidebar' : render_sidebar(request),
                'footer' : render_footer(request),
                }
    return render(request, 'blog/index.html', context)
'''


def blog(request):
    return pages(request)


def article(request, post_id, contexts=None):
    context = { 'header' : render_header(request),
                'content' : render_article(request, post_id, contexts),
                'sidebar' : render_sidebar(request),
                'footer' : render_footer(request),
            }
    return render_to_response('index.html', context)


def pages(request, num='1'):
    context={   'header' : render_header(request),
                'footer' : render_footer(request),
                'contents' : render_pages(request, num, more = 640),
                'sidebar' : render_sidebar(request),
    }
    return render_to_response('index.html', context)


def render_header(request):
    
    navigation_list = Navigation.objects.order_by('-nav_seq')
    headinfo = info.get_head_info()
    
    context = {'navigation_list' : navigation_list,
                'headinfo' : headinfo,
            }

    return render_to_string('header.html', context)


def render_pages(request, num = '1', more = 300):
    context = {}
    if(long(num) <= 0):
        num = 1
    page = None
    post_id = None
    if post_id:
        return render_article(request, post_id)
    else:
        post_list = Post.objects.all().order_by('-post_timestamp')
        if more:
            return render_page_more(post_list, num, more = more)
        else:
            return render_page1(posts_list, num)
    return render_to_string('page.html', context)


def render_article(request, post_id, contexts=None):
    objs = Post.objects.all()
    
    prev_post = objs.filter(id__lt = post_id).only('id', 'post_title').last()
    cur_post = objs.filter(id=post_id)
    next_post = objs.filter(id__gt = post_id).only('id', 'post_title').first()
    

    contents = render_contents(cur_post)
    
    comment_author = None
    if 'comment_author' in request.session:
        comment_author = request.session['comment_author']

    comments = Comments.objects.filter(comment_post_id = post_id).order_by('comment_date')

    return render_page1(cur_post, 1, render_comment(request, post_id, comments, contexts))

def render_page1(posts, num = '1', nator = None, comment = None, num_page = 5):
    paginator = MyPaginator(posts, num_page)
    try:
        page = paginator.page(num)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    conents = render_contents(page)

    context = { 'page_conents' : contents, }

    if comment != None:
        context['page_comment'] = comment
    return render_to_string('page.html', context)


def render_page_more(posts, num='1', nator=None, comment=None, num_page=5,more=300):
#    paginator = MyPaginator(posts, num_page)
#    try:
#        page = paginator.page(num)
#    except PageNotAnInteger:
#        page = paginator.page(1)
#    except EmptyPage:
#        page = paginator.page(paginator.num_pages)
#    if more:
#        contents = render_contents(page, more = more)
#    if nator != None:
#        nator = render_nator(page)
 
    contents = render_contents(posts, more = more)

    context = {
            'page_contents' : contents,
#            'page_nator' : nator,
            }

    if comment != None:
        context['page_comment'] = comment
    return render_to_string('page.html', context)



def render_comment(request, comment_post_id, comments = [], contexts = None):
    return render_to_string('comment.html', contexts)


def render_contents(posts, more = None):
    post_list = Post.objects.order_by('post_timestamp')

    
    context = {'post_list' : post_list,
                'more' : more}

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


def render_nator(page):
    context  = {'page' : page}
    return render_to_string('page_nator.html', context)


class MyPaginator(Paginator):
    def __init__(self, object_list, per_page, range_num = 5, orphans = 0, allow_empty_first_page = True):
        self.range_num = range_num
        Paginator.__init__(self, object_list, per_page, orphans, allow_empty_first_page)

    def page(self, number):
        self.page_number = number
        return super(MyPaginator, self).page(number)

    def _get_page_range_ext(self):
        page_range = super(MyPaginator, self).page_range
        start = long(self.page_number) -1 -self.range_num/2
        end = long(self.page_number) + self.range_num/2

        if(start <= 0):
            end = end -start
            start = 0
        ret = page_range[start : end]
        return ret
    page_range_ext = property(_get_page_range_ext)


