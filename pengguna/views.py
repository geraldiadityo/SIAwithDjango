from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Pengguna

from .decorators import (
    allowed_user,
    unauthenticated_user,
)

from .forms import (
    CreateUserForm,
    PenggunaForm,
)
# Create your views here.
@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['admin'])
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return HttpResponse(
                '<script>alert("success register for username '+str(username)+' !");window.location="'+str(reverse_lazy('pengguna:manage'))+'";</script>'
            )
    
    context = {
        'form':form,
        'page_title':'Pengguna Manage',
    }
    return render(request, 'pengguna/pengguna_create.html',context)

@unauthenticated_user
def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse(
                '<script>alert("combination password and username is wrong, try again");window.location="'+str(reverse_lazy('pengguna:login'))+'";</script>'
            )
    
    context = {}
    return render(request, 'pengguna/login.html',context)

@login_required(login_url='pengguna:login')
def logoutView(request):
    logout(request)
    return redirect('pengguna:login')

@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['admin'])
def managePengguna(request):
    penggunalist = Pengguna.objects.all().order_by('-date_created')
    context = {
        'page_title':'User Management',
        'penggunalist':penggunalist,
    }
    return render(request, 'pengguna/pengguna_manage.html',context)


@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['admin'])
def viewPengguna(request, pk):
    data = dict()
    pengguna = Pengguna.objects.get(id=pk)
    context = {
        'pengguna':pengguna,
    }
    data['html_form'] = render_to_string('pengguna/view_pengguna.html',context)
    return JsonResponse(data)

@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['admin'])
def deletePengguna(request, pk):
    data = dict()
    pengguna = Pengguna.objects.get(id=pk)
    if request.method == 'POST':
        pengguna.delete()
        data['form_is_valid'] = True
        penggunalist = Pengguna.objects.all().order_by('-date_created')
        data['html_pengguna_list'] = render_to_string('pengguna/pengguna_manage_list.html',{'pengguna:list'},request=request)
    else:
        context = {
            'pengguna':pengguna,
        }
        data['html_form'] = render_to_string('pengguna/partpenggunadelete.html',context,request=request)
    
    return JsonResponse(data)
