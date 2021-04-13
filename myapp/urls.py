from django.contrib import admin
from django.urls import path
from myapp import views
app_name='myapp'

urlpatterns = [
    path('',views.view1,name='view1'),
    path('view2/<email>',views.view2,name='view2'),
    path('views3/<name>',views.view3,name='view3'),
]
