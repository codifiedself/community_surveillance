from django.urls import path, include
from .views import *
from django.conf.urls import url

from organizations.backends import invitation_backend

urlpatterns = [
    url(r'^accounts/', include('organizations.urls')),
    url(r'^select2/', include('django_select2.urls')),
    path('ngo/create/', ngo_create, name='ngo_create'),
    path('ngo/details/', ngo_details, name='ngo_details'),
    path('supplies_estimator', supplies_estimator, name='supplies_estimator'),

]

