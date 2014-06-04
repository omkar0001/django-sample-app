import datetime
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from cms.models import CMSPlugin
from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool

from django.contrib import admin
from cms.extensions import PageExtensionAdmin

from cms.models.pluginmodel import CMSPlugin

from django.db import models
# Create your models here.
class News(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(max_length=200)
	videoUrl = models.URLField()
	image = models.ImageField(upload_to="icons")

class NewsPluginModel(CMSPlugin):
	news = models.ForeignKey('news.News', related_name='news')



class NewsContent(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(max_length=200)
	videoUrl = models.URLField()
	image = models.ImageField(upload_to="icons")
	def __unicode__(self):
		return self.title

class NewsContentPluginModel(CMSPlugin):
	news = models.ForeignKey('news.NewsContent', related_name='news')