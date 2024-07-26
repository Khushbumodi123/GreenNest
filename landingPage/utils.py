# utils.py
from django.core.exceptions import ValidationError
from django.utils import timezone
import datetime

def one_year_from_today():
    return timezone.now() + datetime.timedelta(days=365)

def validate_rating(value):
    if value < 0 or value > 5:
        raise ValidationError(f'Rating must be between 0 and 5. You entered {value}.')
