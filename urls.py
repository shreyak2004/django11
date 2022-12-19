from django.contrib import admin
from django.urls import path
from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('',views.index,name='index'),
    path('view_students', views.view_students, name='view_students'),
    path('view_faculty', views.view_faculty, name='view_faculty'),
    path('message', views.send_message, name='message'),
    path('reply', views.view_reply, name='reply'),
   
    path('addstudent', views.addstudent, name='addstudent'),
    path('register', views.registerc, name='register'),
   
    # path('remove_emp/<int:emp_id>', views.remove_emp, name='remove_emp'),

]
urlpatterns+=staticfiles_urlpatterns()