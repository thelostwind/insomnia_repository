from django.contrib import admin

from .models import User, Post, Navigation,Category,Comments

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Navigation)
admin.site.register(Category)
admin.site.register(Comments)
