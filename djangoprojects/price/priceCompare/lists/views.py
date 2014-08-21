from django.shortcuts import render
from django.http import HttpResponse
from lists.models import Laptop
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'lists/index.html'
	context_object_name = 'product_list'

	def get_queryset(self):
		return Laptop.objects.all()[:5]
	
