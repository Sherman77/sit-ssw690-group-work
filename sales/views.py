from django.shortcuts import render, get_object_or_404
from .models import SaleItem
# Create your views here.
def saleslist(request):
    items = SaleItem.objects
    return render(request, 'sales/sales.html', {'items':items})

def item_detail(request, item_id):
    item = get_object_or_404(SaleItem, pk = item_id)
    return render(request, 'sales/item_detail.html', {'item':item})
