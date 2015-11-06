from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('blog.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
