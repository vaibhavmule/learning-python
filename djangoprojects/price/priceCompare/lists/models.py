from django.db import models

# Create your models here.
class Laptop(models.Model):
	productBrand = models.CharField(max_length=30)
	productDescription = models.CharField(max_length=1000)
	productUrl = models.CharField(max_length=200)
	imageUrl = models.CharField(max_length=250)
	amount = models.IntegerField()

	def __unicode__(self):
        	return self.productBrand
