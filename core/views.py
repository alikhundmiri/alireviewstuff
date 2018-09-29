from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404, HttpResponseRedirect

from .models import products, reviews
# Create your views here.

def lander(request):
	all_products = products.objects.all()
	context = {
		'all_products' : all_products,
	}
	return render(request, 'lander.html', context)

# def for product_review

def product_review(request, id=None):
	product = get_object_or_404(products, id=id)

	all_reviews = None
	if product:
		all_reviews = reviews.objects.filter(product_reference = id)
		

	context = {
		'product' : product,
		'all_reviews': all_reviews,
	}

	return render(request, 'core/productreview.html', context)