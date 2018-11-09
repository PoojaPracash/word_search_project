from django.conf.urls import url
from searchengine import views


urlpatterns = [
    url(r'', views.submit),
    url(r'^search/$', views.search)
]
