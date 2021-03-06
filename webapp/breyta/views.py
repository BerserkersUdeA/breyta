from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from django.core.files import File
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.template import RequestContext
from django.template import Context

from breyta.forms import UserForm

# Create your views here.




def index(request):
    return render(request, 'breyta/index.html')


@login_required
def inicio(request):
    return render(request, 'breyta/inicio.html')

@login_required
def billetera(request):
    return render(request, 'breyta/billetera.html')

@login_required
def store(request):
    return render(request, 'breyta/store.html')


@login_required
def aboutus(request):
    return render(request, 'breyta/aboutus.html')


@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(
        request, 'breyta/registration.html', {
            'user_form': user_form,
            'registered': registered
        })


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('breyta:main')
                #render(request, 'breyta/main.html', {})
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(
                username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'breyta/login.html', {})
