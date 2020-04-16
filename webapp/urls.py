from django.urls import path, include
from .views import *
from django.conf.urls import url

from organizations.backends import invitation_backend

urlpatterns = [
    url(r'^accounts/', include('organizations.urls')),
    url(r'^select2/', include('django_select2.urls')),

    path('ngo/create/', ngo_create, name='ngo_create'),
    path('covid19-ngo-collaboration-form', select_language_for_form, name='select_language_for_form'),


    path('ngo/details/', ngo_details, name='ngo_details'),
    path('ngo_district_list_and_form/', ngo_district_list_and_form, name='ngo_district_list_and_form'),

    # path('select_language_for_form/', select_language_for_form, name='select_language_for_form'),


    
    # path('supplies_estimator', supplies_estimator, name='supplies_estimator'),
    path('', index, name='index'),

]

