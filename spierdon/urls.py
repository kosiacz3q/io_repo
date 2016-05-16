from django.conf.urls import url
from . import views

"""
URL patterns used by 'spierdon' app.
"""
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<challenge_id>[0-9]+)/complete$', views.complete_challenge, name='complete_challenge'),
    url(r'^addChallange/', views.addChallange, name='add_challange'),
    url(r'^ranking/', views.ranking, name='ranking'),
    url(r'^newChallenge/(?P<challenge_id>[0-9]+)/add', views.assign_challenge, name='assign_challenge'),
    url(r'^newChallenge/', views.newChallenge, name='new_challenge'),
]
