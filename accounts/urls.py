from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('per-edit/', views.per_edit, name='per_edit'),
    path('<int:category_pk>/edit-cate/', views.edit_cate, name='edit_cate'),
]
