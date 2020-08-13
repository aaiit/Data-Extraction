from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Greeting

# Create your views here.
def index(request):
	# return HttpResponse('Hello from Python!')
	return render(request, "choose.html")


def form(request):
	# return HttpResponse('Hello from Python!')
	if request.method=='POST':
		data=json.loads(request.body)
		return HttpResponse("You send data")
	return render(request, "f.html")


def standardOperators(request):
	return render(request, "standard-operators.html")
