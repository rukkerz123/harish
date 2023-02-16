from django.urls import path
from . import views

urlpatterns = [
    path('', views.add, name='add'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbhome/', views.TaskListview.as_view(), name='cbhome'),
    path('cbdetail/<int:pk>/', views.TaskDetailview.as_view(), name='cbdetail'),
    path('cbupdate/<int:pk>/', views.TaskUpdateview.as_view(), name='cbupdate'),
    path('cbdelete/<int:pk>/', views.TaskDeleteview.as_view(), name='cbdelete'),
]
