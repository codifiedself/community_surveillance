# from django.db import models
from django.forms import ModelForm
# from django.forms.widgets import TypedChoiceField
from django_select2.forms import ModelSelect2MultipleWidget
from .models import Ngo, State, District, Taluk
from django import forms


class NgoForm(ModelForm):
    
    class Meta:
        model = Ngo
        fields = ('name', 'primary_contact', 'email', 'phone',  'work_area', 'operational_level', 'operational_states', 'operational_districts', 'operational_taluks', 
    	'is_govt_funded', 'govt_programs_contributed_to', 'govt_programs_partnered_with', 'population_reach', 'medium_of_reach', 'staff_details',
    	'does_staff_use_phones', 'staff_languages', 'pincode')
        widgets = {
        	'operational_states': ModelSelect2MultipleWidget(model=State,
        												search_fields=['name__icontains'],
														attrs={'data-placeholder': 'Write the name of the state. You can select multiple.'} 
                    								),
        	'operational_districts': ModelSelect2MultipleWidget(model=District,
        												search_fields=['name__icontains'],
														attrs={'data-placeholder': 'Write the name of the state. You can select multiple.'} 
                    								),
        	'operational_taluks': ModelSelect2MultipleWidget(model=Taluk,
        												search_fields=['name__icontains'],
														attrs={'data-placeholder': 'Write the name of the state. You can select multiple.'} 
                    								),
        	# 'is_govt_funded': forms.RadioSelect(choices=[
         #    	(True, 'Yes'),
         #    	(False, 'No')             
        	# ])
        }
        labels = {
            'name': 'Name of the Organization',
            'primary_contact': 'Name of Primary Contact of the Organization',
            'email': 'Email Id',
            'phone': 'Contact Phone Number',
            'work_area': 'Area of work of the organization',
            'operational_level': 'At what level, does your organization carry out implementation activities?',
            'operational_states': 'In which states or union territories does your organization carry out implementation activities?',
            'operational_districts': 'Please list all districts in which your organization has been carrying out implementation activities.',
            'operational_taluks': 'Please list all taluks in which your organization has been carrying out implementation activities.',
            'is_govt_funded': 'Select this checkbox if your project receives funding or other resources from national or state government?',
            'govt_programs_contributed_to': 'Does your project contribute to the objectives of any government programs? If so, please name the programs, adding if they are state-specific or district-level programs. (For example, if you have your cadre of frontline health workers, training government functionaries, providing community outreach support, community monitoring etc.)',
            'govt_programs_partnered_with': 'Does your project work in partnership with any government programs? If so, please name the programs. (Partnership means you have a formal MoU with the Government or relevant department, and you support in program implementation)',
            'population_reach': 'Please share the direct population reach of your organization on the ground',
            'medium_of_reach': 'For the people you can reach, can you reach them in-person only or also remotely (via phones)',
            'staff_details': 'How many ground-level, frontline staff do you have? (field staff, community outreach workers,  community volunteers)',
            'does_staff_use_phones': 'Does your team use mobile phones/tablets and internet services for day to day project operations? ',
            'staff_languages': 'What languages does your team speak, read and write it? (List All)',
            'pincode': 'Please provide the postal pincoode of your Organization'


        }
        help_texts = {
            # 'name': _('Some useful help text.'),
            'work_area': 'Eg. Health, Education, Nutrition, Disability, WASH, Livelihoods, Financial Services etc',
            'operational_level': 'Select one option: State, District, Block, City, Taluk/Tehsil or Other',
            'operational_states': 'If your organization is operational is in multiple states, select multiple',
            'operational_districts': 'If your organization is operational is in multiple districts, select multiple',
            'operational_taluks': 'If your organization is operational is in multiple taluks, select multiple',
            'is_govt_funded': 'This refers to funding, in-kind contributions, etc.'
        }
        error_messages = {
            # 'name': {
            #     'max_length': _("This writer's name is too long."),
            # },
        }




