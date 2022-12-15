from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('users/request_code', views.request_code),
    path('users/confirm_registration', views.confirm_registration),
]
