from django.contrib import admin

from .models import User, Post, Navigation

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Navigation)
