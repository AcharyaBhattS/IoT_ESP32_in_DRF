from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    return render(request,'home.html')

def table1(request):
    all_data1 = sbdb.objects.all()
    # return render(request,'table.html')
    return render(request,'table.html',{'all_data_key1':all_data1})

def esp32_data(request):
    all_data2 = esp32_db.objects.all()
    # return render(request,'esp32.html')
    return render(request,'esp32.html',{'all_data_key2':all_data2})

def insert_data(request):
	if request.method == "POST":
		name = request.POST['name']
		age = request.POST['age']
		address = request.POST['address']
		obj1 = sbdb.objects.create(name=name, age=age, address=address)
		obj1.save()
	return render(request,'insertdata.html')

# http://192.168.1.7/ippt?n=Ranajit+Dey&a=42&b=Sinthee,+Dum+Dum,+Kolkata
def ippt(request):
    try:
        name1 = request.GET.get('n')
        age1 = request.GET.get('a')
        address1 = request.GET.get('b')
        # print(name1,'\n',age1,'\n',address1)
        obj2 = sbdb.objects.create(name=name1, age=age1, address=address1)
        obj2.save()
        return HttpResponse("Okay")
    except:
        return render(request,'home.html')

# Browsing from ESP32_________________________________________________
# http://192.168.1.7/esp32aidi?led1=1&temp1=254
def esp32aidi(request):
    try:
        LED1 = request.GET.get('led1')
        Temp1 = request.GET.get('temp1')
        obj3 = esp32_db.objects.create(led1=LED1, temp1=Temp1)
        obj3.save()
        return HttpResponse("Okay")
    except:
        return render(request,'esp32.html')

# File Upload process_________________________________________________
def handle_upload_file1(f):
    with open("myApp/static/upload/"+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def uploadCustomer(request):
    if request.method == 'POST':
        upl=Upld_sbdb()
        upl.name = request.POST['name']
        upl.email = request.POST['email']
        upl.fileName = request.FILES['fileName'].name
        upl.save()
        handle_upload_file1(request.FILES['fileName'])
        return HttpResponse(request.FILES['fileName'].name)
    else:
        return render(request, 'custUpload.html')
