from django import forms

class Login_forms(forms.Form):
    email=forms.CharField(max_length=100,widget=forms.TextInput)
    password=forms.DecimalField(max_value=20,widget=forms.NumberInput)
