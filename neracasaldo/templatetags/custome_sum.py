from django import template
from jurnal.models import Jurnal

register = template.Library()

@register.inclusion_tag('neracasaldo/data_debet_kredit.html')
def findTheSum(akun):
    data = Jurnal.objects.filter(akun_id=akun)
    res_debet = 0
    res_kredit = 0
    for i in data:
        if i.tipe == 'Debet':
            res_debet += i.nominal
        else:
            res_kredit += i.nominal
    
    res = res_debet - res_kredit
    
    return {'result':abs(res)}

