from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path(r'',views.todolist, name='todolist'),
    re_path(r'/add',views.todoadd, name='todoadd'),
    re_path(r'/todofinish',views.todofinish, name='finish'),
    re_path(r'/tododelete',views.tododelete, name='delete'),
    re_path(r'/todoback',views.todoback, name='back'),

]
