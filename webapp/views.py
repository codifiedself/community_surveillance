# from django.views.generic import CreateView
from .forms import NgoForm
# from django.views.generic.edit import FormView
from .models import *
from django.shortcuts import render, redirect

import json
from django.core.serializers.json import DjangoJSONEncoder

from django.db.models import Count, Sum


def ngo_create(request):
	if request.method == "POST":
		form = NgoForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'webapp/form_thankyou.html', {})
	else:
		form = NgoForm()

	return render(request, 'webapp/ngo_form.html',{'form': form})


def ngo_details(request):
	#create a dictionary which has State Name : { NGO COUNT : "", Districts : [list of districts with their name and NGO counts] }
	all_data = {}
	# states = State.objects.values('name').annotate(ngo_count=Count('ngo'), population_reach=SUM('population_reach') ).order_by('name')
	states = State.objects.values('name').annotate(ngo_count=Count('ngo'), population_reach=Sum('ngo__population_reach'), staff_count=Sum('ngo__staff_count')).order_by('name')


	for state in states:
		all_data[state['name']] = {'ngo_count':state['ngo_count'],'population_reach':state['population_reach'], 'staff_count':state['staff_count'], "districts" : []}


	districts = District.objects.values('name','state__name').annotate(ngo_count=Count('ngo'), population_reach=Sum('ngo__population_reach'), staff_count=Sum('ngo__staff_count')).order_by('name')

	for district in districts:
		if(district['state__name']):
			all_data[district['state__name']]['districts'].append([district['name'], district['ngo_count'], district['population_reach'], district['staff_count']])

	print(all_data)

	return render(request, 'webapp/ngo_details.html', {'all_data' : all_data})


def supplies_estimator(request):
	comm_list = Commodity.objects.all()
	options = [[x.name, x.quantity,  x.unit, x.price] for x in comm_list]
	commodities = json.dumps(options, cls=DjangoJSONEncoder)
	return render(request, 'webapp/supplies_estimator.html',{'commodities': commodities})



