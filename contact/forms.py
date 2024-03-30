from django import forms
from contact.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=["first_name","last_name","deal_type","email","message"]
