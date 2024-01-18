from django import forms
from website.models import contact


class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
    
class contact_form(forms.ModelForm):
    
    class meta:
        model = contact

