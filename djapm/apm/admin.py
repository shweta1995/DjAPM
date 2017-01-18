from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Tenant)
admin.site.register(Project)
admin.site.register(ProjectEstimationGuidelines)
admin.site.register(Backlog)
admin.site.register(Sprint)
admin.site.register(Release)