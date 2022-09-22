from django.contrib import admin

from .models import Listing, Bid, Comment, User ,Bider

# Register your models here.

admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Bid)
admin.site.register(Bider)
admin.site.register(Comment)

