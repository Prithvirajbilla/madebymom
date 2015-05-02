from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse,HttpResponseRedirect,Http404,HttpResponseNotFound
from food.models import Food
import json
import datetime
import urllib 

def home(request):
	template = "index.html"
	# foods = Food.objects.filter(day=datetime.date.today())
	foods = Food.objects.all()
	return render(request,template,{"foods":foods})


def cart(request):
	template = "cart.html"
	if "cart_basket" in request.COOKIES:
		cookie = urllib.unquote(request.COOKIES.get("cart_basket")).decode('utf8')
		cart_basket = json.loads(cookie)
		foods = []
		for key in cart_basket:
			pid = key[1:]
			print pid,cart_basket[key]

			dish = Food.objects.get(id=pid)
			if (cart_basket[key] > 10 or cart_basket[key] < dish.quantity) and cart_basket >= 1:
				foods.append(Food.objects.get(id=pid))
			else:
				raise Http404
		return render(request,template,{"foods":foods})
	else:
		return render(request,template,{"foods":None})