from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
def index(request):
	return render(request,"ytindex.html")


def searchv(request):
	return render(request,"searchv.html")


def ytcomments(request):
	return render(request,"ytcomments.html")
