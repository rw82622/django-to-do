from django.shortcuts import render, redirect, reverse
from .models import Item

# Create your views here.
def index(request):
    items = Item.objects.all()
    return render(request, 'to_do_app/index.html', {'items': items})

def new_to_do(request):
    if request.method == 'GET':
        return render(request, 'to_do_app/new_item.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('description')
        item = Item(name=title, description=desc)
        item.save()
        data = {'item': item}
        return render(request, 'to_do_app/item_detail.html', data)
    
def details(request, id):
    current_item = Item.objects.get(id=id)
    return render(request, 'to_do_app/item_detail.html', {'item': current_item})

def edit(request, id):
    current_item = Item.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'to_do_app/edit_item.html', {'item': current_item})
    elif request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('description')
        current_item.name=title
        current_item.description=desc
        current_item.save()
        data = {'item': current_item}
        return render(request, 'to_do_app/item_detail.html', data)

def delete_item(request, id):
    current_item = Item.objects.get(id=id)
    current_item.delete()
    return redirect(reverse('home'))
