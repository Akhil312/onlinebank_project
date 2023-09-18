from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
# Create your views here.
def home(request):
    return render(request,'index.html')

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid user")
            return redirect('login')
    return render(request,"login.html")

def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['confirm_password']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken!!")
                return redirect('register')
            user=User.objects.create_user(username=username,password=password)
            user.save();
            messages.info(request,"new user created")
            return redirect('login')
        else:
            return redirect('register')
        return redirect('/')

    return render(request,"register.html")
def detailsview(request):
    if request.method=='POST':
        Name = request.POST['Name']
        Dob = request.POST['Dob']
        Gender = request.POST['Gender']
        Email = request.POST['Email']
        Address = request.POST['Address']

        if User.objects.filter(Email=Email).exists():
            messages.info(request, "Email Exist!")
            return redirect("detailsview")

        user = User.objects.create_user(Name=Name,Dob=Dob,Gender=Gender,Email=Email,Address=Address)
        user.save();
        messages.info(request, "Added Successfully")
        return redirect('/')

    return render(request,"details.html")
def logout(request):
    auth.logout(request)
    return redirect('/')

