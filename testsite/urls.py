from django.urls import path
from . import views

urlpatterns = [
    path('',views.testsitepost_list,name='testsitepost_list')
]
