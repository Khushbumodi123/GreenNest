from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserProfileForm

def profile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            # process form data
            return HttpResponse("Profile saved successfully.")
    else:
        form = UserProfileForm()
    #return render(request, 'profile_page/profile.html', {'form': form})
    return render(request, 'profile_page/profile.html')
