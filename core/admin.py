from django.contrib import admin
from .models import products, reviews

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	list_display = ["user", "product_name", "using_since", "replacement_available", "warranty_years", "affiliate_url", "public_display"]
	list_filter = ["user", "product_name", "using_since", "replacement_available", "warranty_years", "affiliate_url", "public_display"]
	search_fields = ["user", "product_name", "using_since", "replacement_available", "warranty_years", "affiliate_url", "public_display"]
	class Meta:
		model = products

class ReviewAdmin(admin.ModelAdmin):
	list_display = ["user", "product_reference", "product_caption", "public_display",]
	list_filter = ["user", "product_review", "product_reference", "product_caption", "public_display",]
	search_fields = ["user", "product_review", "product_reference", "product_caption", "public_display",]
	class Meta:
		model = reviews



admin.site.register(products, ProductAdmin)
admin.site.register(reviews, ReviewAdmin)