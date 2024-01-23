from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Category
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Q

def items(request):
    query = request.GET.get('query', '')
    categories = Category.objects.all()
    items = Item.objects.all()
    category_id = request.GET.get('category', 0)

    if category_id:
        items= items.filter(category_id = category_id)
    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'item/items.html', {
        'items' : items,
        'query' : query,
        'categories' : categories,
        'category_id' : int(category_id),
    })


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_rent=False).exclude(pk=pk)[0:3]


    return render(request, 'item/detail.html', {
        'item' : item,
        'related_items': related_items
    })


@login_required
def rent_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if not item.is_rent:
        item.rented_by = request.user
        item.is_rent = True
        item.rented_at = timezone.now()
        item.save()
    return redirect('core:rented_items')