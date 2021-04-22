from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import render
import csv
from cdacalumini.models import Job,Apply_job
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
from django.utils import timezone

# Create your views here.
def tpo(request):
	if (request.user.username=='cdac'):
		countd = 0
		counta = 0
		today = timezone.now()
		t = today.date()

		obj_list = Job.objects.all().order_by('-id')
		for o in obj_list:
			if o.Deadline < t:
				countd = countd+1
			else:
				counta = counta+1
		return render(request, 'tpojobs.html', {"obj_list": obj_list,'dead':countd,'totalj':len(obj_list),'active':counta})

	else:
		return redirect('/login')

def deadjob(request):
	if (request.user.username=='cdac'):
		countd = 0
		counta = 0
		dead_list=[]
		today = timezone.now()
		t = today.date()

		obj_list = Job.objects.all().order_by('-id')
		for o in obj_list:
			if o.Deadline < t:
				countd = countd + 1
				dead_list.append(o)
			else:
				counta = counta + 1
		return render(request, 'tpojobs.html',{"obj_list": dead_list, 'dead': countd, 'totalj': len(obj_list), 'active': counta})
	else:
		return redirect('/login')

def activejob(request):
	countd = 0
	counta = 0
	active_list=[]
	today = timezone.now()
	t = today.date()

	obj_list = Job.objects.all().order_by('-id')
	for o in obj_list:
		if o.Deadline < t:
			countd = countd + 1

		else:
			counta = counta + 1
			active_list.append(o)
	return render(request, 'tpojobs.html',{"obj_list": active_list, 'dead': countd, 'totalj': len(obj_list), 'active': counta})








def detail(request,id=None):
    instance = get_object_or_404(Job, id=id)
    return render(request,'fortpo/detail.html',{'instance':instance})

def getcsv(request,id=None):
	instance=get_object_or_404(Job,id=id)
	response=HttpResponse(content_type='text/csv')
	response['Content-Disposition']='attachment;filename="Data.csv"'
	candidates=Apply_job.objects.all().filter(Q(Company_name__icontains=instance.Company_name) and Q(Job_title__icontains=instance.Job_title))
	writer=csv.writer(response)
	writer.writerow(['Candidate Id','Candidate Name','Candidate Email','Candidate Mobile No.','Date of Apply','Company Name'])
	for candidate in candidates:
		writer.writerow([candidate.id,candidate.user,candidate.Email_apply,candidate.Mobile_no,candidate.Apply_date,candidate.Company_name])
	return response

