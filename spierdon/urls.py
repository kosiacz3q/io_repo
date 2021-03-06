from django.conf.urls import url
from . import views

"""
URL patterns used by 'spierdon' app.
"""
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ranking/', views.ranking, name='ranking'),
    url(r'^challenge/(?P<challenge_id>[0-9]+)/complete$', views.complete_challenge, name='complete_challenge'),
    url(r'^challenge/(?P<challenge_id>[0-9]+)/join/', views.join_challenge, name='join_challenge'),
    url(r'^challenge/new/', views.add_challenge, name='add_challange'),
    url(r'^challenge/(?P<challenge_id>[0-9]+)/block/', views.block_challenge, name='block_challange'),
    url(r'^challenges/completed/', views.get_completed, name='get_completed'),
    url(r'^challenges/available/', views.get_challenges, name='get_challenges'),
]
