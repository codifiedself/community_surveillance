from django.contrib import admin

from .models import *

import csv
from django.http import HttpResponse


def range_text(count):
	range = ''

	if(count == 1000):
		range = 'less than 1000 people'
	elif (count == 10000):
		range = '1000 to 10,000 people'
	elif (count == 50000):
		range = '10,000 to 50,000 people'
	elif (count == 100000):
		range = 'more than 50,000 people'

	return range

class NgoAdmin(admin.ModelAdmin):
	list_display = ['name', 'primary_contact', 'email', 'phone',  'work_area','special_needs_groups','operational_level', 'medium_of_reach', 'staff_count',
    	'does_staff_use_phones', 'states_display', 'district_display', 'created_at']

	# search_fields = ['operational_states']
	list_filter = ['operational_states', 'operational_districts']

	search_fields = ['name']

	actions = ["export_as_csv"]

	def states_display(self, obj):
		return ", ".join([
			state.name for state in obj.operational_states.all()
		])

	states_display.short_description = "States"

	def district_display(self, obj):
		return ", ".join([
			nd.district.name + " (" + range_text(nd.population_reach) + ")\n" for nd in obj.ngo_districts.all()
		])

	district_display.short_description = "Districts"


	def export_as_csv(self, request, queryset):
		meta = self.model._meta
		field_names = [field.name for field in meta.fields]

		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
		writer = csv.writer(response)

		writer.writerow(field_names)
		for obj in queryset:
		    row = writer.writerow([getattr(obj, field) for field in field_names])

		return response

	export_as_csv.short_description = "Export Selected"





	# def population_reach(self, obj):
	# 	return population_reach
	# 		district.name for district in obj.operational_districts.all()
	# 	])


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


