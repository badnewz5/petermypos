from django.contrib import admin
from . models import*

# Register your models here.

admin.site.register((Product,Transfer))
admin.site.register(BranchProduct)
admin.site.register((ProductCategory,TaxPercentage))
