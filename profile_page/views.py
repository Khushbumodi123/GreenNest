from django.shortcuts import render, redirect
from django.http import HttpResponse

from landingPage.models import Customer
from .forms import UserProfileForm

# def profile(request):

#     if request.user.is_authencticated:

#         if request.method == "POST":
#             user_profile = Customer.get_customer_by_email(email=request.user.email)
#             form = UserProfileForm(request.POST, instance=user_profile)
#             if form.is_valid():
#                 form.save()  # Save the form data to the database
#                 return HttpResponse("Profile saved successfully.")
        # else:
        #     user_profile = Customer.get_customer_by_email(email=request.user.email)
        #     form = UserProfileForm(instance=user_profile)

#         return render(request, 'profile_page/profile.html', {'form': form, 'user_profile': user_profile})
#     else:
#         return redirect('landingPage:login')

def prof(request):
    if request.user.is_authenticated:

        customer = Customer.get_customer_by_email(email=request.user.email)

        if request.method == "POST":      
            form = UserProfileForm(request.POST, request.FILES, instance=customer)
            if form.is_valid():
                form.save()  # Save the form data to the databas
        else:
            form = UserProfileForm(instance=customer)
        return render(request, 'profile_page/profile.html', {'form': form, 'user_profile': customer})
    else:
        return redirect('landingPage:login')

