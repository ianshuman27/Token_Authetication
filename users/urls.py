from django.contrib import admin
from django.urls import path
from users.views import signin, user_info


urlpatterns = [
    path('api/v1/signin', signin),
    path('api/v1/user_info', user_info),
]
