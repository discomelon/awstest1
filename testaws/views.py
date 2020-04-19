from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	response = HttpResponse()
	response.write("<p> This Works </p>")
	return response