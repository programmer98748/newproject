from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from website.forms import SignupForm
#, UserUpdateForm, ProfileForm


def register(request):
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, 'your account has been created ') 
            return redirect('login')
    else:
        form = SignupForm()
    context = {'form':form}
    return render(request, 'store/auth/register.html', context)


def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request, 'logged in')
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'logged in success')
                return redirect('/')
            else:
                messages.error(request, 'invalid username or password')
                return redirect('login')
                
        return render(request, 'store/auth/login.html')

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, ' logged out')
    return redirect('/')
    
         