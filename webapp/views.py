# from django.views.generic import CreateView
from .forms import *
# from django.views.generic.edit import FormView
from .models import *
from django.shortcuts import render, redirect

import json
from django.core.serializers.json import DjangoJSONEncoder

from django.db.models import Count, Sum
from django.db import transaction
from django.contrib import messages

def index(request):
	return render(request, 'webapp/index.html', {})


def ngo_create(request):
	if request.method == "POST":
		form = NgoForm(request.POST)
		ngo_district_form = NgoDistrictFormSet(request.POST, request.FILES)
		with transaction.atomic():
			print("got here 1")
			if form.is_valid():
				print("got here 2")
				ngo = form.save()
				if ngo_district_form.is_valid():
					print("got here 3")
					ngo_district_form.instance = ngo
					ngo_district_form.save()

				return render(request, 'webapp/form_thankyou.html', {})
			else:
				messages.error(request, "Error")
	else:
		form = NgoForm()
		ngo_district_form = NgoDistrictFormSet()

	return render(request, 'webapp/ngo_form.html',{'form': form, 'ngo_district_form': ngo_district_form})


# class ListView(ListView):
# 	template_name = 'book-list.html'
# 	context_object_name = 'books'
# 	paginate_by = 10
# 	ordering = ['-created']

#     def get_queryset(self):
#         return Book.objects.filter(created_by=self.request.user)


def ngo_details(request):
	#create a dictionary which has State Name : { NGO COUNT : "", Districts : [list of districts with their name and NGO counts] }
	all_data = {}
	# states = State.objects.values('name').annotate(ngo_count=Count('ngo'), population_reach=SUM('population_reach') ).order_by('name')
	states = State.objects.values('name').annotate(ngo_count=Count('ngo'), population_reach=Sum('ngo__population_reach'), staff_count=Sum('ngo__staff_count')).order_by('name')


	for state in states:
		state_population_reach = 0 if state['population_reach'] is None else state['population_reach']
		staff_count_staff_count =  0 if state['staff_count'] is None else state['staff_count']

		all_data[state['name']] = {'ngo_count':state['ngo_count'],'population_reach':state_population_reach, 'staff_count':staff_count_staff_count, "districts" : []}


	districts = District.objects.values('name','state__name').annotate(ngo_count=Count('ngo'), population_reach=Sum('ngo__population_reach'), staff_count=Sum('ngo__staff_count')).order_by('name')

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



