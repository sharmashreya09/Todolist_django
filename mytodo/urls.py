from django.urls import path
from mytodo import views

urlpatterns = [
    path("", views.index, name="TodoHome"),
    path('addTodo/' , views.addTodo , name="addtodo"),
    path('deleteTodo/<str:title>/', views.deleteTodo,name="deleteTodo"),

]
