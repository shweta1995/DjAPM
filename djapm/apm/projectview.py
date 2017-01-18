'''
Created on Dec 5, 2016

@author: Atul Sharma
'''
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.http.response import HttpResponse
from models import Project,ProjectEstimationGuidelines,GetItemsInJson,Sprint,Backlog
import datetime
from django.shortcuts import render_to_response
import json
from django.template import RequestContext
from django.contrib.auth.models import User
from django.core import serializers


class ProjectView(LoginRequiredMixin,UserPassesTestMixin,View):
    permission_required = 'apm.add_project'
    def test_func(self):
        return self.request.user.has_perm('apm.add_project')
    def get(self,request):
        return render(request,'apm/apm-add-project.html')
    def post(self,request):
        name = request.POST.get('proj_name')
        des = request.POST.get('proj_desc')
        startdate = request.POST.get('proj_start')
        enddate = request.POST.get('proj_end')
        
        newpro = Project()
        newpro.project_name = name
        newpro.project_description = des
        
        st_dt = datetime.datetime.strptime(startdate,'%m/%d/%Y').strftime('%Y-%m-%d')
        newpro.project_startDate = datetime.datetime.strptime(st_dt,'%Y-%m-%d').date()
        
        ed_dt = datetime.datetime.strptime(enddate,'%m/%d/%Y').strftime('%Y-%m-%d')
        newpro.project_endDate = datetime.datetime.strptime(ed_dt,'%Y-%m-%d').date()
        
        newpro.project_assigned_to = request.user
#         newpro.project_members.add(request.user)
        newpro.save()
        

    
        #for estimations
#         
#         estimate=ProjectEstimationGuidelines()
#         estimate.fk_project=newpro
#         estimate.task_complexity="Very Simple"
#         estimate.task_complexity_point= 1
#         estimate.task_estimated_efforts= 1.0
#         estimate.save()
#         
#         estimate = ProjectEstimationGuidelines()
#         estimate.fk_project=newpro
#         estimate.task_complexity="Simple"
#         estimate.task_complexity_point= 1
#         estimate.task_estimated_efforts= 1.0
#         estimate.save()
#         
#         estimate = ProjectEstimationGuidelines()
#         estimate.fk_project=newpro
#         estimate.task_complexity ="Medium"
#         estimate.task_complexity_point= 1
#         estimate.task_estimated_efforts= 1.0
#         estimate.save()
#         
#         estimate = ProjectEstimationGuidelines()
#         estimate.fk_project=newpro
#         estimate.task_complexity="Complex"
#         estimate.task_complexity_point= 1
#         estimate.task_estimated_efforts= 1.0
#         estimate.save()
#         
#         estimate = ProjectEstimationGuidelines()
#         estimate.fk_project=newpro
#         estimate.task_complexity="Very Complex"
#         estimate.task_complexity_point= 1
#         estimate.task_estimated_efforts= 1.0
#         estimate.save()
        
        return HttpResponse(newpro.id)
       # return HttpResponse('dhfgsdh')

class ViewProject(LoginRequiredMixin,UserPassesTestMixin,View):
    permission_required = 'apm.view_project'
    def test_func(self):
        return self.request.user.has_perm('apm.view_project')
    def get(self,request):
        projectid=request.GET.get('proj_id')
        
        project_data=Project.objects.get(id = projectid)
        estimate=ProjectEstimationGuidelines.objects.filter(fk_project = project_data)
        
        return render(request, 'apm/viewproject.html', {"project":project_data,'estimation':estimate,'project_id':project_data.id})
   
   

    
class AddEstimation(View):
    permission_required = 'apm.addestimatetoproj'
    def test_func(self):
        return self.request.user.has_perm('apm.addestimatetoproj')
   
    def post(self,request):
       
        projid = request.POST.get('projid')
        project=Project.objects.get(id=projid)
     
        complexity = request.POST.get("name")
        points = request.POST.get("pts")
        efforts   = request.POST.get("eff")     
        
        estimate = ProjectEstimationGuidelines()
        estimate.fk_project=project
        estimate.task_complexity=complexity
        estimate.task_complexity_point= int(points)
        estimate.task_estimated_efforts= float(efforts)

        estimate.save()
#         data = {}
#         data['id'] = estimate.id
#         data['projectid'] = projid
#         data['estimationLevel'] = estimate.task_complexity
#         data['estimationPoint'] = estimate.task_complexity_point
#         data['estimationHours'] = estimate.task_estimated_efforts
#         
        return HttpResponse('true')


