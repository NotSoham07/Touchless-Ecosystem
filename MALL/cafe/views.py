from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Feedback, Product, Joinus, Orders
from math import *
import datetime

def home(request):
    return render(request, 'home.html')

def feedback(request):
    if request.method=='POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        feedback = request.POST.get('subject','')
        data = Feedback(name=name, email = email, feedback=feedback )
        data.save()
    return render(request, 'feedback.html')

def menu(request):
    #products = Product.objects.all()
    #n = len(products)

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds':allProds}
    return render(request, 'menu.html', params)

def joinus(request):
    if request.method=='POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone', '')
        location = request.POST.get('location', '')
        file = request.POST.get('file', '')
        subject = request.POST.get('subject','')
        data = Joinus(name=name, email = email, phone=phone, location=location, file= file ,subject=subject )
        data.save()
    return render(request, 'joinus.html')

def tray(request):
    if request.method=="POST":
        items_json= request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        # address=request.POST.get('address', '')
        # city=request.POST.get('city', '')
        # state=request.POST.get('state', '')
        # zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')

        order = Orders(items_json= items_json, name=name, email=email)
        order.save()
        thank=True
        id=order.order_id
        return render(request, 'tray.html', {'thank':thank, 'id':id})
    return render(request, 'tray.html')

def about(request):
    return render(request, 'about.html')

def status(request):
    from django.utils import timezone
    now = timezone.now()
    today_orders = Orders.objects.filter(created_at = now.date())
    orders = Orders.objects.all()
    for i in orders:
        if i.order_status == "Ordered":
            # if last modified is greater than 3 minutes
            if i.last_modified + datetime.timedelta(seconds=7) < now:
                i.order_status = "Preparing"
                i.save()
        elif i.order_status == "Preparing":
            if i.last_modified + datetime.timedelta(seconds=30) < now:
                i.order_status = "Ready"
                i.save()
        elif i.order_status == "Ready":
            if i.last_modified + datetime.timedelta(minutes=2) < now:
                i.order_status = "Completed"
                i.save()
        
    orders = Orders.objects.all().exclude(order_status = "Completed")
    return render(request, 'status.html', {'orders':orders, 'today_orders':today_orders})

def index(request):
    return render(request, 'index.html')

def front(request):
    return render(request, 'front.html')

def movies(request):
    return render(request, 'movies.html')

def seating(request):
    return render(request, 'seating.html')

def payment(request):
    return render(request, 'payment.html')

def tickets(request):
    return render(request, 'tickets.html')

