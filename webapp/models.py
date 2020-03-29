from django.contrib.auth.models import Permission
from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth import get_user_model

# from django.forms import ModelForm

from organizations.abstract import (
    AbstractOrganization,
    AbstractOrganizationOwner,
    AbstractOrganizationUser
)


# class OperationalLocation(models.Model):
# 	TYPE_CHOICES = (('state', 'State'), ('district', 'District'), ('block', 'Block'), ('city', 'City'))
# 	name = models.CharField(max_length=100)
# 	code = models.IntegerField(blank=True, null=True)
# 	location_type = models.CharField(max_length=30, choices=TYPE_CHOICES, default='block')

# 	def __str__(self):              # __unicode__ on Python 2
# 	    return "%s" % (self.name)




class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):              # __unicode__ on Python 2
        return "%s" % (self.name)

class District(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)

    def __str__(self):              # __unicode__ on Python 2
    	if self.state:
    		return "%s (%s)" % (self.name, self.state.name)
    	else:
    		return "%s (No State)" % (self.name)

        

class Taluk(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)

    def __str__(self):              # __unicode__ on Python 2
    	if self.district:
    		return "%s (District: %s)" % (self.name, self.district.name)
    	else:
    		return "%s ()" % (self.name)

class Pincode(models.Model):
	pincode = models.IntegerField()
	taluk = models.ForeignKey(Taluk, on_delete=models.SET_NULL, null=True)

	def __str__(self):              # __unicode__ on Python 2
	    return "%s" % (self.name)

class PincodeLocation(models.Model):
    name = models.CharField(max_length=100)
    pincode = models.ForeignKey(Pincode, on_delete=models.SET_NULL, null=True)
    lat = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    lng = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)

    def __str__(self):              # __unicode__ on Python 2
        return "%s" % (self.name)





class Ngo(AbstractOrganization):
	name = models.CharField(max_length=100)
	email = models.EmailField() #non mandatory
	phone = models.CharField(max_length=15) #non mandatory
	primary_contact = models.CharField(max_length=100)
	work_area = models.CharField(max_length=200)


	OPERATIONAL_LEVEL_CHOICES = (('state', 'State'), ('district', 'District'), ('block', 'Block'), ('city', 'City'), ('taluk', 'Taluk/Tehsil'), ('other', 'Other'))
	operational_level = models.CharField(max_length=50, choices=OPERATIONAL_LEVEL_CHOICES)


	operational_states = models.ManyToManyField(State)
	operational_districts = models.ManyToManyField(District)
	operational_taluks = models.ManyToManyField(Taluk)


	is_govt_funded = models.BooleanField()
	govt_programs_contributed_to = models.TextField(blank=True)
	govt_programs_partnered_with = models.TextField(blank=True)
	population_reach = models.IntegerField()

	REACH_MEDIUM_CHOICES = (('inperson', 'In Person Only'), ('remotely', 'Remote Only via phones'), ('remote_and_inperson', 'Both in Person & Remotely via phones'))
	medium_of_reach = models.CharField(max_length=30, choices=REACH_MEDIUM_CHOICES)

	staff_details = models.TextField(blank=True)
	does_staff_use_phones = models.BooleanField()
	staff_languages = models.TextField(blank=True)

	pincode = models.IntegerField(blank=True, null=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	created_by = models.ForeignKey(get_user_model(), models.SET_NULL, blank=True, null=True)

	def __str__(self):              # __unicode__ on Python 2
	    return "%s" % (self.name)




class NgoUser(AbstractOrganizationUser):
	pass

class NgoOwner(AbstractOrganizationOwner):
    pass


# class NgoForm(ModelForm):
#     class Meta:
#         model = Author
#         fields = ['name', 'title', 'birth_date']
