from django.conf import settings
from django.db import models

import datetime

# Create your models here.

class products(models.Model):
	user					=			models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	product_name			=			models.CharField(max_length=50, blank=False, null=False, default="")
	mrp						=			models.PositiveIntegerField(default=0)
	selling_price			=			models.PositiveIntegerField(default=0)
	using_since				=			models.DateField(default=datetime.date.today)
	replacement_available	=			models.BooleanField(default=False)
	warranty_years			=			models.PositiveIntegerField(default=0)
	affiliate_url			=			models.URLField(max_length=10000, blank=False, null=False, help_text="Product Affiliate link.")
	number_of_reviews		=			models.PositiveIntegerField(default=0)
	image_url				=			models.URLField(max_length=10000, blank=False, null=False, default='http://placehold.it/230x260')
	
	# delete this later
	image_display			=			models.TextField(max_length=1000, blank=True, null=True)

	# To Avoid spam content
	public_display			=			models.BooleanField(default=False)

	timestamp				=			models.DateTimeField(auto_now=False, auto_now_add=True)
	updated					=			models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return(self.product_name)

	class Meta:
		ordering = ["-timestamp", "-updated"]
		verbose_name = 'Product'
		verbose_name_plural = 'Products'

class reviews(models.Model):
	user					=			models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	product_review			=			models.TextField(max_length=100000, blank=False, null=False, default="12 words cant do justice to this product, wait for full review.")
	product_caption			=			models.TextField(max_length=128, blank=False, null=False, default="Amazing Product... 5/7 would buy again.")
	product_reference		=			models.ForeignKey(products, related_name='all_products', blank=True, null=True, on_delete=models.CASCADE)
	
	# To Avoid spam content
	public_display			=			models.BooleanField(default=False)
	
	timestamp				=			models.DateTimeField(auto_now=False, auto_now_add=True)
	updated					=			models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return(self.product_caption)

	class Meta:
		ordering = ["-timestamp", "-updated"]
		verbose_name = 'Review'
		verbose_name_plural = 'Reviews'

"""
I N    M Y    M I N D:

the site is populated with products.
each product will have multiple reviews, on different point of times.

>> so one products will have miltiple reviews. <<


"""