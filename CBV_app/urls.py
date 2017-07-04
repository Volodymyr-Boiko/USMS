from django.conf.urls import url

from .views import UserListView
from .views import UserDetailView


urlpatterns = [
    url(r'^users/$', UserListView.as_view(), name='users'),
    url(r'^user/(?P<pk>[0-9]+)/$', UserDetailView.as_view(), name='user'),
]
