from django import forms
from landingPage.models import Customer

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'first_name', 'last_name', 'email', 'phone',
            'address', 'city', 'country', 'postal_code', 'image'
        ]