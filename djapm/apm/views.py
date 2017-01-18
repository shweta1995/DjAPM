from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.template.backends.django import Template
from django.contrib.auth.models import User, Group
import json
from models import Tenant
def index(request):
    return HttpResponse(render(request,'apm/landing-bright.html'))
def validate_email(request):
        try:
            usrObj = User.objects.get(email=request.GET.get('email'))
        except:
            return HttpResponse(json.dumps(True))
        return HttpResponse(json.dumps(False))
def validate_checkdomain(request):
        TenantObj = Tenant().getUserBySubdomain(request.GET.get('company_domain'))
        if TenantObj == None:
            return HttpResponse(json.dumps(True))
        return HttpResponse(json.dumps(False))
class CompanyRegisterationView(View):
    
    
    def get(self,request):
        pass
    def post(self,request):
        form_data = request.POST
        username = form_data['email'].split('@')[0]
        email = form_data['email']
        company_name = form_data['company_name']
        subdomain = form_data['company_domain']
        
        g = Group.objects.get(name="Admin")
        
        new_user = User.objects.create_user(username,email,password='default123')
        try:
            Tenant_info = Tenant.objects.create(user=new_user,company_name=company_name,subdomain=subdomain)
        except:
            new_user.delete()
        
        
        new_user.groups.add(g)
        new_user.save()
        return HttpResponse('User created successfully')