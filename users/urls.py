from django.conf.urls import url

from . import views

app_name = 'users'
urlpatterns = [
    url(r'^profile/$', views.UserProfileView.as_view(), name='profile'),
]