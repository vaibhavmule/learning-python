from django.contrib import admin

from .forms import SignUpForm
from .models import SignUp

# Register your models here.

class SingUpAdmin(admin.ModelAdmin):
    form = SignUpForm
    list_display = ('email', 'timestamp', 'updated')
    class Meta:
        model = SignUp

admin.site.register(SignUp, SingUpAdmin)
