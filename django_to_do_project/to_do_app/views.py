from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Item, TheUser


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('home')
    elif request.method == 'GET':
        return render(request, 'to_do_app/sign_up.html')
    elif request.method == 'POST':
        try:
            body = request.POST
            firstName = body['firstName']
            lastName = body['lastName']
            user_email = body['email']
            userName = body['userName']
            user_password = body['password']
            TheUser.objects.create_user(
                username=userName,
                password=user_password,
                email = user_email,
                first_name=firstName,
                last_name=lastName)
            return redirect('home')
        except:
            return render(request, 'to_do_app/sign_up.html', {'msg': "Username already exists"})

@login_required(login_url='log_in')        
def index(request):
    items = Item.objects.filter(user_id=request.user.id)
    return render(request, 'to_do_app/index.html', {'items': items, 'user': request.user})

def log_in(request):
    if request.user.is_authenticated:
        return redirect('home')
    elif request.method == 'GET':
        return render(request, 'to_do_app/log_in.html')
    elif request.method == 'POST':
        username = request.POST.get('userName')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'to_do_app/log_in.html', {'msg': "Username or Password is Incorrect"})

@login_required(login_url='log_in') 
def log_out(request):
    logout(request)
    return redirect('log_in')

@login_required(login_url='log_in') 
def new_to_do(request):
    if request.method == 'GET':
        return render(request, 'to_do_app/new_item.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('description')
        item = Item(name=title, description=desc, user_id=request.user.id)
        item.save()
        data = {'item': item}
        return render(request, 'to_do_app/item_detail.html', data)
    
@login_required(login_url='log_in')     
def details(request, id):
    current_item = Item.objects.get(id=id)
    return render(request, 'to_do_app/item_detail.html', {'item': current_item})

@login_required(login_url='log_in') 
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

@login_required(login_url='log_in') 
def delete_item(request, id):
    current_item = Item.objects.get(id=id)
    current_item.delete()
    return redirect('home')
