from django.urls import path,re_path
from .views import (
    manageAkun,
    createAkun,
    editAkun,
    deleteAkun,
    viewAkun,
)
app_name = 'akun'

urlpatterns = [
    re_path(r'^view-akun/(?P<pk>\d+)/$',viewAkun,name='view-akun'),
    re_path(r'^delete-akun/(?P<pk>\d+)/$',deleteAkun,name='delete'),
    re_path(r'^edit-akun/(?P<pk>\d+)/$',editAkun,name='edit'),
    path('create-akun/',createAkun,name='create'),
    path('',manageAkun,name='manage'),
]
