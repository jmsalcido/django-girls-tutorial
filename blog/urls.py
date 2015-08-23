from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name="post_list"),
    url(r'^post/(?P<post_id>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<post_id>[0-9]+)/delete/$', views.post_delete, name='post_delete'),
    url(r'^post/(?P<post_id>[0-9]+)/edit/$', views.post_add_edit, name='post_edit'),
    url(r'^post/new/$', views.post_add_edit, name='post_new')
]
