from .models import OrderDetail
from django.db.models import Sum

def grand_total():

    total = OrderDetail.objects.filter(status=0).aggregate(Sum('total'))['total__sum']
    if total==None:
        return 0
    return  total