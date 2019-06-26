from django.urls import path
from django.conf.urls import url
from . import views

# app_name = 'cal'
# urlpatterns = [
#      path('', views.CalendarView.as_view(), name='calendar'),
#      path('new/', views.event, name='event_new'),
#      path('edit/<int:event_id>/', views.event, name='event_edit'),
# ]

app_name = 'calendar'
urlpatterns = [
     path('', views.my_calendar, name='calendar'),
     path('<month>/', views.my_calendar, name='calendar'),    
     path('create/<year>/<month>/<day>/', views.create, name='create'),
     path('edit/<int:event_id>/', views.edit, name='edit'),
     path('detail/<year>/<month>/<day>/', views.detail, name='detail'),
     path('delete/<int:content_id>/', views.delete, name='delete'),
]