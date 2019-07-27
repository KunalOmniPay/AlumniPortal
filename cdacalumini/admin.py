from __future__ import unicode_literals

from django.contrib import admin

from .models import *



# Register your models here.
class skilladmin(admin.ModelAdmin):
    list_display=['skill','level','semail']

class sjobadmin(admin.ModelAdmin):
    list_display=['semail','profile','organisation']
class tech(admin.ModelAdmin):
    list_display = [
        'name',]
class Infoadmin(admin.ModelAdmin):
       list_display=[
           'First_name',
            'Last_name',
            'Email',
            'Role',
            'Technology',
            'Batch',
            'Mobile_no',
            'Gender',
            'City',
            'Profile_photo']

class Jobadmin(admin.ModelAdmin):
           list_display=[
               'Your_name',
               'Email',
               'Company_name',
               'Job_title',
               'Location',
               'Deadline',
               'Salary',
               'About_company',
               'About_role',

           ]

class Applyadmin(admin.ModelAdmin):
            list_display = [
                'Company_name',
                'Job_title',
                'Posted_by',
                'Email_post',
                'user',
                'Email_apply',
                'Apply_date',
                'Deadline',
                'resume',

            ]

admin.site.register(Info, Infoadmin),
admin.site.register(Job, Jobadmin),
admin.site.register(Apply_job, Applyadmin)
admin.site.register(Technology, tech)

admin.site.register(Profile)
admin.site.register(FriendRequest)

admin.site.register(Message)
admin.site.register(carousel)
admin.site.register(dir)
admin.site.register(testimonial)
admin.site.register(Con)
admin.site.register(Sjob,sjobadmin)
admin.site.register(Training)
admin.site.register(Skill,skilladmin)
admin.site.register(project)
admin.site.register(Intern)