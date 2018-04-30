from django.urls import path
from django.conf.urls import url
from . import views

# URL namespaces allow you to uniquely reverse named URL patterns even if different applications use the same URL names.
# app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$',views.IndexView.as_view(), name ='index'),
    # path('', views.index, name='index'),

    url(r'^register/$',views.UserFormView.as_view(), name ='register'),

    # /music/<album_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view() , name='detail'),

    # /music/album/add
    url(r'album/add/$', views.AlbumCreate.as_view() , name='album-add'),

    # /music/album/2
    url(r'album/(?P<pk>[0-9]+)/$', views.UpdateView.as_view() , name='album-update'),

    # /music/album/2/delete
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.DeleteView.as_view() , name='album-delete')
    ]



# changing for generic views
# urlpatterns = [
#     # /music/
#     url(r'^$',views.index,name ='index'),
#     # path('', views.index, name='index'),
#
#     # /music/<album_id>/
#     url(r'^(?P<album_id>[0-9a-z]+)/$', views.detail, name='detail'),
#
#     # /music/<album_id>/favorite
#     url(r'^(?P<album_id>[0-9a-z]+)/favorite$', views.favorite, name='favorite'),
#
# ]