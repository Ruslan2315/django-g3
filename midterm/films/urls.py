from django.urls import path
from films import views

urlpatterns = [
    path('api/films', views.employees_handler),
    path('api/films/<int:pk>', views.employee_handler),
]