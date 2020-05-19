from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render
from my_user.forms import LoginForm


@login_required
def index(request):
    return render(request, 'index.html')


def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def loginview(request):
    message_after = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('home'))
                )
            else:
                message_after = """Credentials supplied do not match our records.
                    Please try again."""
    form = LoginForm()
    return render(request, 'login_form.html',
                  {'form': form, 'message_after': message_after})


# def loginView(request):
#     username = request.POST('username')
#     password = request.POST('password')
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return HttpResponseRedirect(reverse('home'))
#     else:
#         return HttpResponseRedirect(reverse('invalid_login'))


def invalid_loginView(request):
    return render(request, 'invalid_login.html')
