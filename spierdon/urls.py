from django.conf.urls import url
from . import views

"""
URL patterns used by 'spierdon' app.
"""

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
