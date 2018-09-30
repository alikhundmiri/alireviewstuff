from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404, HttpResponseRedirect, Http404
from django.urls import reverse
from django.conf import settings

from .models import products, reviews
# Create your views here.

def lander(request):
	all_products = products.objects.filter(public_display=True)
	context = {
		'all_products' : all_products,
		"production" : settings.PRODUCTION,

	}
	return render(request, 'lander.html', context)

def hidden(request):
	context = {
		"production" : settings.PRODUCTION,
	}
	return render(request, 'hidden.html', context)

def about(request):
	context = {
		"production" : settings.PRODUCTION,

	}
	return render(request, 'core/about.html', context)


# def for product_review
def product_review(request, id=None):
	product = get_object_or_404(products, id=id)

	all_reviews = None
	if product:
		all_reviews = reviews.objects.filter(product_reference__id = id).exclude(public_display = False)

	context = {
		'product' : product,
		'all_reviews': all_reviews,
		"production" : settings.PRODUCTION,

	}

	return render(request, 'core/productreview.html', context)