# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import (

   AbstractBaseUser,
   BaseUserManager

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

#our model manager
class UserManager(BaseUserManager):
	#takes in all the required fields
	def create_user(self,email, password=None, is_admin = False):
		if not email:
			raise ValueError("User must have an email address")
		if not password:
			raise ValueError("User must have a password ")
		user_obj = self.model(
		email= self.normalize_email(email)
		)	
		user_obj.set_password(password)
		user_obj.admin = is_admin
		user_obj.save(using = self.db)
		return user_obj

	def create_donoruser(self, email, password = None):
		user= self.create_user(
                  email,
                  password = password,
                  is_admin = False
			)
		return user

	def create_superuser(self, email, password = None):
		user= self.create_user(
                  email,
                  password = password,
                  is_admin = True

			)
		return user





class User(AbstractBaseUser):
	email = models.EmailField(max_length = 255, unique = True)
	full_name = models.CharField(max_length = 255, blank= True , null= True)
	blood_type = models.CharField(max_length = 2)
	rhesus_factor = models.BooleanField(default = False)
	gender = models.CharField(max_length = 10)
	first_time_donor = models.BooleanField(default = False) # may need to adjust this
	age = models.IntegerField(null= True)
	current_location = models.IntegerField(null= True)
	admin = models.BooleanField(default = False )
	weight = models.IntegerField(null= True)

	active = models.BooleanField(default = True)
	staff = models.BooleanField(default = True)
	


	USERNAME_FIELD = 'email'
	# USERNAME_FIELD and password field are required by default 
	REQUIRED_FIELDS = [] #'name','blood_type','rhesus_factor','gender','gender','age','current_location','weight'] #python manage.py createsuperuser will go off of this
	objects = UserManager()	

	#supporting methods

	def __str__(self):
		return self.email

	def get_full_name(self):
		return self.name

	def get_blood_type(self):
		return self.blood_type

    # Rhesus is either  
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

	def is_first_time(self):
		return self.first_time_donor

	def rhesus(self):
		return self.rhesus

		#built in must be included
	def has_perm (self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	def get_full_name(self):
		return self.full_name

	def get_short_name (self):
		return self.email
		

	@property
	def is_admin(self):
		return self.admin

	@property
	def is_active(self):
		return self.admin

	@property
	def is_staff(self):
		return self.staff



# extending the user model/ may choose to a profiles app all together. 
# class UserProfile(models.Model):
	#user = models.OneToOneField(Donor)  #Foreign key 
	# Extend extra data here
