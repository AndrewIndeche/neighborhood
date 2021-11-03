from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.conf.urls import url,include

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^all-hoods/$', views.hoods, name='hood'),
    url(r'^new-hood/$', views.create_hood, name='new-hood'),
    url(r'^profile/(\d+)/$', views.profile, name='profile'),
    url(r'^profile/(\d+)/edit/$', views.edit_profile, name='edit-profile'),
    url(r'join_hood/(\d+)/', views.join_hood, name='join-hood'),
    url(r'leave_hood/(\d+)/', views.leave_hood, name='leave-hood'),
    url(r'^single_hood/(\d+)/$', views.single_hood, name='single-hood'),
    url(r'(\d+)//new-post', views.create_post, name='post'),
    path('<hood_id>/members', views.hood_members, name='members'),
    url('search/', views.search_business, name='search'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
