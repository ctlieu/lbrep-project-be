from django.contrib import admin
from listings.models import Listing
from listings.models import Poi
from .forms import PoisForm

class PoiAdmin(admin.ModelAdmin):
    form = PoisForm
    
# # Register your models here.
# admin.site.register(Listing, ListingAdmin)
admin.site.register(Listing)
admin.site.register(Poi, PoiAdmin)