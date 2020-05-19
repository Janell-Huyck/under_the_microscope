from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render
from microscope import settings
from my_user.forms import LoginForm


@login_required
def index(request):
    context = {'settings': settings.AUTH_USER_MODEL}
    # context['settings'] = settings.AUTH_USER_MODEL
    return render(request, 'index.html', context)


def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('loginPage'))


def loginView(request):
    message_after = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('home'))
                )
            else:
                message_after = """Credentials supplied do not match our records.
                    Please try again."""
    form = LoginForm()
    return render(request, 'general_form.html',
                  {'form': form, 'message_after': message_after})
