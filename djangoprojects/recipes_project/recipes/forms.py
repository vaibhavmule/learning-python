from django.forms import ModelForm, HiddenInput
from recipes.models import Ingredient

class Ingredient(ModelForm):

	class Meta:
		model = Ingredient
		widgets = {'recipes' HiddenInput()}