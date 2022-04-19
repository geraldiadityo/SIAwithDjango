from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='pengguna:login')
def index(request):
    context = {}
    return render(request, 'dashboard.html',context)