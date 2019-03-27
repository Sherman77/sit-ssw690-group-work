from django.shortcuts import render, get_object_or_404
from .models import People

# Create your views here.
def portfolio(request):
    people = People.objects
    return render(request, 'portfolio/portfolio_page.html', {'people':people})

def people_detail(request, people_id):
    people = get_object_or_404(People, pk = people_id)
    return render(request, 'portfolio/portfolio_page.html', {'people':people})
