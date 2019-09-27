# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime 
from django.utils import timezone
from django import forms
from django.forms import ModelForm, Textarea, CharField

#model classes
class PotluckItem(models.Model):
	potluckItem_text = models.CharField(max_length=200, default="I.E. Canopy or 2x Dog Collar(s)", blank=True)
	user_name = models.CharField(max_length=20, default="")
	dog_name = models.CharField(max_length=20, default="", blank=True)
	raffle_participation = models.BooleanField(default=False)
	pub_date = models.DateTimeField(auto_now_add=True, blank=True)
	additional_message = models.CharField(max_length=1000, default='', blank=True)
	
	def __str__(self):
		return self.potluckItem_text

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

class User(models.Model):
	potluck_item = models.ForeignKey(PotluckItem, on_delete=models.CASCADE)
	user_name = models.CharField(max_length=20, default="anonymous")

	def __str__(self):
		return self.user_name

#form classes
class PotluckItemForm(forms.ModelForm):
	class Meta:
		model = PotluckItem
		fields = ['user_name', 'dog_name', 'raffle_participation', 'potluckItem_text', 'additional_message']
		widgets = {
			'additional_message' : Textarea,
		}
		labels = {
			'user_name' : 'Name of Person/People Attending',
			'dog_name' : "Name(s) of the Dog(s) Coming (not required)",
			'additional_message': "Additional Message (not required), i.e further detail about what you are bringing",
			'potluckItem_text' : 'Potluck Item(s) you are Bringing',
			'raffle_participation': "Will you be bringing anything for the raffle?"
		}


class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['user_name']

		############################
		############################
		############################

# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField(auto_now_add=True, blank=True)
	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text