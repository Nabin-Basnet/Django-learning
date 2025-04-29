from django import forms

class Login_forms(forms.Form):
    email=forms.CharField(max_length=100,widget=forms.TextInput)
    password=forms.CharField(max_length=5,widget=forms.TextInput)
