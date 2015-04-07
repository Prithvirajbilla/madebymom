from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse,HttpResponseRedirect,Http404,HttpResponseNotFound


def home(request):
	template = "index.html"
	return render(request,template)

