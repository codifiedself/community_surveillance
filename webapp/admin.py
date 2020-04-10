from django.contrib import admin

from .models import *

class NgoAdmin(admin.ModelAdmin):
	list_display = ['name', 'primary_contact', 'email', 'phone',  'work_area', 'operational_level', 'medium_of_reach', 'staff_count',
    	'does_staff_use_phones']

	# search_fields = ['operational_states']
	list_filter = ['operational_states', 'operational_districts']

	search_fields = ['name']


class CommodityAdmin(admin.ModelAdmin):
	list_display = ['name','quantity','unit','price']


class DistrictAdmin(admin.ModelAdmin):
	search_fields = ['name']


class NgoDistrictAdmin(admin.ModelAdmin):
	list_display = ['ngo', 'district', 'population_reach']
		




admin.site.register(Ngo, NgoAdmin)
admin.site.register(NgoDistrict, NgoDistrictAdmin)
admin.site.register(NgoUser)
admin.site.register(NgoOwner)
admin.site.register(State)
admin.site.register(District, DistrictAdmin)
admin.site.register(Taluk)
admin.site.register(Pincode)
admin.site.register(PincodeLocation)
admin.site.register(Commodity, CommodityAdmin)


