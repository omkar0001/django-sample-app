
"""
All forms related to the apps
"""
"""
Upload form
"""
from django import forms
from taggit.forms import *
#from autocomplete_light.contrib.taggit_field import TaggitField, TaggitWidget



class UploadFileForm(forms.Form):
	title = forms.CharField(max_length=50)
	file  = forms.FileField()
	#tags = TaggitField(widget=TaggitWidget('TagAutocomplete'))
	def is_valid():
		return true