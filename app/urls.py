from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddTaskView.as_view(), name='add_task'),
    path('show_task/', views.show_task, name='show_task'),
    path('update_task/<int:pk>', views.UpdateTaskView.as_view(), name='update_task'),
    path('delete_task/<int:pk>', views.DeleteTaskView.as_view(), name='delete_task'),
    path('task_complete/', views.CompleteTaskView.as_view(), name='complete_task'),
    path('<int:id>', views.is_complete_task, name='make_complete_task'),
]