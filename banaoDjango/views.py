from django.shortcuts import redirect, render
from django.contrib import messages
from banaoDjango.models import patient
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request, 'index.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('passwd')
        fname = request.POST.get('fname')
        cuser = authenticate(username=username, password=password, fname = fname)

        if cuser is not None:
            print(username,password)
            login(request, cuser)
            messages.success(request, "Login successful")
            return redirect('Home')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('SignUp')
    return render(request,'signin.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstName = request.POST.get('fname')
        lastName = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('passwd')
        confirmPassword = request.POST.get('cpasswd')

        Patient = patient(username=username, firstName=firstName, lastName=lastName, email=email, password=password, cpassword=confirmPassword)
        Patient.save()
        messages.success(request,"User has been created successfully")

        return redirect('SignIn')
        # user = authenticate(request, username=username, password=password)
        # if user is not None:
        #     login(request, user)
        #     return redirect('index')
        # else:
        
    return render(request,'signup.html')

def signout(request):
    return render(request,'signout.html')
