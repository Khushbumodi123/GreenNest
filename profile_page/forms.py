from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'firstname', 'lastname', 'email', 'phone',
            'address', 'city', 'country', 'postal_code', 'profile_picture'
        ]