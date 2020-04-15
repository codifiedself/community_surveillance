# from django.db import models
from django.forms import ModelForm, formset_factory, BaseModelFormSet
# from django.forms.widgets import TypedChoiceField
from django_select2.forms import ModelSelect2MultipleWidget
from .models import *
from django import forms

from django.utils.translation import ugettext_lazy as _





class NgoForm(ModelForm):
    
    class Meta:
        model = Ngo
        fields = ('name', 'primary_contact', 'email', 'phone',  'work_area', 'special_needs_groups', 'operational_level', 'operational_states', 
        	'medium_of_reach', 'staff_count', 'does_staff_use_phones')
    	# 'operational_taluks','is_govt_funded', 'govt_programs_contributed_to', 'govt_programs_partnered_with',   'staff_details'
        widgets = {
        	'operational_states': forms.CheckboxSelectMultiple(),
                    								
        	# 'operational_districts': ModelSelect2MultipleWidget(model=District,
        	# 											search_fields=['name__icontains'],
									# 					attrs={'data-placeholder': 'Write the name of the district. You can select multiple.'} 
         #            								),
            'medium_of_reach': forms.RadioSelect(),
            'does_staff_use_phones': forms.RadioSelect()
        	# 'operational_taluks': ModelSelect2MultipleWidget(model=Taluk,
        	# 											search_fields=['name__icontains'],
									# 					attrs={'data-placeholder': 'Write the name of the state. You can select multiple.'} 
         #            								),
        	# 'is_govt_funded': forms.RadioSelect(choices=[
         #    	(True, 'Yes'),
         #    	(False, 'No')             
        	# ])
        }
        labels = {
            'name': _('1. Name of the Organization'),
            'primary_contact': _('2. Name of Primary Contact of the Organization'),
            'email': _('3. Email Id'),
            'phone': _('4. Contact Phone Number'),
            'work_area': _('5. Area of work of the organization'),
            'special_needs_groups': _('6. Does your organization work with any special needs’ group? (Select as many as applies)'),
            'operational_level': _('7. At what level, does your organization carry out direct implementation activities?'),
            'operational_states': _('8. In which states or union territories does your organization carry out direct implementation activities? (If your organization is operational is in multiple states, select multiple)'),
            # 'operational_districts': '9. Please list all districts in which your organization has been carrying out direct implementation activities.',
            # 'operational_taluks': 'Please list all taluks in which your organization has been carrying out implementation activities.',
            # 'is_govt_funded': 'Select this checkbox if your project receives funding or other resources from national or state government?',
            # 'govt_programs_contributed_to': 'Does your project contribute to the objectives of any government programs? If so, please name the programs, adding if they are state-specific or district-level programs. (For example, if you have your cadre of frontline health workers, training government functionaries, providing community outreach support, community monitoring etc.)',
            # 'govt_programs_partnered_with': 'Does your project work in partnership with any government programs? If so, please name the programs. (Partnership means you have a formal MoU with the Government or relevant department, and you support in program implementation)',
            'population_reach': _('9. Please share the direct population reach of your organization on the ground'),
            'medium_of_reach': _('10. For the people you can reach, can you reach them in-person only or also remotely (via phones)'),
            'staff_count': _('11. How many ground-level, frontline staff do you have? (field staff, community outreach workers, community volunteers)'),
            'does_staff_use_phones': _('12. Does your team use mobile phones/tablets and internet services for day to day project operations? '),
            # 'staff_languages': '14. What languages does your team speak, read and write it? (List All)',
            # 'pincode': '14. Please provide the postal pin codes of your organization’s head quarter and all office locations from where you function (comma separated)'


        }
        help_texts = {
            # 'name': _('Some useful help text.'),
            # 'work_area': 'Eg. Health, Education, Nutrition, Disability, WASH, Livelihoods, Financial Services etc',
            # 'operational_level': 'Select one option: State, District, Block, City, Taluk/Tehsil or Other',
            # 'operational_states': 'If your organization is operational is in multiple states, select multiple',
            # 'operational_districts': 'If your organization is operational in multiple districts, select multiple',
            # 'operational_taluks': 'If your organization is operational is in multiple taluks, select multiple',
            # 'is_govt_funded': 'This refers to funding, in-kind contributions, etc.'
        }
        error_messages = {
            # 'name': {
            #     'max_length': _("This writer's name is too long."),
            # },
        }



class NgoDistrictForm(forms.ModelForm):

    class Meta:
        model = NgoDistrict
        fields = ('district', 'population_reach')
        widgets = {
            'population_reach': forms.RadioSelect()
        }
        labels = {
            'district': _('Enter or Search the District where you have reach'),
            'population_reach': _('Population reach in the selected District')
        }

    # def __init__(self, *args, **kwargs):
    #     super(NgoDistrictForm, self).__init__(*args, **kwargs)
    #     self.fields['district'].queryset = District.objects.filter(state__in = self.instance.ngo.operational_states)

        # widgets = {'ngo': forms.HiddenInput()}




       

