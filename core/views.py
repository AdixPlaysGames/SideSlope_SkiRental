from django.shortcuts import render, redirect
from item.models import Category, Item, ItemDetail
from .forms import SignupForm

from django.contrib.auth.decorators import login_required
from datetime import timedelta
from django.utils import timezone

from django.http import HttpResponse
from django.core import serializers


def index(request):
    items = Item.objects.all()[0:10]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories' : categories,
        'items' : items,
    })

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')
    
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })


@login_required
def rented_items(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        item = Item.objects.get(id=item_id)
        item.rented_by = None
        item.is_rent = False
        item.rented_at = None
        item.save()

    items = Item.objects.filter(rented_by=request.user)
    for item in items:
        item.time_left = timedelta(hours=24) - (timezone.now() - item.rented_at)

    return render(request, 'core/rented_items.html', {'items': items})

"""def pricing(request):
    items = Item.objects.all()
    xml = serializers.serialize('xml', items)
    return HttpResponse(xml, content_type='application/xml')"""

def pricing(request):
    items = Item.objects.all()
    if request.GET.get('format') == 'xml':
        details = ItemDetail.objects.filter(item__in=items)
        xml = serializers.serialize('xml', details)
        return HttpResponse(xml, content_type='application/xml')
    else:
        return render(request, 'core/pricing.html', {'items': items})