from django.contrib import admin
from news.models import News
from news.models import NewsContent

class NewsPageAdmin(admin.ModelAdmin):
	fields = ('title', 'description', 'videoUrl', 'image')

admin.site.register(News, NewsPageAdmin)

class NewsContentPageAdmin(admin.ModelAdmin):
	fields = ('title', 'description', 'videoUrl', 'image')

admin.site.register(NewsContent, NewsContentPageAdmin)

# Register your models here.
