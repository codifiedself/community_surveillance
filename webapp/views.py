# from django.views.generic import CreateView
from .forms import NgoForm
# from django.views.generic.edit import FormView
from .models import Ngo
from django.shortcuts import render, redirect


def ngo_create(request):
	if request.method == "POST":
		form = NgoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('ngo_create')
	else:
		form = NgoForm()

	return render(request, 'webapp/ngo_form.html',{'form': form})








