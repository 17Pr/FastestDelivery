from cgitb import reset
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import transporter
from .models import distrubuter



def home(request):
    
    return render(request,'index.html')

    
def join(request):
    if(request.method=="POST"):
        stud=transporter()
        stud.name=request.POST['name']
        stud.email=request.POST['email']
        stud.phone=request.POST['mobile']
        stud.destination=request.POST['place of destination'] 
        stud.link=request.POST['linkedin']
        stud.gender=request.POST['gender']

        stud.save()
    return render(request,'join.html')

def services(request):
    if(request.method=="POST"):
        stude=distrubuter()
        stude.name=request.POST['name']
        stude.email=request.POST['email']
        stude.phone=request.POST['mobile']
        stude.placeofpickup=request.POST['pickup'] 
        stude.destination=request.POST['destination']
        stude.mode=request.POST['mode']
        stude.typeofproduct=request.POST['typeofproduct']

        stude.save()
    return render(request,'services.html')

def login(request):
    if(request.method=="POST"):
        email=request.POST['email']
        contact=request.POST['contact']
        checklog=transporter.objects.get(email=email,contact=contact)
        if(checklog):
            return redirect('admin')
        else:
            return render(request,'adminhome.html')

    return render(request,'login.html')


def signup(request):
    return render(request,'signup.html')
def admin(request):
    return render(request,'adminhome.html')

    
def adminhome(request):
    return render(request,'adminhome.html')
    
def adminlogin(request):
    return render(request,'adminlogin.html')

    
def transporters(request):
    trans=transporter.objects.all()
    return render(request,'transporter.html',{'trans':trans})
    
def delete(request,id):
    tran=transporter.objects.get(id=id)
    tran.delete()
    return redirect('adminhome')

def distrubuters(request):
    distru=distrubuter.objects.all()
    return render(request,'distrubuter.html',{'distru':distru})
         

def deletedis(request,id):
    dis=distrubuter.objects.get(id=id)
    dis.deletedis()
    return redirect('adminhome')
    
