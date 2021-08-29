from django import forms

class user_form(forms.Form):

    user_name = forms.CharField(required=True, label="Full Name",
                                widget=forms.TextInput(attrs={'placeholder':'enter your full name',
                                                              'style':'width:300px'}))

    user_email = forms.EmailField(label="Email ID")

    user_date=forms.DateField(label="Date of birth", widget=forms.TextInput(attrs={'type':'date'}))

    user_phone = forms.IntegerField(label="Phone Number")

    password = forms.PasswordInput()