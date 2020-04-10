from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="todo"),
    path('Todo',views.operations,name="content"),
    path('add_todo',views.add_todo,name="add"),
    path('delete_todo/<int:todo_id>/',views.delete_todo,name="name")
]