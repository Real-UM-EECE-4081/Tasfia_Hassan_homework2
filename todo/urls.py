from django.urls import path
from .views import TaskList, TaskDetail,  TaskCreate, TaskUpdate, TaskDelete, CustomLoginView

urlpatterns = [
    path('', TaskList.as_view(), name='task'),
    path('task/<int:pk>/', TaskDetail.as_view(), name="tasks-detail"),
    path('task-create/', TaskCreate.as_view(), name="task-create"),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('task/<int:pk>/', TaskDetail.as_view(), name="tasks-detail"),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name="tasks-update"),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name="tasks-delete")
]