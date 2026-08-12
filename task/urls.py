from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.create_task, name='create_task'),
    path('my-tasks/', views.my_tasks, name='my_tasks'),
    path('view-task/<int:id>/', views.view_task, name='view_task'),
    path('update-task/<int:id>/', views.update_task, name='update_task'),
    path("my-tasks/",views.my_tasks,name="my_tasks"),
    path("delete-task/<int:id>/", views.delete_task, name="delete_task"),

]