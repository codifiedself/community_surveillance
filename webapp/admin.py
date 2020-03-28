from django.contrib import admin

from .models import Ngo, NgoUser, NgoOwner, State, District, Taluk, Pincode, PincodeLocation

admin.site.register(Ngo)
admin.site.register(NgoUser)
admin.site.register(NgoOwner)
admin.site.register(State)
admin.site.register(District)
admin.site.register(Taluk)
admin.site.register(Pincode)
admin.site.register(PincodeLocation)


