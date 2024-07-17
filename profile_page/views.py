from django.shortcuts import render, redirect
from django.http import HttpResponse

from landingPage.models import Customer
from .forms import UserProfileForm

def profile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return HttpResponse("Profile saved successfully.")
    else:
        form = UserProfileForm()
    return render(request, 'profile_page/profile.html', {'form': form})


def prof(request):
    if request.user.is_authenticated:
        customer = Customer.get_customer_by_email(email=request.user.email)
        return render(request, 'profile_page/profile1.html', {'customer': customer})
    else:
        return HttpResponse("not!!!")