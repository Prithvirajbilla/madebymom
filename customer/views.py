from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse,HttpResponseRedirect,Http404,HttpResponseNotFound
from food.models import Food
import json
import datetime
import urllib 
from users.models import *


def check_order(request,pid,quant):

	data = {}
	try:
		food = Food.objects.get(pk=pid)
		if int(food.quantity) >= int(quant):
			data["result"] = True
		else:
			data["result"] = False
			data["quantity"] = int(food.quantity)
	except Exception, e:
		data["result"] = False
	return HttpResponse(json.dumps(data), content_type="application/json")

def home(request):
	template = "index.html"
	# foods = Food.objects.filter(day=datetime.date.today())
	foods = Food.objects.all()
	response = render(request,template,{"foods":foods})

	if "cart_basket" in request.COOKIES:
		cookie = urllib.unquote(request.COOKIES.get("cart_basket")).decode('utf8')
		print cookie
		cart_basket = json.loads(cookie)
		for key in cart_basket:
			pid = key[1:]
			if cart_basket[key] == 0:
				continue
			dish = Food.objects.get(pk=pid)
			print cart_basket[key],dish.quantity
			if cart_basket[key] <= 10 and cart_basket >= 1:
				if int(cart_basket[key]) > int(dish.quantity):
					print dish.quantity
					cart_basket[key] = dish.quantity

		response.set_cookie("cart_basket",urllib.quote(json.dumps(cart_basket)))

	return response


def cart(request):
	template = "cart.html"
	if "cart_basket" in request.COOKIES:
		cookie = urllib.unquote(request.COOKIES.get("cart_basket")).decode('utf8')
		cart_basket = json.loads(cookie)
		foods = []
		for key in cart_basket:
			pid = key[1:]
			print pid,cart_basket[key]

			dish = {"food":Food.objects.get(id=pid)}
			if cart_basket[key] == 0:
				continue
			if cart_basket[key] <= 10  and cart_basket >= 1:
				dish["order_quantity"] = cart_basket[key]
				if  cart_basket[key] <= dish["food"].quantity:
					dish["in_stock"] = True
				else:
					cart_basket[key] = dish["food"].quantity
					dish["in_stock"] = False
				foods.append(dish)
			else:
				raise Http404
		response = render(request,template,{"foods":foods})
		response.set_cookie("cart_basket",urllib.quote(json.dumps(cart_basket)))
		return response
	else:
		return render(request,template,{"foods":None})


def checkout(request):
	template = "checkout.html"
	if "cart_basket" in request.COOKIES:
		cookie = urllib.unquote(request.COOKIES.get("cart_basket")).decode('utf8')
		cart_basket = json.loads(cookie)
		print cart_basket
		foods = []
		for key in cart_basket:
			pid = key[1:]
			dish = {"food":Food.objects.get(id=pid)}
			if cart_basket[key] == 0:
				continue
			if cart_basket[key] <= 10  and cart_basket >= 1:
				dish["order_quantity"] = cart_basket[key]
				if  cart_basket[key] <= dish["food"].quantity:
					print dish
					dish["in_stock"] = True
					foods.append(dish);
				else:
					cart_basket[key] = dish["food"].quantity
					request.session["expired"] =True
					return HttpResponseRedirect("/cart")
			else:
				raise Http404

		if request.method == "POST":
			name = request.POST["name"].strip()
			email = request.POST["email"].strip()
			mobile = request.POST["mobile"].strip()
			address_1 = request.POST["address_1"].strip()
			address_2 = request.POST["address_2"].strip()
			area = request.POST["area"].strip()


			if name != "" and email != "" and mobile != "" and address_1 != "" and area != "":
				order = Order(name=name,email=email,mobile=mobile,address_line_1=address_1,
					address_line_2=address_2,area=area)
				order.save()
				cart = Cart(order=order,discount=0)
				cart.save()
				print len(foods)
				print foods
				for dish in foods:
					item = Item(cart=cart,food=dish["food"],quantity=dish["order_quantity"])
					dish["food"].quantity-=dish["order_quantity"]
					dish["food"].save()
					item.save()
					print item.food.name

				return HttpResponseRedirect("/thanks/"+str(cart.pk));
			else:
				request.session["wrong"] = True

				return HttpResponseRedirect("/cart/")

	return HttpResponseRedirect("/cart/")



def thanks(request,pid):
	template = "thanks.html"
	cart = Cart.objects.get(pk=pid)
	items = Item.objects.filter(cart=cart)
	print items
	return render(request,template,{"cart":cart,"items":items})