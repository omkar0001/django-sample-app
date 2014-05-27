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

class Hello(CMSPlugin):
    guest_name = models.CharField(max_length=50, default='Guest')





class IconExtension(PageExtension):
    image = models.ImageField(upload_to='icons')

extension_pool.register(IconExtension)




# existing Poll and Choice models...

class PollPluginModel(CMSPlugin):
    poll = models.ForeignKey('polls.Poll', related_name='plugins')

    def __unicode__(self):
      return self.poll.question
#Image model
class ImageModel(models.Model):
    imageField = models.FileField(upload_to="images")
    #Taggit manager
    tags = TaggableManager()

"""
Ignore the below Models
"""    
# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
    	return self.question
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)	

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
    	return self.choice_text