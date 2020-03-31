# from django.views.generic import CreateView
from .forms import NgoForm
# from django.views.generic.edit import FormView
from .models import Ngo, Commodity
from django.shortcuts import render, redirect

import json
from django.core.serializers.json import DjangoJSONEncoder


def ngo_create(request):
	if request.method == "POST":
		form = NgoForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'webapp/form_thankyou.html', {})
	else:
		form = NgoForm()

	return render(request, 'webapp/ngo_form.html',{'form': form})

def supplies_estimator(request):
	comm_list = Commodity.objects.all()
	options = [[x.name, x.quantity,  x.unit, x.price] for x in comm_list]
	commodities = json.dumps(options, cls=DjangoJSONEncoder)
	return render(request, 'webapp/supplies_estimator.html',{'commodities': commodities})

