from django.urls import path
from . import views

app_name = 'bots'
urlpatterns = [
    path('<token>/telegram/', views.telegram, name='telegram'),
]