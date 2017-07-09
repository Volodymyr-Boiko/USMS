from django.conf.urls import url

from .views import UserListView
from .views import UserDetailView
from .views import CreateUser


urlpatterns = [
    url(r'^User/$', UserListView.as_view(), name='User'),
    url(r'^user/(?P<pk>[0-9]+)/$', UserDetailView.as_view(), name='user'),
    url(r'^create_user/$', CreateUser.as_view(), name='create_user'),
]
