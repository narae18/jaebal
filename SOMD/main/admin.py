from django.contrib import admin
from .models import Post,Comment,Tag,SOMD,Member,JoinRequest,Images
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(SOMD)
admin.site.register(Member)
admin.site.register(JoinRequest)
admin.site.register(Images)
