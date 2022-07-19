from django.urls import path
from . import views
# import hashlib

urlpatterns = [
    path('', views.form, name='form'),
]