from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import table1,table2
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as authlogin,logout as authlogout
from django.contrib.auth.decorators import login_required
# Create your views here

def heading(request):
    error_message = None
    
    if request.method == 'POST':
        print("Received POST request")
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            authlogin(request, user)
            return redirect('l1')
        else:
            error_message = 'Invalid credentials!!!!!ENTER CORRECT USERNAME AND PASSWORD'
    
    return render(request,'text.html', {'error_message': error_message})

@login_required(login_url='heading/')
def login(request):
    user = request.user  
    try:
        user_details = table1.objects.get(user=user)
        user_marks = table2.objects.get(user=user)
    except (table1.DoesNotExist, table2.DoesNotExist):
        user_details = None
        user_marks = None 
    return render(request, 'login.html', {'user': user, 'user_details': user_details, 'user_marks': user_marks})

@login_required(login_url='heading/')
def logout(request):
        authlogout(request)
        return redirect('main')

def signup(request):
    user=None
    error_message=None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.create_user(username=username, password=password)
        except Exception as e:
            error_message=str(e)
        if user:
            id=request.POST.get('stud_id')
            name=request.POST.get('name')
            pho=request.POST.get('ph_no')
            email=request.POST.get('email')
            t1obj = table1.objects.create(user=user, student_id=id, name=name, phone_no=pho, email=email)
            m1=request.POST.get('m1')
            m2=request.POST.get('m2')
            m3=request.POST.get('m3')
            t2obj = table2.objects.create(user=user,Physics=m1,Chemistry=m2,Maths=m3)
            return redirect('main')
         
    return render(request,'signup.html',{'user':user,'error_message':error_message})