from django.contrib import admin
from .models import MomoCategory ,Product ,MenuCategory,allmenu,Contact,IngredientCategory,ingredient
# Register your models here.
admin.site.register([MomoCategory,Product])
admin.site.register([MenuCategory,allmenu])
admin.site.register(Contact)
admin.site.register([IngredientCategory,ingredient])