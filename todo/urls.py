from django.urls import path
from .views import listTodo, createTodo, updateTodo, deleteTodo

urlpatterns = [
    path('', listTodo, name='home'),
    path('create/', createTodo, name='create'),
    path('update/<str:pk>/', updateTodo, name='update'),
    path('delete/<str:pk>/', deleteTodo, name='delete'),
]
