from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
# Create your views here.
from .models import Akun
from .forms import AkunForm

def manageAkun(request):
    akunlist = Akun.objects.all()
    context = {
        'akunlist':akunlist,
        'page_title':'Akun Manage',
    }
    return render(request, 'akun/manage_akun.html',context)

def akun_save_form(request,form,template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            akunlist = Akun.objects.all()
            data['html_akun_list'] = render_to_string('akun/manage_akun_list.html',{'akunlist':akunlist})
        else:
            data['form_is_valid'] = False
    
    context = {
        'form':form,
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def createAkun(request):
    if request.method == 'POST':
        form = AkunForm(request.POST)
    else:
        form = AkunForm()
    
    return akun_save_form(request, form, 'akun/partakuncreate.html')

def editAkun(request,pk):
    akun = Akun.objects.get(id=pk)
    if request.method == 'POST':
        form = AkunForm(request.POST, instance=akun)
    else:
        form = AkunForm(instance=akun)
    
    return akun_save_form(request, form, 'akun/partakunupdate.html')


def deleteAkun(request,pk):
    data = dict()
    akun = Akun.objects.get(id=pk)
    if request.method == 'POST':
        akun.delete()
        data['form_is_valid'] = True
        akunlist = Akun.objects.all()
        data['html_akun_list'] = render_to_string('akun/manage_akun.html',{'akunlist':akunlist},request=request)
    else:
        context = {
            'akun':akun,
        }
        data['html_form'] = render_to_string('akun/partakundelete.html',context,request=request)
    
    return JsonResponse(data)

def viewAkun(request,pk):
    data = dict()
    akun = Akun.objects.get(id=pk)
    context = {
        'akun':akun,
    }
    data['html_form'] = render_to_string('akun/viewAkun.html',context, request=request)
    return JsonResponse(data)


