from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from django.core.files import File
from django.conf import settings

from django.template.loader import get_template
from django.template import RequestContext
from django.template import Context

# Create your views here.

def home(request):

    return render(request, "breyta/base.html")

