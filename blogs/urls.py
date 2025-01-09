from django.urls import path
from .import views

urlpatterns=[
    path('',views.landing,name='landing'),
    path('signup',views.sign_up,name='signup'),
    path('login',views.log_in,name='login'),
    path('explore',views.explore,name='explore'),
    path('post/<int:id>/',views.post,name='post'),
    path('logout',views.log_out,name="logout"),
    path('write',views.write,name='write'),
    ]