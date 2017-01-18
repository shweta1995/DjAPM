'''
Created on Dec 1, 2016

@author: Atul Sharma
'''


from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from django.template.backends.django import Template
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate,login,logout
import json
from django.urls import reverse

class UserSignIn(View):
    def get(self,request):
        pass
    @classmethod
    def signin(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('user_dashboard'))
        else:
            return HttpResponse('User does not exist')
    @classmethod
    def signout(self,request):
        logout(request)
        return redirect(reverse('home'))