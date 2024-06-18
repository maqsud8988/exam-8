from django import forms
from .models import Subscribe_to_Newsletter

class GetInTouchForm(forms.ModelForm):
    class Meta:
        model = Subscribe_to_Newsletter
        fields = ('name', 'email', 'message')
