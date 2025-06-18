from django.forms import ModelForm

from .models import customer

class customer_form(ModelForm):
    class Meta:
        model=customer
        fields='__all__'

