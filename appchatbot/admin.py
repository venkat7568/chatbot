from django.contrib import admin

from .models import message,friend,img,bio

admin.site.register(message)
admin.site.register(friend)
admin.site.register(img)
admin.site.register(bio)
