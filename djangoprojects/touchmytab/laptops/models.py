from django.db import models
from django.utils.text import slugify

# Create your models here.
class Laptop(models.Model):
	productTitle = models.CharField(max_length=50)
	slug = models.SlugField(null=True, blank=True)
#	productDescription = models.CharField(max_length=1000)
	imageUrl = models.CharField(max_length=200)
	flipkartAmount = models.IntegerField()
	flipkartProductUrl = models.CharField(max_length=250)
	productBrand = models.CharField(max_length=300)
	inStock = models.CharField(max_length=40)
	productColor = models.CharField(max_length=70)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.productBrand)
		super(Mobile, self).save(*args, **kwargs)

	def __unicode__(self):
        	return self.productTitle
