'''
Created on Dec 2, 2016

@author: Atul Sharma
'''
from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http.response import HttpResponseForbidden, HttpResponse

class UserDashboardView(LoginRequiredMixin,UserPassesTestMixin,View):
    
    PERMITTED_GROUP = "Admin"
     
    def test_func(self):
        return self.request.user.groups.filter(name=self.PERMITTED_GROUP).exists()
    
    def get(self,request):
        return render(request,'apm/apm-user-dashboard.html')
    def post(self,request):pass