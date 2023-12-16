from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
import templates

# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        # Get the username and password
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        # Check if the user exists
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist!')
        
        user = authenticate(request, username=username, password=password)
        # If he does, log them in
        if user is not None: # If user exists
            login(request, user) # Add session in the database and log in the user
            return redirect('home')
        else:
            messages.error(request, 'Username or Password does not exist')
    context = {'page':page}
    return render(request, 'base/login_register.html', context)

# def registerUser(request):
#     page = 'register'
#     context = {'page': page}
#     return render(request, 'base/login_register.html', context)

def registerUser(request):
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # the credentials that we send
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error has occured during registration')


    return render(request, 'base/login_register.html', {'form': form})


def editUser(request):
    form = UserChangeForm()
    if request.method == 'POST':
        form = UserChangeForm(request.POST) # the credentials that we send
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error has occured during registration')
    
    def get_object(self):
        return self.request.user

    return render(request, 'base/edit_profile.html', {'form':form})




def settings(request):
    return render(request, 'base/settings.html')


def logoutUser(request):
    logout(request)
    return redirect('login')

def kindergarten(request):
    return render(request, 'kindergarten.html')

def grade1(request):
    return render(request, 'grade1.html')

def grade2(request):
    return render(request, 'grade2.html')

def grade3(request):
    return render(request, 'grade3.html')

def introMultiplication(request):
    return render(request, 'introToMultiplication.html')

def grade4(request):
    return render(request, 'grade4.html')

def grade5(request):
    return render(request, 'grade5.html')

def grade6(request):
    return render(request, 'grade6.html')

def grade7(request):
    return render(request, 'grade7.html')

def grade8(request):
    return render(request, 'grade8.html')