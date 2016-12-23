from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^ajax_func/$', views.ajax_func, name='ajax_func'),

    url(r'^delete_func/$', views.delete_func, name='delete_func'),

    url(r'^update_func/$', views.update_func, name='update_func'),

    url(r'^url_page/$', views.url_page, name='url_page'),
	
    url(r'^detail/$', views.detail,name='detail'),

    url(r'^database/$', views.database,name='database'),
    
    url(r'^(?P<sampletable_id>[0-9]+)/$', views.detail,name='detail'),

    url(r'^(?P<sampletable_id>[0-9]+)/results/$' , views.results, name = 'results'),

    url(r'^(?P<sampletable_id>[0-9]+)/vote/$', views.vote, name = 'vote'),
    ]
