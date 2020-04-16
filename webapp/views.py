# from django.views.generic import CreateView
from .forms import *
# from django.views.generic.edit import FormView
from .models import *
from django.shortcuts import render, redirect

import json
from django.core.serializers.json import DjangoJSONEncoder

from django.db.models import Count, Sum

from django.forms.models import modelformset_factory
from django.utils import translation


def index(request):
	return render(request, 'webapp/index.html', {})


def select_language_for_form(request):
	langs = [
		["English", "en-us"], 
		["हिन्दी (Hindi)", "hi"], 
		["ಕನ್ನಡ (Kannada)", "kn"], 
		["বাংলা (Bengali)","bn"],
		# ["தமிழ் (Tamil)","ta"],
		["മലയാളം (Malayalam)","ml"],  
		# ["தெலுங்கு (Telugu)","te"],  
	]
	return render(request, 'webapp/select_language_for_form.html',{"langs": langs})



def ngo_create(request):
	if request.method == "POST":
		form = NgoForm(request.POST)
		if form.is_valid():
			ngo = form.save()
			# return render(request, 'webapp/ngo_district_form.html', {})
			return redirect("/ngo_district_list_and_form/?ngo_id="+str(ngo.pk)) 
	else:
		lang = request.GET.get('lang')
		if lang:
			translation.activate(lang)
		else:
			translation.activate('en-us')

		form = NgoForm()

	return render(request, 'webapp/ngo_form.html',{'form': form})


def ngo_district_list_and_form(request):
	NgoDistrictFormSet = modelformset_factory(NgoDistrict, form=NgoDistrictForm)     
	
	if request.method == 'POST':
		formset = NgoDistrictFormSet(request.POST, request.FILES)
		ngo_id = request.GET.get('ngo_id')
		if formset.is_valid():
			instances = formset.save(commit=False)
			for instance in instances:
				instance.ngo_id = ngo_id
			# do something with the formset.cleaned_data
				instance.save()
			return render(request, 'webapp/form_thankyou.html',{})

	else:
		ngo_id = request.GET.get('ngo_id')

		operational_states = Ngo.objects.get(pk=ngo_id).operational_states.all()

		        # form.base_fields['local_categories'].queryset = LocalStoryCategory.\
          #   objects.filter(office=request.user.profile.office)

		formset = NgoDistrictFormSet(initial=[{'ngo_id':ngo_id}], queryset=NgoDistrict.objects.none())

		for form in formset:
			form.fields['district'].queryset = District.objects.filter(state__in = operational_states)
		# formset.base_fields['district'].queryset = 

	return render(request, 'webapp/ngo_district_list_and_form.html',{'formset': formset, 'ngo_id': ngo_id})



def ngo_details(request):
	#create a dictionary which has State Name : { NGO COUNT : "", Districts : [list of districts with their name and NGO counts] }
	all_data = {}

	states = State.objects.values('name').annotate(ngo_count=Count('ngo'), staff_count=Sum('ngo__staff_count')).order_by('name')


	for state in states:
		state_population_reach = 0 #if state['population_reach'] is None else state['population_reach']
		staff_count_staff_count =  0 if state['staff_count'] is None else state['staff_count']

		all_data[state['name']] = {'ngo_count':state['ngo_count'],'population_reach':state_population_reach, 'staff_count':staff_count_staff_count, "districts" : []}


	districts = District.objects.values('name','state__name').annotate(ngo_count=Count('ngo'), population_reach=Sum('ngodistrict__population_reach'), staff_count=Sum('ngo__staff_count')).order_by('name')

	for district in districts:
		district_population_reach = 0 if district['population_reach'] is None else district['population_reach']
		district_count_staff_count =  0 if district['staff_count'] is None else district['staff_count']

		if(district['state__name']):
			all_data[district['state__name']]['districts'].append([district['name'], district['ngo_count'], district['population_reach'], district['staff_count']])

	# print(all_data)

	return render(request, 'webapp/ngo_details.html', {'all_data' : all_data})


# def supplies_estimator(request):
# 	comm_list = Commodity.objects.all()
# 	options = [[x.name, x.quantity,  x.unit, x.price] for x in comm_list]
# 	commodities = json.dumps(options, cls=DjangoJSONEncoder)
# 	return render(request, 'webapp/supplies_estimator.html',{'commodities': commodities})



