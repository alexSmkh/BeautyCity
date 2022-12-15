from django.urls import path
from beauty.views import index, service, service_finally, notes

app_name = 'beauty'

urlpatterns = [
    path('', index, name='index'),
    path('service', service, name='service'),
    path('service_finally', service_finally, name='service_finally'),
    path('notes', notes, name='notes')
]
