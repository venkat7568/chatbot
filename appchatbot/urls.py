from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('regst', views.regst, name="regst"),
    path('home', views.home, name="home"),
   path('inhome', views.inhome, name="inhome"),
   path('onhome', views.onhome, name="onhome"),
   path('prof', views.prof, name="prof"),
  path('loginpage', views.loginpage, name="loginpage"),
  path('vf_login', views.vf_login, name="vf_login"),
  path("requsted_P", views.requ, name="requ"),
  path("search_code", views.search_code, name="search_code"),
  path("request_button", views.request_button, name="request_button"),
  path("accept", views.accept, name="accept"),
  path("imgupload", views.imgupload, name="imgupload"),
  path("back", views.back_fun, name="back_fun"),
  path("logout", views.logout, name="logout"),
  path("bioon", views.bioon, name="bioon"),
  path("bioinput", views.bioinput, name="bioinput"),
]
