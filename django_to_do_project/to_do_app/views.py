from django.shortcuts import render
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
        data = {'items': Item.objects.all(), 'myKey': item.id}
        return render(request, 'to_do_app/item_detail.html', data)

