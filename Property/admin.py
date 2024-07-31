from django.contrib import admin

from .models import Property

# from .forms import PropertyForm

# Register your models here.


# class PropertyAdmin(admin.ModelAdmin):
#     form = PropertyForm


admin.site.register(Property)  # , PropertyAdmin
