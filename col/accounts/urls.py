from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.home, name='home'),
    path('classes/', views.classes, name='classes'),
    path('class1/', views.class1, name='class1'),
    path('class1vn/', views.class1vn, name='class1vn'),

    path('', views.index, name = 'index'),
    path('signin/', views.signin, name = 'signin'),
    path('signup/', views.signup, name = 'signup'),
    path('aboutus/', views.aboutus, name = 'aboutus'),

    path('matlab/', views.matlab, name = 'matlab'),
    path('programming/', views.prog_ide, name = 'prog_ide'),
    path('notifications/', views.notif, name = 'notif'),
]
