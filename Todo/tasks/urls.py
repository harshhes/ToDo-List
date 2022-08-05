from django.urls import path
from .views import *

urlpatterns =[
    path('', index, name='list'),
    path('update_task/<int:pk>/', updateTask, name='update_task'),
    path('delete/<int:pk>/', deleteTask, name='delete')

]