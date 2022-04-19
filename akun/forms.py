from django import forms
from django.forms import TextInput,Select

from .models import Akun

class AkunForm(forms.ModelForm):
    class Meta:
        model = Akun
        fields = [
            'nama_akun',
            'kode_akun',
            'kategori',
        ]
        
        labels = {
            'nama_akun':'Nama Akun',
            'kode_akun':'Nomor / Kode Akun',
            'kategori':'Posisi Awal Akun',
        }

        widgets = {
            'nama_akun':TextInput,
            'kode_akun':TextInput,
            'kategori':Select,
        }

