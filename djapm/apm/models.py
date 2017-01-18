from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template.defaultfilters import default
from django.core import serializers
import json



def GetItemsInJson(table,projectID):
        data_list=[]
        project_data=Project.objects.get(id = projectID) 
        table_data=table.objects.filter(fk_project = project_data)
        for d in table_data:
            data = serializers.serialize('json', [d])
            struct = json.loads(data)
            data_list.append(struct[0]['fields'])
            
        return data_list
       

# Create your models here.

class Tenant(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    subdomain = models.CharField(max_length=100, default=None)
    
    def getUserBySubdomain(self,sub):
        try:
            return Tenant.objects.get(subdomain=sub)
        except:
            return None
    

class Project(models.Model):
    project_name = models.CharField(max_length=250)
    project_category = models.CharField(max_length=100)
    project_description = models.TextField()
    project_createdDate = models.DateField(auto_now_add=True)
    project_startDate = models.DateField()
    project_endDate = models.DateField()
    project_assigned_to = models.ForeignKey(User)
    project_members = models.ManyToManyField(User,related_name='AllUsers')


class ProjectEstimationGuidelines(models.Model):
    task_complexity = models.CharField(max_length=100)
    task_complexity_point = models.IntegerField()
    task_estimated_efforts = models.BigIntegerField()
    fk_project = models.ForeignKey(Project)
    
    

#status
Status = [(1,"Open"), (2,"In Progress") ,(3, "Done") ,(4, "ReOpen"),(5, "Deferred"),(6, "Close")]

#release
class Release(models.Model):
    fk_project = models.ForeignKey(Project)
    releaseName = models.CharField(max_length=100)
    createdDate = models.DateTimeField(auto_now_add=True)
   # sprints = models.ForeignKey(Sprint,null=True,blank=True,default=None)
    releaseDate = models.DateField()


#for sprint
class Sprint(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    createdDate = models.DateTimeField(auto_now_add=True)
    startDate = models.DateField()
    endDate = models.DateField()
    fk_project = models.ForeignKey(Project)
    createdby = models.ForeignKey(User,null=True,blank=True,default=None)
    sprint_status = models.CharField(max_length=12,choices=Status,default=1)
    workinghours = models.CharField(max_length=100)
    release_key=models.ForeignKey(Release,null=True,blank=True,default=None)



    
#for userstory
class Backlog(models.Model):
    fk_project = models.ForeignKey(Project)
    user_story_status = models.CharField(max_length=12,choices=Status,default=1)
    sprintId = models.ForeignKey(Sprint,null=True, blank=True, default = None)
    storyDesc = models.CharField(max_length=1000)
    startDate = models.DateField(auto_now_add=True)
    roughEstimate = models.FloatField()
    priority = models.IntegerField()
    actual_effort=models.FloatField()
    backlog_name= models.CharField(max_length=100)
    assignee=models.ForeignKey(User,null=True, blank=True, default = None)
    created_by=models.CharField(max_length=1000,default=None)
  #  created_by=models.ForeignKey(User,related_name='%(class)s_requests_created',null=True, blank=True, default = None)
    

#issue_status
Issue_Status = [(1,"Pending"),(2,"In Progress"),(3,"Completed")]

#issue_type
Issue_Type = [(1,"User Story"),(2,"Task"),(3,"Subtask"),(4,"Bug")]

class Issue(models.Model):
    issue_title = models.CharField(max_length=100)
    issue_desc = models.CharField(max_length=1000)
    issue_type = models.CharField(max_length=100, choices=Issue_Type,default=1)
    issue_parent = models.CharField(max_length=100)
    issue_startDate = models.DateField(blank=True)
    issue_endDate = models.DateField(blank=True)
    issue_estimated_effort = models.FloatField(blank=True)
    issue_actual_effort = models.FloatField(blank=True)
    issue_assigned_to = models.ForeignKey(User, blank=True)
    issue_progress_status = models.CharField(max_length=100, choices=Issue_Status,default=1)
    issue_sprint = models.ForeignKey(Sprint)
    issue_project_id = models.ForeignKey(Project)
   
        








