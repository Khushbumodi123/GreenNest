from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout 
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib import messages
from django.core.mail import send_mail

def register(request):
    messages.info(request, 'Please fill the form below to register.')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('authapp:login')
        else:
            # Handle form errors, e.g., display errors in the form
            print(form.errors)
    else:
        messages.success(request, 'Please fill the form below to register.')
        form = UserCreationForm()  # Create a new form instance for GET requests
    return render(request, 'authapp/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        if username and password:
            user = authenticate(request, username=username, password=password) 
            if user is not None:
                auth_login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('myapp:store')
            else:
                messages.error(request, "Invalid email or password.")
        else:
            messages.error(request, "Please provide both email and password.")
        return redirect('authapp:login')
    else:
        return render(request, 'authapp/login.html', {})

def forget_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            # Assuming you have configured email backend in Django settings
            send_mail(
                'Password Reset Request',
                'Please click the link to reset your password.',
                'from@example.com',
                [username],
                fail_silently=False,
            )
            messages.info(request, f'Password reset link sent to {username}.')
            return redirect('authapp:login')
    else:
        form = PasswordResetForm()
    return render(request, 'authapp/forget_password.html', {'form': form})

def password_reset_done(request):
    return render(request, 'authapp/password_reset_done.html')