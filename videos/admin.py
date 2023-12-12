from django.contrib import admin
from .models import Video, Keyword, Categories, VideoOTD
# Register your models here.
admin.site.register(Video)
admin.site.register(Keyword)
admin.site.register(Categories)
admin.site.register(VideoOTD)