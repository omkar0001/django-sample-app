from django.contrib import admin
from polls.models import Poll
from polls.models import Choice

class ChoiceInline(admin.StackedInline):
	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ['question', 'pub_date', 'was_published_recently']
    search_fields = ['question']
admin.site.register(Choice)
admin.site.register(Poll, PollAdmin)
# Register your models here.
    
