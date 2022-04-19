from django.urls import path, re_path

from .views import (
    managePengguna,
    viewPengguna,
    register,
    loginView,
    logoutView,
    deletePengguna,
)

app_name = 'pengguna'
urlpatterns = [
    re_path(r'^delete-pengguna/(?P<pk>\d+)/$',deletePengguna,name='delete'),
    path('logout-pengguna/',logoutView,name='logout'),
    path('login-pengguna/',loginView,name='login'),
    path('create-pengguna/',register,name='create'),
    path('',managePengguna,name='manage'),
]