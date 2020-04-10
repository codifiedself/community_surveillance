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
	    return "%s" % (self.pincode)

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


	WORK_AREA_CHOICES = (
							('health','Health'), 
							('education', 'Education'), 
							('nutrition', 'Nutrition'),
							('disability', 'Disability'), 
							('wash', 'WASH'), 
							('livelihoods','Livelihoods'), 
							('financial_services', 'Financial Services'),
							('others','Others')
						)

	work_area = MultiSelectField(choices=WORK_AREA_CHOICES, null=True, blank=True)


	OPERATIONAL_LEVEL_CHOICES = (('state', 'State'), ('district', 'District'), ('block', 'Block'), ('city', 'City'), ('taluk', 'Taluk/Tehsil'), ('other', 'Other'))
	operational_level = MultiSelectField(choices=OPERATIONAL_LEVEL_CHOICES, null=True, blank=True)


	SPECIAL_NEEDS_CHOICES = (
								('no', 'No, we do not work with any special needs group'),
								('mental_illness', 'People with mental illness'),
								('hearing_loss','People with hearing loss'),
								('physical_disabilities','People with physical disabilities'),
								('intellectual_disabilities','People with intellectual disabilities'),
								('aids','People living with HIV/AIDS'),
								('sex_workers', 'Sex Workers'),
								('injective_drug_users', 'Injective Drug Users'),
								('msm_and_trans','MSM and Trans People'),
								('chronic_illness','People living with chronic illness such as cancer, heart ailments, are immune-compromised'),
								('elderly','Elderly'),
								('tribal_population','Tribal population'),
								('rural_poor','Rural poor'),
								('urban_poor','Urban poor'),
								# ('migrants','Migrants and internally displaced'),
								('migrant_labourers', 'Migrant labourers'),
								('hospice_shelters','Hospice/homes/orphanages/shelters'),
								('homeless','Homeless'),
								('others','Others')
							)
	special_needs_groups = MultiSelectField(choices=SPECIAL_NEEDS_CHOICES, null=True, blank=True)


	operational_states = models.ManyToManyField(State)
	# operational_districts = models.ManyToManyField(District)
	operational_districts = models.ManyToManyField(District, through='NgoDistrict', blank=True)	
	# operational_taluks = models.ManyToManyField(Taluk)

	# is_govt_funded = models.BooleanField()
	# govt_programs_contributed_to = models.TextField(blank=True)
	# govt_programs_partnered_with = models.TextField(blank=True)
	# population_reach = models.IntegerField(default=0)

	REACH_MEDIUM_CHOICES = (('inperson', 'In Person Only'), ('remotely', 'Remote Only via phones'), ('remote_and_inperson', 'Both in Person & Remotely via phones'))
	medium_of_reach = models.CharField(max_length=30, choices=REACH_MEDIUM_CHOICES, blank=False, default="")


	staff_count = models.IntegerField(default=0)
	# staff_details = models.TextField(blank=True)

	BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
	does_staff_use_phones = models.BooleanField(choices=BOOL_CHOICES, blank=False, default=False)
	# staff_languages = models.TextField(blank=True)

	# pincode = models.CharField(max_length=400, default="")

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	created_by = models.ForeignKey(get_user_model(), models.SET_NULL, blank=True, null=True)

	def __str__(self):              # __unicode__ on Python 2
	    return "%s" % (self.name)

	class Meta:
		verbose_name = 'NGO'


class NgoDistrict(models.Model):
	ngo = models.ForeignKey(Ngo, on_delete=models.CASCADE)
	district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
	REACH_CHOICES = ((1000,'less than 1000 people'), (10000,'1000 to 10,000 people'), (50000,'10,000 to 50,000 people'), (100000,'more than 50,000 people'))
	population_reach = models.IntegerField(choices=REACH_CHOICES, blank=False, default="")


class NgoUser(AbstractOrganizationUser):
	class Meta:
		verbose_name = 'NGO User'

class NgoOwner(AbstractOrganizationOwner):
	class Meta:
		verbose_name = 'NGO Owner'


class Commodity(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=10)
    price = models.IntegerField()#(max_digits=6, decimal_places=2)

    def __str__(self):              # __unicode__ on Python 2
        return "%s" % (self.name)

    class Meta:
    	verbose_name_plural = "Commodities"


# class NgoForm(ModelForm):
#     class Meta:
#         model = Author
#         fields = ['name', 'title', 'birth_date']
