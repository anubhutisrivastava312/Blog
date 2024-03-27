
from django.urls import path,include
from .import views

urlpatterns = [
    path("", views.home, name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('signup/',views.signup,name="signup"),
    path("user_login/",views.user_login ,name="user_login"),
    path("user_logout/",views.user_logout,name="user_logout"),
    path("addpost/",views.add_post,name="addpost"),
    path("updatepost/<int:id>/",views.update_post,name="updatepost"),
    path("delete/<int:id>/",views.delete_post,name="deletepost"),
]