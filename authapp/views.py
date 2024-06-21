from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm, PasswordResetForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('myapp:store')
    else:
        form = UserCreationForm()
    return render(request, 'authApp/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('myapp:store')
    else:
        form = AuthenticationForm()
    return render(request, 'authApp/login.html', {'form': form})



def forget_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp:store')
    else:
        form = PasswordResetForm()
    return render(request, 'authApp/forget_password.html', {'form': form})
