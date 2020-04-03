from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from .models import *
#from .forms import LaptopSearchForm
from django.db import connection
from django.http import HttpResponseRedirect
from django.shortcuts import render
import datetime



# Create your views here.
def yogeshblog(request):
     return render(request,"yogeshblog.html")