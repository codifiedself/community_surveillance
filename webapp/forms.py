# from django.db import models
from django.forms import ModelForm
# from django.forms.widgets import TypedChoiceField
from django_select2.forms import ModelSelect2MultipleWidget
from .models import *
from django import forms

from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, Row, HTML, ButtonHolder, Submit
from .custom_layout_object import *

import re




class NgoDistrictForm(forms.ModelForm):

    class Meta:
        model = NgoDistrict
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        formtag_prefix = re.sub('-[0-9]+$', '', kwargs.get('prefix', ''))

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Field('district'),
                Field('population_reach'),
                Field('DELETE'),
                css_class='formset_row-{}'.format(formtag_prefix)
            )
        )

NgoDistrictFormSet = inlineformset_factory(Ngo, NgoDistrict, form=NgoDistrictForm,
    fields=['district','population_reach'], extra=1, can_delete=True
    )


class NgoForm(ModelForm):
    
    class Meta:
        model = Ngo
        fields = ('name', 'primary_contact', 'email', 'phone',  'work_area', 'special_needs_groups', 'operational_level', 'operational_states', 'operational_districts', 
        	'population_reach', 'medium_of_reach', 'staff_count', 'does_staff_use_phones', 'pincode')
    	# 'operational_taluks','is_govt_funded', 'govt_programs_contributed_to', 'govt_programs_partnered_with',   'staff_details'
        widgets = {
        	# 'operational_states': ModelSelect2MultipleWidget(model=State,
        	# 											search_fields=['name__icontains'],
									# 					attrs={'data-placeholder': 'Write the name of the state. You can select multiple.'} 
         #            								),
            'operational_states': forms.CheckboxSelectMultiple(),
            # 'operational_districts': ManyToManyRawIdWidget(),

                # 'operational_districts': ModelSelect2MultipleWidget(model=District,
                # 											search_fields=['name__icontains'],
                # 											attrs={'data-placeholder': 'Write the name of the district. You can select multiple.'} 
                #     								),
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
            'name': '1. Name of the Organization',
            'primary_contact': '2. Name of Primary Contact of the Organization',
            'email': '3. Email Id',
            'phone': '4. Contact Phone Number',
            'work_area': '5. Area of work of the organization (Eg. Health, Education, Nutrition, Disability, WASH, Livelihoods, Financial Services etc)',
            'special_needs_groups': '6. Does your organization work with any special needs’ group? (Select as many as applies)',
            'operational_level': '7. At what level, does your organization carry out direct implementation activities?',
            'operational_states': '8. In which states or union territories does your organization carry out direct implementation activities?',
            'operational_districts': '9. Please list all districts in which your organization has been carrying out direct implementation activities.',
            # 'operational_taluks': 'Please list all taluks in which your organization has been carrying out implementation activities.',
            # 'is_govt_funded': 'Select this checkbox if your project receives funding or other resources from national or state government?',
            # 'govt_programs_contributed_to': 'Does your project contribute to the objectives of any government programs? If so, please name the programs, adding if they are state-specific or district-level programs. (For example, if you have your cadre of frontline health workers, training government functionaries, providing community outreach support, community monitoring etc.)',
            # 'govt_programs_partnered_with': 'Does your project work in partnership with any government programs? If so, please name the programs. (Partnership means you have a formal MoU with the Government or relevant department, and you support in program implementation)',
            'population_reach': '10. Please share the direct population reach of your organization on the ground',
            'medium_of_reach': '11. For the people you can reach, can you reach them in-person only or also remotely (via phones)',
            'staff_count': '12. How many ground-level, frontline staff do you have? (field staff, community outreach workers,  community volunteers)',
            'does_staff_use_phones': '13. Does your team use mobile phones/tablets and internet services for day to day project operations? ',
            # 'staff_languages': '14. What languages does your team speak, read and write it? (List All)',
            'pincode': '14. Please provide the postal pin codes of your organization’s head quarter and all office locations from where you function (comma separated)'


        }

        help_texts = {
            # 'name': _('Some useful help text.'),
            # 'work_area': 'Eg. Health, Education, Nutrition, Disability, WASH, Livelihoods, Financial Services etc',
            # 'operational_level': 'Select one option: State, District, Block, City, Taluk/Tehsil or Other',
            'operational_states': 'If your organization is operational is in multiple states, select multiple',
            'operational_districts': 'If your organization is operational in multiple districts, select multiple',
            # 'operational_taluks': 'If your organization is operational is in multiple taluks, select multiple',
            # 'is_govt_funded': 'This refers to funding, in-kind contributions, etc.'
        }
        error_messages = {
            # 'name': {
            #     'max_length': _("This writer's name is too long."),
            # },
        }


    def __init__(self, *args, **kwargs):
        super(NgoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('name'),
                Field('primary_contact'),
                Field('email'),
                Field('phone'),
                Field('work_area'),
                Field('special_needs_groups'),
                Field('operational_level'),
                Field('operational_states'),
                Fieldset('Add Districts', Formset('ngo_district_form')),
                Field('medium_of_reach'),
                Field('staff_count'),
                Field('does_staff_use_phones'),
                Field('pincode'),

                HTML("<br>"),
                ButtonHolder(Submit('submit', 'Save NGO')),
                )
            )

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['operational_districts'].queryset = District.objects.none()




