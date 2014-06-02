from django.conf.urls import patterns, url
from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter

from custom_rest import views


router = DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.

urlpatterns = patterns('',
	url(r'^news/?$',views.news_rest_list),
)
