from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
# Create your views here.

from akun.models import Akun
from jurnal.models import Jurnal

def homeView(request):
    akun_list = Akun.objects.all()
    context = {
        'akun_list':akun_list,
        'page_title':'Buku Besar'
    }
    return render(request, 'bukubesar/home_bukubesar.html',context)

def get_by_akun(request):
    data = dict()
    if request.is_ajax and request.method == 'GET':
        akun = request.GET.get('akun_id')
        nama = request.GET.get('nama')
        data_transaksi = Jurnal.objects.filter(akun_id=akun).order_by('tgl')
        tgl_list = data_transaksi.values_list('tgl',flat=True).order_by('tgl').distinct()
        total_debet = 0
        total_kredit = 0
        for i in data_transaksi:
            if i.tipe == 'Debet':
                total_debet += i.nominal
            else:
                total_kredit += i.nominal
        
        saldo_debet = total_debet - total_kredit
        context_data = {
            'databytgl':tgl_list,
            'akun':akun,
            'saldo_debet':saldo_debet,
        }
        data['nama_akun'] = nama
        data['html_buku_akun_list'] = render_to_string('bukubesar/data_table.html',context_data,request=request)
        return JsonResponse(data)
    return JsonResponse({},status=400)
