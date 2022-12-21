from django.urls import path
from beauty.views import get_available_time, index, service, service_finally, notes, create_appointment
from beauty.views import get_masters, index, get_categories, service, service_finally, notes

app_name = 'beauty'

urlpatterns = [
    path('', index, name='index'),
    path('service', service, name='service'),
    path('service_finally', service_finally, name='service_finally'),
    path('notes', notes, name='notes'),
    path('api/categories', get_categories),
    path('api/masters', get_masters),
    path('api/get_available_time', get_available_time),
    path('notes', notes, name='notes'),
    path('create_appointment', create_appointment, name='create_appointment')
]
