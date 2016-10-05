from django.shortcuts import render
from django.http import HttpResponse
from laptops.models import Laptop
from django.views.generic import ListView, DetailView

# Create your views here.
class IndexView(ListView):
	template_name = 'laptops/index.html'
	context_object_name = 'product_list'

	def get_queryset(self):
		return Laptop.objects.all()[:5]

class LaptopDetail(DetailView):
	model = Laptop
	template_name = 'laptops/detail.html'

	def get_queyset(self):
		return Laptop.objects.filter(pk=pk)


