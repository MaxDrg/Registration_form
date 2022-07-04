from django.urls import path
from . import views
# import hashlib

urlpatterns = [
    path('', views.form, name='form'),
    #path('thank', views.thank, name='thank')
    #path(hashlib.sha256('buckets'.encode('utf8')).hexdigest(), views.buckets, name='buckets')
]