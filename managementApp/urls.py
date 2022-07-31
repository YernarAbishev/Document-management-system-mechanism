from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-query/', views.addQuery, name='addQuery'),
    path('students/list/', views.studentsList, name='studentsList'),
    path('documents/list/', views.documentsList, name='documentsList'),
    path('documents/detail/<int:pk>/', views.documentDetail, name='documentDetail'),
]