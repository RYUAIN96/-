# urls.py

from django.urls import path

from . import views

# 127.0.0.1:8000/member/index => index 함수 동작
urlpatterns = [
    path('index', views.index, name="index"),
    path('join', views.join, name="join"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('list', views.list, name="list"),
    path('edit', views.edit, name="edit"),
    path('delete', views.delete, name="delete"),

    path('join1', views.join1, name="join1"),

]