class EditEstimation(View):
    permission_required = 'apm.editestimatetoproj'
    def test_func(self):
        return self.request.user.has_perm('apm.editestimatetoproj')
   
    def post(self,request):
        estimateid=request.POST.get('estimate_id')
        estimate=ProjectEstimationGuidelines.objects.get(id=estimateid)
        
        projid = request.POST.get('projid')
        project=Project.objects.get(id=projid)
     
        complexity = request.POST.get("new_name")
        points = request.POST.get("pts")
        efforts   = request.POST.get("eff")     
        
        estimate.fk_project=project
        estimate.task_complexity=complexity
        estimate.task_complexity_point= int(points)
        estimate.task_estimated_efforts= float(efforts)

        estimate.save()
        return HttpResponse('true')
    
class AllEstimation(View):   
    permission_required = 'apm.allestimatetoproj'
    def test_func(self):
        return self.request.user.has_perm('apm.allestimatetoproj')
    def get(self,request):
       
        projectid=request.GET.get('proj_id')
       
        
        data_list=[]
        project_data=Project.objects.get(id = projectid)
        table_data=ProjectEstimationGuidelines.objects.filter(fk_project = project_data)
    
       # d=GetItemsInJson(ProjectEstimationGuidelines,projectid)
        
        d=GetItemsInJson(Backlog,projectid)
      
        return HttpResponse(json.dumps(d))
 
    
#for Backlog
class AllBacklog(View):
    permission_required = 'apm.backlog'
    def test_func(self):
        return self.request.user.has_perm('apm.backlog')
    
    def get(self,request):
        projectid=request.GET.get('proj_id')
        data=GetItemsInJson(Backlog,projectid)
       
        project_data=Project.objects.get(id = projectid)
  
        return render(request, 'apm/apm-backlog-new.html', {"backlogjson":data,"project":project_data,'project_id':project_data.id})
   
      #  return render(request, 'apm/apm-backlog-new.html', {"project":project_data,'project_id':project_data.id})
   
   
    def post(self,request):
        
        backlog=Backlog()
        
        projectid=request.POST.get('projid')
        project_data=Project.objects.get(id = projectid)
        
        storyDesc = request.POST.get("description")
        roughEstimate = request.POST.get("rough_estimate")
        priority = int(request.POST.get("priority"))
        actual_effort= request.POST.get("actual_effort")
        backlog_name = request.POST.get("backlog_name")
        assignee=request.POST.get("assignee")
        sprint=request.POST.get("sprint")
        
        backlog.fk_project=project_data
        backlog.user_story_status=1
        
        
        if (sprint != 'None'):
            backlog.sprintId = Sprint.objects.get(id=sprint)
        else:
            backlog.sprintId =None
            
        backlog.storyDesc = storyDesc
        backlog.roughEstimate = roughEstimate
        backlog.priority = priority
        backlog.actual_effort= actual_effort
        backlog.backlog_name = backlog_name
        backlog.actual_effort = float(0.0)
        backlog.created_by= 'None'
        
        if(assignee != 'None'):
            backlog.assignee = User.objects.get(id=assignee)
        else:
            backlog.assignee=None
        
        backlog.save()

        
        return HttpResponse('true')
    
    
class EditBacklog(View):
    permission_required = 'apm.editbacklog'
    def test_func(self):
        return self.request.user.has_perm('apm.editbacklog')
   
    def post(self,request):
        backlogid=request.POST.get('backlog_id')
        backlog=Backlog.objects.get(id=backlogid)
        
        backlog=Backlog()
        
        projectid=request.POST.get('projid')
        project_data=Project.objects.get(id = projectid)
        
        storyDesc = request.POST.get("description")
        roughEstimate = request.POST.get("rough_estimate")
        priority = int(request.POST.get("priority"))
        actual_effort= request.POST.get("actual_effort")
        backlog_name = request.POST.get("backlog_name")
        assignee=request.POST.get("assignee")
        sprint=request.POST.get("sprint")
        
        backlog.fk_project=project_data
        backlog.user_story_status=1
        
        
        if (sprint != 'None'):
            backlog.sprintId = Sprint.objects.get(id=sprint)
        else:
            backlog.sprintId =None
            
        backlog.storyDesc = storyDesc
        backlog.roughEstimate = roughEstimate
        backlog.priority = priority
        backlog.actual_effort= actual_effort
        backlog.backlog_name = backlog_name
        backlog.actual_effort = float(0.0)
        backlog.created_by= 'None'
        
        if(assignee != 'None'):
            backlog.assignee = User.objects.get(id=assignee)
        else:
            backlog.assignee=None
        
        backlog.save()

        
        return HttpResponse('true')
    
    
        
    
