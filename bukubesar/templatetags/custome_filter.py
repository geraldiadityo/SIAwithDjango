from django import template
from jurnal.models import Jurnal
register = template.Library()

@register.inclusion_tag('bukubesar/datajurnal.html')
def loadFromTglAkun(tgl=None,akun=None):
    if tgl == None or akun == None:
        data_list = {}
    else:

        data_list = Jurnal.objects.filter(akun=akun).filter(tgl=tgl)
    return {'datalist':data_list}

