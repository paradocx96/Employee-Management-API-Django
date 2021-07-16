from django.urls import path
from . import views

urlpatterns = [
    path('get', views.employee_list, name="employees"),
    path('details/<str:pk>/', views.employee_by_id, name="employee"),
    path('create', views.employee_create, name="create"),
    path('update/<str:pk>/', views.employee_update, name="update"),
    path('delete/<str:pk>/', views.employee_delete, name="delete"),
]
