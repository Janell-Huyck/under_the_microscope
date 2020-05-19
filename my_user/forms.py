from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput, max_length=20)


class MyUserForm(forms.Form):
    username = forms.CharField(
        max_length=50)
    display_name = forms.CharField(max_length=50)
    password = forms.CharField(
        widget=forms.PasswordInput, max_length=20)

    home_page = forms.URLField(
        max_length=200, required=False)
    age = forms.IntegerField(required=False)
