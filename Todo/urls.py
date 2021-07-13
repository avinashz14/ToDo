from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_todo_items, name = 'list_todo_items'),   
    path('list/<int:todo_id>/', views.details_todo_item, name = 'todo_item'),
    path('insert/', views.insert_todo_items, name = 'insert_todo_items'),
    path('delete/<int:todo_id>', views.delete_todo_items, name = 'delete_todo_items'),

]
