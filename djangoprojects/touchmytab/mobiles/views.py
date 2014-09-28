from django.shortcuts import render
from django.http import HttpResponse
from mobiles.models import Mobile
from django.views.generic import ListView, DetailView

# Create your views here.
class IndexView(ListView):
	template_name = 'mobiles/index.html'
	context_object_name = 'product_list'

	def get_queryset(self):
		return Mobile.objects.all()[:20]

class MobileDetail(DetailView):
	model = Mobile
	template_name = 'mobiles/detail.html'

	def get_queyset(self):
		return Mobile.objects.filter(pk=pk)


