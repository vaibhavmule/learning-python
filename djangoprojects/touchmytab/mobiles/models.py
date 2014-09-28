from django.db import models
from django.utils.text import slugify

# Create your models here.
class Mobile(models.Model):
	productBrand = models.CharField(max_length=70)
	slug = models.SlugField(null=True, blank=True)
	productDescription = models.CharField(max_length=1000)
	flipkartProductUrl = models.CharField(max_length=200)
	snapdealProductUrl = models.CharField(max_length=200)
	amazonProductUrl = models.CharField(max_length=200)
	imageUrl = models.CharField(max_length=250)
	flipkartAmount = models.IntegerField()
	snapdealAmount = models.IntegerField()
	amazonAmount = models.IntegerField()

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.productBrand)
		super(Mobile, self).save(*args, **kwargs)

	def __unicode__(self):
        	return self.productBrand
