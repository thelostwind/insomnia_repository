from django.conf.urls import *

from . import views

#urlpatterns = [
    #url(r'^$', views.blog, name='blog'), 
#    url(r'^$', 'blog'),   
#]


urlpatterns = patterns('blog.views',
        url(r'^$', 'blog'),
        )
