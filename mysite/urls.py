#import autocomplete_light
#autocomplete_light.autodiscover()

from django.conf.urls import patterns, include, url

from django.contrib import admin

from django.conf.urls import patterns, url, include
from rest_framework import routers
from polls import views
from custom_rest import views as views_rest


from django.conf.urls import *
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf import settings

admin.autodiscover()
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'news', views_rest.NewsViewSet)


#Django cms urls.

urlpatterns = i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)

urlpatterns = i18n_patterns('',
	url(r'^polls1/', include('polls.urls')),
) + urlpatterns


urlpatterns = patterns('',
	url(r'^', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
) + urlpatterns


urlpatterns = patterns('',
    # [...] your url patterns are here
	url(r'', include('custom_rest.urls')),
) + urlpatterns

urlpatterns = patterns('',
	url(r'^docs/', include('rest_framework_swagger.urls')),
) + urlpatterns

#urlpatterns = patterns('',
    # [...] your url patterns are here
#	url(r'^autocomplete/', include('autocomplete_light.urls')),
#) + urlpatterns

if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns