# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from .models import book
from rest_framework  import viewsets # Act as controller (enables us to CRUD)
from .serializer import BookSerializer
from rest_framework import generics, permissions

from django.views.generic import TemplateView

from rest_framework.response import Response

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
# Create your views here.

def home(request):
	return render(request, 'index.html')  


class BookViewSet(viewsets.ModelViewSet):
	queryset = book.objects.all() # will fetch all
	serializer_class = BookSerializer

class Index(TemplateView):
	def get(self, request, *args, **kwargs):
		return HttpResponse('Empty Page')

class Register(generics.CreateAPIView):
	def post(self, request, *args, **kwargs):
		#creating new user
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')
		name = request.POST.get('name')
		blood_type = request.POST.get('blood_type')
		rhesus_factor = request.POST.get('rhesus_factor')
		gender = request.POST.get('gender')
		first_time_donor = request.POST.get('first_time_donor')
		age = request.POST.get('age')
		current_location = request.POST.get('current_location')


		user = User.objects.create_user(username, email, password)
		user.name = name
		user.blood_type = blood_type
		user.rhesus_factor = rhesus_factor
		user.gender = gender
		user.first_time_donor = first_time_donor
		user.age = age
		user.current_location = current_location

		user.save()

		#Generating authentication token for the user 
		token = Token.objects.objects.create(user = user)

		return Response({'detail': 'user has been created with token '+ token.key})


