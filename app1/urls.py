from django.urls import path
from app1 import views

app_name = 'app1'

urlpatterns = [ 
    path('course',views.courseinfo,name='course'),
    path('course/<int:id>',views.courseinfo,name='courseinfo')
]