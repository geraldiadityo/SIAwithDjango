from django.shortcuts import render
from django.template.loader import render_to_string

from jurnal.models import Jurnal
from akun.models import Akun
# Create your views here.

def viewNeracaSaldo(request):
    data_akun = Akun.objects.all()
    data_jurnal = Jurnal.objects.all()
    total_saldo_debet = 0
    total_saldo_kredit = 0
    for i in data_akun:
        data_transaksi = data_jurnal.filter(akun_id=i.id)
        res_debet = 0
        res_kredit = 0
        for x in data_transaksi:
            if x.tipe == 'Debet':
                res_debet += x.nominal
            else:
                res_kredit += x.nominal
        res = abs(res_debet - res_kredit)
        if i.kategori == 'Debit':
            total_saldo_debet += res
        else:
            total_saldo_kredit += res
    context = {
        'akun':data_akun,
        'page_title':'Neraca Saldo',
        'total_saldo_debet':total_saldo_debet,
        'total_saldo_kredit':total_saldo_kredit,
    }
    return render(request, 'neracasaldo/neraca_saldo_view.html',context)

