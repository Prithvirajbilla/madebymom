from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse,HttpResponseRedirect,Http404,HttpResponseNotFound
from food.models import Food

import datetime

def home(request):
	template = "index.html"
	# foods = Food.objects.filter(day=datetime.date.today())
	foods = Food.objects.all()
	return render(request,template,{"foods":foods})


def cart(request):
	template = "cart.html"
	# foods = Food.objects.filter(day=datetime.date.today())
	foods = Food.objects.all()
	return render(request,template,{"foods":foods})
