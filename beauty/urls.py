from django.urls import path
from beauty.views import index, service

app_name = 'beauty'

urlpatterns = [
    path('', index, name='index'),
    path('service', service, name='service')
]
