from django.contrib import admin

from .models import *

class NgoAdmin(admin.ModelAdmin):
	list_display = ['name', 'primary_contact', 'email', 'phone',  'work_area', 'operational_level',  
    	'is_govt_funded', 'govt_programs_contributed_to', 'govt_programs_partnered_with', 'population_reach', 'medium_of_reach', 'staff_details',
    	'does_staff_use_phones', 'staff_languages', 'pincode']

	# search_fields = ['operational_states']
	list_filter = ['operational_states', 'operational_districts']

admin.site.register(Ngo, NgoAdmin)
admin.site.register(NgoUser)
admin.site.register(NgoOwner)
admin.site.register(State)
admin.site.register(District)
admin.site.register(Taluk)
admin.site.register(Pincode)
admin.site.register(PincodeLocation)


