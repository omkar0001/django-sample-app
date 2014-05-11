from django.conf.urls import patterns, url

from polls import views




# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.

urlpatterns = patterns('',
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
	url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
	url(r'^ws/$',views.poll_rest_list),
	url(r'^upload_form/$',views.upload_file),
	url(r'^list_images/$', views.list_images),
	url(r'^search_images/$',views.search_images)

)

#urlpatterns = patterns('',
#	url(r'^', include(router.urls)),
#	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))