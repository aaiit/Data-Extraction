from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Greeting
from django.views.decorators.csrf import csrf_exempt

from Core import *
# Create your views here.
def index(request):
	return render(request, "choose.html")

@csrf_exempt 
def form(request):
	# return HttpResponse('Hello from Python!')
	if request.method=='POST':
		fields=json.loads(request.body)
		#fields = {'q': 'covid19', 'lang': 'en', 'result_type': 'popular'}
		return HttpResponse(test(fields))
	return render(request, "form1.html")


def standardOperators(request):
	return render(request, "standard-operators.html")
