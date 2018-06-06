# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import (

   AbstractBaseUser

	)

# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length = 200)
	body = models.TextField(max_length = 200)
	def __unicode__(self):
		return self.title


class book(models.Model):
	title = models.CharField(max_length = 200)
	author = models.CharField(max_length = 200)

	def __unicode__(self):
		return self.title

# For the registration table, this user model should not be changed , may bring complications

class Donor(AbstractBaseUser):
	email = models.EmailField(max_length = 30, unique = True)
	name = models.CharField(max_length = 30, blank= True , null= True)
	blood_type = models.CharField(max_length = 2)
	rhesus_factor = models.BooleanField()
	gender = models.CharField(max_length = 10)
	first_time_donor = models.BooleanField(default = False) # may need to adjust this
	age = models.IntegerField()
	current_location = models.IntegerField()
	


	USERNAME_FIELD = 'email'
	# USERNAME_FIELD and password field are required by default 
	REQUIRED_FIELDS = ['name','blood_type','rhesus_factor','gender','first_time_donor','gender','age','current_location'] #python manage.py createsuperuser will go off of this


	#supporting methods

	def __str__(self):
		return self.email

	def get_full_name(self):
		return self.name

	def get_blood_type(self):
		return self.blood_type

	def get_rhesus(self):
		return self.rhesus_factor

	def get_gender(self):
		return self.gender

	def get_is_first(self):
		return self.first_time_donor

	def get_age(self):
		return self.age

	def get_curr_loc(self):
		return self.current_location

	@property
	def is_first_time(self):
		return self.first_time_donor

	def rhesus(self):
		return self.rhesus


# extending the user model/ may choose to a profiles app all together. 
class UserProfile(models.Model):
	user = models.OneToOneField(Donor)  #Foreign key 
	# Extend extra data here
