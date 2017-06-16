from django.conf.urls import url

from views import register
from views import login
from views import status


urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^login/$', login, name='login'),
    url(r'^status/$', status, name='status'),
]
