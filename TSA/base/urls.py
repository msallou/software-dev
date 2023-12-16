from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name="login"),
    path('register/', views.registerUser, name="register"),
    path('edit-profile/', views.editUser, name="edit-profile"),
    path('logout/', views.logoutUser, name="logout"),
    path('home/', views.home, name="home"),
    path('kindergarten/', views.kindergarten, name="kindergarten"),
    path('grade1/', views.grade1, name="grade1"),

    path('grade2/', views.grade2, name="grade2"),
    
    path('grade3/', views.grade3, name="grade3"),
    path('grade3/intro-to-multiplication', views.introMultiplication, name="introMultiplication"),
    
    path('grade4/', views.grade4, name="grade4"),
    
    path('grade5/', views.grade5, name="grade5"),
    
    path('grade6/', views.grade6, name="grade6"),
    
    path('grade7/', views.grade7, name="grade7"),
    
    path('grade8/', views.grade8, name="grade8"),
    
    path('settings/', views.settings, name="settings"),

]
