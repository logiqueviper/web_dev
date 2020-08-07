from django import forms

class Registration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
class Get_Email(forms.Form):
    email = forms.EmailField()
    