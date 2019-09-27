# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# from django.template import loader
from django.urls import reverse 
from django.views import generic

from potluck import models as potluck_models
import json

class IndexView(generic.TemplateView):
	template_name = 'index.html'

	def get_potluckItem(self):
		try:
			obj = potluck_models.PotluckItem.objects.order_by('-pub_date')
		except potluck_models.PotluckItem.DoesNotExist:
			raise Http404('PotluckItem not found!')
		return obj

	def get_context_data(self, **kwargs):
		kwargs['potluck_items'] = self.get_potluckItem()
		if 'user_form' not in kwargs:
			kwargs['user_form'] = potluck_models.UserForm(self.request.GET or None)
		if 'potluck_form' not in kwargs:
			kwargs['potluck_form'] = potluck_models.PotluckItemForm(self.request.GET or None)
		return kwargs

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, self.get_context_data())

	def post(self, request, *args, **kwargs):
		ctxt = {}
		if 'potluckitem' in request.POST:
			potluck_form = potluck_models.PotluckItemForm(request.POST)
			user_form = potluck_models.UserForm()
			if potluck_form.is_valid():
				potluck_form.save()
				potluck_form = potluck_models.PotluckItemForm()
				ctxt['potluck_form'] = potluck_form
				return HttpResponseRedirect('/')
			else:
				ctxt['potluck_form'] = potluck_form
		if 'deletePotluckitem' in request.POST:
			itemDict = dict(request.POST.iterlists())
			itemID = itemDict['deletePotluckitem'][0]
			potluck_form = potluck_models.PotluckItemForm(request.POST)
			self.delete(request, itemID, *args, **kwargs)
			ctxt['potluck_form'] = potluck_form
		return render(request, self.template_name, self.get_context_data(**ctxt))

	def delete(self, request, potluck_id, *args, **kwargs):
		if 'deletePotluckitem' in request.POST:
			potluck_item = get_object_or_404(potluck_models.PotluckItem, pk=potluck_id)
			potluck_item.delete()


class PotluckFormView(generic.FormView):
	form_class = potluck_models.PotluckItemForm
	template_name = 'index.html'
	success_url = '/'

	def post(self, request, *args, **kwargs):
		potluck_form = self.form_class(request.POST)
		user_form = potluck_models.UserForm()
		if potluck_form.is_valid():
			potluck_form.save()
			return self.render_to_response(self.get_context_data(success=True))
		else:
			return self.render_to_response(self.get_context_data(user_form=user_form,potluck_form=potluck_form))
		# return render(request, 'index.html', {'potluck_form':potluck_form, 'submitted': submitted})

class UserFormView(generic.FormView):
	form_class = potluck_models.UserForm
	template_name = 'index.html'
	success_url = '/'

	def post(self, request, *args, **kwargs):
		user_form = self.form_class(request.POST or None)
		potluck_form = potluck_modelsPotLuckItemForm()
		if user_form.is_valid():
			user_form.save()
			return self.render_to_response(self.get_context_data(success=True))
		else:
			return self.render_to_response(self.get_context_data(user_form=user_form, potluck_form=potluck_form))
		# return render(request, 'index.html', {'potluck_form':potluck_form, 'submitted': submitted})