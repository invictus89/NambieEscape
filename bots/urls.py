from django.urls import path
from . import views

app_name = 'bots'
urlpatterns = [
    path('telegram/<token>/', views.telegram, name='telegram'),
    path('<token>/', views.telegram, name='telegram'),
]
