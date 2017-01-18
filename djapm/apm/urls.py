'''
Created on Nov 17, 2016

@author: Atul Sharma
'''

from django.conf.urls import url
from . import views
from views import CompanyRegisterationView
from appusers import *
from userdashboard import *
from projectview import *

urlpatterns = [
               url(r'^$',views.index,name='home'),
               url(r'^company/register$',CompanyRegisterationView.as_view(),name='company_registration'),
               url(r'^company/checkemail',views.validate_email,name='check_email'),
               url(r'^company/checksubdomain',views.validate_checkdomain,name='check_subdomain'),
               url(r'^user/signin',UserSignIn.signin,name='user_signin'),
               url(r'^user/dashboard',UserDashboardView.as_view(),name='user_dashboard'),
               url(r'^user/signout',UserSignIn.signout,name='user_signout'),
               url(r'^project/add$',ProjectView.as_view(),name='add_project'),
               url(r'^project/viewproject$',ViewProject.as_view(),name='view_project'),
               url(r'^project/addestimatetoproj$',AddEstimation.as_view(),name='addestimatetoproj'),
               url(r'^project/editestimatetoproj$',EditEstimation.as_view(),name='editestimatetoproj'),
               url(r'^project/allestimatetoproj$',AllEstimation.as_view(),name='allestimatetoproj'),
               url(r'^project/backlog$',AllBacklog.as_view(),name='backlog'),
                             
               ]