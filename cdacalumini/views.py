from __future__ import unicode_literals
from django.shortcuts import render
import csv
import io
from mailmerge import MailMerge
from django.http import JsonResponse
from django.core.urlresolvers import reverse



#from templated_docs import fill_template
#from templated_docs.http import FileResponse,Json

from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect,render_to_response
from django.core.mail import send_mail
from .models import Profile, FriendRequest
from django.conf import settings
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from .models import Info,Job,Apply_job,Message,carousel,Con,dir,testimonial
import string
from django.utils.text import slugify
import os
import datetime
from django.utils import timezone
from .forms import LoginForm, RegisterForm,messageform,eduedit,expertedit,picedit,contactedit
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)
User = get_user_model()
#change
from django.shortcuts import render
from .forms import *
from formtools.wizard.views import SessionWizardView

# Create your views here.
def home(request):
	r = 0
	s = 0
	countn = 0
	em = []
	rec = []
	p = []
	f = []
	l = []
	if request.user.is_authenticated:
		rec = FriendRequest.objects.all().filter(to_user=request.user).order_by('-timestamp')
		for i in range(0, len(rec)):
			b = get_object_or_404(Info, Email=rec[i].from_user.email)
			p.append(b.Profile_photo)
			f.append(b.First_name)
			l.append(b.Last_name)
		r = 1
		z = Info.objects.all()
		for i in range(0, len(z)):
			em.append(z[i].Email)
		if request.user.email in em:
			a = get_object_or_404(Info, Email=request.user.email)
			if a.valid == True:
				s = 1
		countn = rec.count()
	a = carousel.objects.all()
	d = dir.objects.all()
	test = testimonial.objects.all()

	list = zip(f, l, p)
	return render(request, "home.html",
				  {'a': a[0], 'd': d[0], 'tp': test, 'r': r, 's': s, 'rec': list, 'count': countn})
def about(request):
	r = 0
	z=1
	em=[]
	s=0
	if request.user.is_authenticated:
		r = 1
		n = Info.objects.all()
		for i in range(0, len(n)):
			em.append(n[i].Email)
		if request.user.email in em:
			a = get_object_or_404(Info, Email=request.user.email)
			if a.valid == True:
				s = 1
	return render(request,"about.html",{'r':r,'s':s,'z':z})


def register_c(request):
	if request.method=="GET":
		form = RegisterForm(request.POST or None)
		context = {
			'form': form
		}
		return render(request, 'registration1.html', context)

	if request.method=='POST':
			form = RegisterForm(request.POST or None)
			if form.is_valid():
				u=form.cleaned_data.get('username')
				if (any(c.isalpha() for c in u)==False):
					return redirect('/register')
				User = form.save(commit=False)
				email = form.cleaned_data.get('email')
				k = get_user_model().objects.all()
				e = []
				for i in range(0, len(k)):
					e.append(k[i].email)
				if email in e:
					return redirect('/registere')
				else:
					pwd = form.cleaned_data.get('password')
					c_pwd = form.cleaned_data.get('confirm_password')
					if pwd == c_pwd:
						User.set_password(pwd)
						User.save()
						subject2 = 'CDAC ALUMNI PORTAL'
						message2 = 'Thanks for registering.Now complete your profile to let let other know about you.'
						print('kunal')
						user = authenticate(username=User.username, password=pwd)
						try:
							login(request, User)
							send_mail(subject2, message2, settings.EMAIL_HOST_USER, [request.user.email])

							return redirect('/')
						except:
							return redirect('/registeru/')


					else:
						s = 1
						return redirect('/registerp')
			else:
				return redirect('/registeru')
			context = {
				'form': form
			}
			return render(request, 'registration1.html', context)


def register_p(request):
	if request.method=="GET":
		form = RegisterForm(request.POST or None)
		context = {
			'form': form
		}
		return render(request, 'register.html', context)

	if request.method=='POST':
			form = RegisterForm(request.POST or None)
			if form.is_valid():
				print('kunal')
				u=form.cleaned_data.get('username')
				if (any(c.isalpha() for c in u)==False):
					return redirect('/register')
				User = form.save(commit=False)
				email = form.cleaned_data.get('email')
				k = get_user_model().objects.all()
				e = []
				for i in range(0, len(k)):
					e.append(k[i].email)
				if email in e:
					return redirect('/registere')
				else:
					pwd = form.cleaned_data.get('password')
					c_pwd = form.cleaned_data.get('confirm_password')
					if pwd == c_pwd:
						User.set_password(pwd)
						User.save()
						subject2 = 'CDAC ALUMNI PORTAL'
						message2 = 'Thanks for registering.Now complete your profile to let let other know about you.'
						print('kunal')
						user = authenticate(username=User.username, password=pwd)
						try:
							login(request, User)
							send_mail(subject2, message2, settings.EMAIL_HOST_USER, [request.user.email])

							return redirect('/')
						except:
							return redirect('/registeru/')


					else:
						s = 1
						print('vaishali')
						return redirect('/registerp')
			else:
				return redirect('/registeru')
			context = {
				'form': form
			}
			return render(request, 'register.html', context)


def register_e(request):
	s = 0
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		u=form.cleaned_data.get('username')
		if (any(c.isalpha() for c in u)==False):
			return redirect('/register')
		User = form.save(commit=False)
		email = form.cleaned_data.get('email')
		k = get_user_model().objects.all()
		e = []
		for i in range(0, len(k)):
			e.append(k[i].email)
		if email in e:
			return redirect('/registere')
		else:
			pwd = form.cleaned_data.get('password')
			c_pwd = form.cleaned_data.get('confirm_password')
			if pwd == c_pwd:
				User.set_password(pwd)
				User.save()
				subject2 = 'CDAC ALUMNI PORTAL'
				message2 = 'Thanks for registering.Now complete your profile to let let other know about you.'

				user = authenticate(username=User.username, password=pwd)
				try:
					login(request, User)
					send_mail(subject2, message2, settings.EMAIL_HOST_USER, [request.user.email])

					return redirect('/')
				except:
					return redirect('/registeru/')


			else:
				s = 1
				return redirect('/registerp')

	context = {
		'form': form
	}
	return render(request, 'registratione.html', context)

def register_u(request):
	if request.method == "GET":
		print('Kunal')
		form = RegisterForm(request.POST or None)
		context = {
			'form': form
		}
		return render(request, 'registeru.html', context)

	if request.method == 'POST':
		form = RegisterForm(request.POST or None)
		if form.is_valid():
			print('kunal')
			u = form.cleaned_data.get('username')
			if (any(c.isalpha() for c in u) == False):
				return redirect('/register')
			User = form.save(commit=False)
			email = form.cleaned_data.get('email')
			k = get_user_model().objects.all()
			e = []
			for i in range(0, len(k)):
				e.append(k[i].email)
			if email in e:
				return redirect('/registere')
			else:
				pwd = form.cleaned_data.get('password')
				c_pwd = form.cleaned_data.get('confirm_password')
				if pwd == c_pwd:
					User.set_password(pwd)
					User.save()
					subject2 = 'CDAC ALUMNI PORTAL'
					message2 = 'Thanks for registering.Now complete your profile to let let other know about you.'
					print('kunal')
					user = authenticate(username=User.username, password=pwd)
					try:
						login(request, User)
						send_mail(subject2, message2, settings.EMAIL_HOST_USER, [request.user.email])

						return redirect('/')
					except:
						return redirect('/registeru/')


				else:
					s = 1
					print('kunal')
					return redirect('/registerp')
		else:
			return redirect('/registeru')
		context = {
			'form': form
		}
		return render(request, 'registeru.html', context)


def contact(request):
		r = 0
		em=[]
		s=0
		if request.user.is_authenticated:
			z = Info.objects.all()
			for i in range(0, len(z)):
				em.append(z[i].Email)
			if request.user.email in em:
				a = get_object_or_404(Info, Email=request.user.email)
				if a.valid == True:
					s = 1
			r = 1
		c = Con.objects.all()
		a = Con.objects.all().count()
		b = a - 1
		return render(request, "contact.html", {'r': r, 's':s,'c': c[b]})


def login_c(request):
		if request.method=="GET":
			return render(request,"login.html")
		if request.method=="POST":
			username = request.POST.get('username')
			password = request.POST.get('Password')
			if (username=='cdac' and password=='cdac@123'):				#username and password of TPO
				tp=authenticate(username='cdac',password='cdac@123')
				login(request,tp)
				return redirect('/tpo')
			else:
				user = authenticate(username=username, password=password)
			try:
				login(request, user)
				return redirect('/')
			except:
				return redirect('/login1/')


def login_v(request):
	if request.method == "GET":
		return render(request, "login1.html")
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('Password')
		if (username == 'cdac' and password == 'cdac@123'):
			return redirect('/tpo')
		else:
			user = authenticate(username=username, password=password)
		try:
			login(request, user)
			return redirect('/')
		except:
			return redirect('/login1/')


def logout_c(request):
	if request.user.is_authenticated:
		logout(request)
		return redirect('/')
def roleinfo(request):
	return render (request,'roleinfo.html',{})


class ContactWizard(SessionWizardView):
	template_name = "roleinfo.html"
	form_list = [ContactForm1,ContactForm2,ContactForm3,ContactForm4]
	file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'media'))

	instance = None

	def get(self, request, *args, **kwargs):
		try:
			return self.render(self.get_form())
		except KeyError:
			return super.get(request, *args, **kwargs)


	def get_form_instance(self, step):
		if self.instance is None:
		 self.instance = Info()
		return self.instance


	def done(self, form_list, **kwargs):
		self.instance.Email=self.request.user.email
		self.instance.save()
		return redirect('/done/')

def pdone(request):
	if request.user.is_authenticated:
		e=request.user.email
		obj = Info.objects.all().filter(Q(Email__icontains=e))
		return render(request,'profiledone.html',{'m':obj})
def emailf(request):
    form = EmailForm(request.POST or None)
    if form.is_valid():
        User = form.save(commit=False)
        mobile_no = form.cleaned_data.get('mobile')
        email = form.cleaned_data.get('email')
        message=form.cleaned_data('message')
        name=form.cleaned_data('name')
        subject = 'enquiry from student'
        message = name+"with mobile no."+mobile_no+"and email id"+email+"had a following querry      "+message
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['kunagg25@gmail.com', email]
        send_mail(subject, message, email_from, recipient_list)

def batch(request):
	if request.user.is_authenticated:
		e = request.user.email
		obj = Info.objects.all().filter(Q(Email__icontains=e))
		for o in obj:
			bat = Info.objects.exclude(Email=request.user.email).filter(Q(Batch__icontains=o.Batch))
		return render(request,'batch.html',{'obj_list':bat})

def single(request,id=None):
    instance = get_object_or_404(Info, id=id)
    context = {
        'instance': instance
    }
    return render(request, 'single.html', context)

def yearbook(request):
	a=0
	b=0
	c=0
	d=0
	e=0
	f=0
	g=0
	h=0
	i=0
	j=0
	k=0
	l=0
	ob= Info.objects.all().exclude(Email=request.user.email)
	for m in range(0,len(ob)):
		if ob[m].Batch=='2019':
			a+=1
		elif ob[m].Batch=='2018':
			b+=1
		elif ob[m].Batch=='2017':
			c+=1
		elif ob[m].Batch == '2016':
			d += 1
		elif ob[m].Batch == '2015':
			e += 1
		elif ob[m].Batch == '2014':
			f += 1
		elif ob[m].Batch == '2013':
			g += 1
		elif ob[m].Batch == '2012':
			h += 1
		elif ob[m].Batch=='2011':
			i+=1
		elif ob[m].Batch=='2010':
			j+=1
		elif ob[m].Batch=='2009':
			k+=1
		elif ob[m].Batch=='2008':
			l+=1
	u=request.user.email
	instance=get_object_or_404(Info,Email=u)
	return render(request,'yearbook2.html',{'obj':instance,'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'g':g,'h':h,'i':i,'j':j,'k':k,'l':l})
def b2019(request):
	bat = Info.objects.all().filter(Q(Batch__icontains=2019)).exclude(Email=request.user.email)

	return render(request,'batch.html',{'obj_list':bat,'b':2019,'z':bat.count()})
def b2018(request):
	bat = Info.objects.all().filter(Q(Batch__icontains=2018)).exclude(Email=request.user.email)
	return render(request,'batch.html',{'obj_list':bat,'b':2018,'z':bat.count()})
def b2017(request):
	bat = Info.objects.all().filter(Q(Batch__icontains=2017)).exclude(Email=request.user.email)
	return render(request,'batch.html',{'obj_list':bat,'b':2017,'z':bat.count()})
def b2016(request):
	bat = Info.objects.all().filter(Q(Batch__icontains=2016)).exclude(Email=request.user.email)
	return render(request,'batch.html',{'obj_list':bat,'b':2016,'z':bat.count()})
def b2015(request):
	bat = Info.objects.all().filter(Q(Batch__icontains=2015)).exclude(Email=request.user.email)
	return render(request,'batch.html',{'obj_list':bat,'b':2015,'z':bat.count()})
def b2014(request):
	bat = Info.objects.all().filter(Q(Batch__icontains=2014)).exclude(Email=request.user.email)
	return render(request,'batch.html',{'obj_list':bat,'b':2014,'z':bat.count()})
def b2013(request):
	bat = Info.objects.all().filter(Q(Batch__icontains=2013)).exclude(Email=request.user.email)
	return render(request,'batch.html',{'obj_list':bat,'b':2013,'z':bat.count()})
def b2012(request):
	bat = Info.objects.all().filter(Q(Batch__icontains=2012)).exclude(Email=request.user.email)
	return render(request,'batch.html',{'obj_list':bat,'b':2012,'z':bat.count()})
def b2011(request):
	bat = Info.objects.all().filter(Q(Batch__icontains=2011)).exclude(Email=request.user.email)
	return render(request,'batch.html',{'obj_list':bat,'b':2011,'z':bat.count()})
def b2010(request):
	bat = Info.objects.all().filter(Q(Batch__icontains=2010)).exclude(Email=request.user.email)
	return render(request,'batch.html',{'obj_list':bat,'b':2010,'z':bat.count()})
def b2009(request):
	bat = Info.objects.all().filter(Q(Batch__icontains=2009)).exclude(Email=request.user.email)
	return render(request,'batch.html',{'obj_list':bat,'b':2009,'z':bat.count()})
def b2008(request):
	bat = Info.objects.all().filter(Q(Batch__icontains=2008)).exclude(Email=request.user.email)
	return render(request,'batch.html',{'obj_list':bat,'b':2008,'z':bat.count()})
def postjob(request):
	if request.user.is_authenticated:
		form = JobForm(request.POST or None)
		if form.is_valid():
			flag=0
			countr=0
			countc=0
			cn=form.cleaned_data.get('Company_name')
			jt=form.cleaned_data.get('Job_title')
			loc=form.cleaned_data.get('Location')
			ar=form.cleaned_data.get('About_role')
			ac=form.cleaned_data.get('About_company')
			if (any(c.isalpha() for c in cn)==False):
				print('kunal')
				flag=1
			elif (any(c.isalpha() for c in loc) ==False):
				print('kunal')
				flag=1

			elif (any(c.isnumeric() for c in jt) ==True):
				print('kunal')
				flag=1
			for i in ar:
				if i.isalpha():
					countr=countr+1

			for i in ac:
				if i.isalpha():
					countc=countc+1

			if countr<6:
				flag=1
			elif countc<6:
				flag=1

			if (flag == 1):
				return redirect('/demo')
			new_post = form.save(commit=False)
			new_post.Deadline = request.POST.get('date')
			new_post.Your_name = request.user.username
			new_post.Email = request.user.email
			new_post.save()
			return redirect('/job/')
		context = {
			'form': form}
		return render(request, 'postjob.html', context)
	else:
		return redirect('/login/')
def job(request):
	today = timezone.now()
	if request.user.is_authenticated:
		e=request.user.email
		a = get_object_or_404(Info, Email=e)
		count=0
		obj_list=Job.objects.all().order_by('Deadline')
		a=Job.objects.all()
		for i in range(0,len(a)):
			if (a[i].Deadline >= datetime.date(datetime.now())):
				count+=1
		z=Job.objects.all().filter(Email=request.user.email).count()
		k=Apply_job.objects.all().filter(Email_apply=request.user.email).count()

		return render(request,'jobs.html',{"obj_list":obj_list,"a":a,"today":today,'k':k,'z':z,'count':count})
	else:
		return redirect('/login/')

def my_profile(request):
	q=request.user
	z = Profile.objects.filter(user=q).first()
	rec_friend_requests = FriendRequest.objects.filter(to_user=z.user)
	m = Message.objects.filter(to_user=q.username)
	p=get_object_or_404(Profile,user=q)
	friend=p.friends.all()
	e=request.user.email
	
	obj=get_object_or_404(Info, Email=e)
	
	pic=[]
	first=[]
	last=[]
	photo=[]
	for i in range(0,len(friend)):
		a=get_object_or_404(User,username=friend[i].user)
		b=get_object_or_404(Info,Email=a.email)
		pic.append(b.Profile_photo)
		first.append(b.First_name)
		last.append(b.Last_name)




	mylist = zip(friend[:3], pic[:3],first[:3],last[:3])

	context={'obj':obj,
			 'friend':mylist,
			 'count':len(friend),

			 'rec':rec_friend_requests,
			 'message_list':m,

			 }
	return render(request,'my_profile.html',context)

def jobdetail(request,id=None):
	count = 0
	check = 0
	e = request.user.username
	i=get_object_or_404(Info,Email=request.user.email)
	instance = get_object_or_404(Job, id=id)
	list=Apply_job.objects.all().filter(Q(Email_apply__icontains=request.user.email))
	for l in list:
		if (l.Company_name==instance.Company_name and l.Job_title==instance.Job_title):
			count=count+1
	if request.user.is_authenticated:
		form = Apply_form(request.POST or None, request.FILES or None)
		if form.is_valid():
			new_post = form.save(commit=False)
			new_post.user = request.user
			new_post.Company_name = instance.Company_name
			new_post.Job_title = instance.Job_title
			new_post.Posted_by = instance.Your_name
			new_post.Email_post = instance.Email
			new_post.Email_apply = request.user.email
			new_post.Deadline = instance.Deadline
			new_post.Salary=instance.Salary
			new_post.Location=instance.Location
			new_post.About_role=instance.About_role
			new_post.Mobile_no=i.Mobile_no
			new_post.About_company=instance.About_company
			new_post.save()
			subject=str(new_post.user)+" having email - "+str(new_post.Email_apply)+" had applied for the job posted by you having company-name - "+str(new_post.Company_name)+" and of profile - "+str(new_post.Job_title)+". You can find his/her resume in attachment.   THANK YOU!!"
			email = EmailMessage('CDAC-ALUMNI ,Student Applied',subject
								 ,settings.EMAIL_HOST_USER,
								 [instance.Email])
			file=new_post.resume.url
			email.content_subtype = "html"
			files = os.path.join(settings.BASE_DIR,file[1:])
			email.attach_file(files)
			email.send(fail_silently=False)
			return redirect('/job/')
		context = {
			'instance': instance, 'a': e, 'form':form,'list':list,'count':count,'check':check
		}

		return render(request,'jobdetail.html',context)
	else:
		return redirect("/login")
def director(request):
	r = 0
	z = 1
	em = []
	s = 0
	if request.user.is_authenticated:
		r = 1
		n = Info.objects.all()
		for i in range(0, len(n)):
			em.append(n[i].Email)
		if request.user.email in em:
			a = get_object_or_404(Info, Email=request.user.email)
			if a.valid == True:
				s = 1
	return render(request,'director.html',{'r':r,'s':s,'z':z})

def applied_by_me(request):
	e = request.user.email
	a = request.user.username
	list = Apply_job.objects.all().filter(Q(Email_apply__icontains=e))
	context ={'list':list,'a':a,'z':list.count()}
	return render(request,'applied_by_me.html',context)

def applyjob(request,id=None):
	instance=get_object_or_404(Apply_job,id=id)
	return render(request,'applyjob.html',{'instance':instance,'a':request.user.username})

def postedjob(request):
	e = request.user.email
	a = request.user.username
	list = Job.objects.all().filter(Q(Email__icontains=e))
	z=list.count()
	context ={'list':list,'a':a,'z':z}
	return render(request,'postedjob.html',context)

def singlepostedjob(request,id=None):
	instance=get_object_or_404(Job,id=id)
	return render(request,'singlepostedjob.html',{'instance':instance,'a':request.user.username})


def getfile(request,id=None):
	instance=get_object_or_404(Job,id=id)
	response=HttpResponse(content_type='text/csv')
	response['Content-Disposition']='attachment;filename="Data.csv"'
	candidates=Apply_job.objects.all().filter(Q(Company_name__icontains=instance.Company_name) and Q(Job_title__icontains=instance.Job_title))
	writer=csv.writer(response)
	writer.writerow(['Candidate Id','Candidate Name','Candidate Email','Candidate Mobile No.','Date of Apply','Company Name'])
	for candidate in candidates:
		writer.writerow([candidate.id,candidate.user,candidate.Email_apply,candidate.Mobile_no,candidate.Apply_date,candidate.Company_name])
	return response


# for friend request



def users_list(request):
	count = FriendRequest.objects.filter(to_user=request.user).count()
	counts = FriendRequest.objects.filter(from_user=request.user).count()
	p = get_object_or_404(Profile, user=request.user)
	countf = p.friends.all().count()
	k = Profile.objects.exclude(friends=request.user.profile)
	users =k.exclude(user=request.user)
	obj=get_object_or_404(Info,Email=request.user.email)
	button=[]
	pic=[]
	tech=[]
	first=[]
	last=[]
	batch=[]
	em=[]
	for i in range(0,len(users)):
		button.append('None')
		if users[i] not in request.user.profile.friends.all():
			button[i] = 'not_friend'

			# if we have sent him a friend request
			if len(FriendRequest.objects.filter(
					from_user=request.user).filter(to_user=users[i].user)) == 1:
				button[i] = 'friend_request_sent'
	z = Info.objects.all()

	for i in range(0,len(z)):
		em.append(z[i].Email)

	for i in range(0,len(users)):
		a=get_object_or_404(User,username=users[i].user)
		if a.email in em:
			b=get_object_or_404(Info,Email=a.email)
			if b.valid==True:
				pic.append(b.Profile_photo)
				first.append(b.First_name)
				last.append(b.Last_name)
				batch.append(b.Batch)
				tech.append(b.Technology)
	mylist=zip(users,button,pic,first,last,batch,tech)
	context = {
		'my':mylist,
		'obj':obj,
		'count':count,
		'counts':counts,
		'countf':countf
	}
	

	return render(request, "accounts/home.html", context)

def send_friend_request(request, id):
	if request.user.is_authenticated:
		user = get_object_or_404(User, id=id)
		frequest, created = FriendRequest.objects.get_or_create(
			from_user=request.user,
			to_user=user)
		return HttpResponseRedirect('/users')

def cancel_friend_request(request, id):
	if request.user.is_authenticated:
		user = get_object_or_404(User, id=id)
		frequest = FriendRequest.objects.filter(
			from_user=request.user,
			to_user=user).first()
		frequest.delete()
		return HttpResponseRedirect('/users')

def accept_friend_request(request, id):
	from_user = get_object_or_404(User, id=id)
	frequest = FriendRequest.objects.filter(from_user=from_user, to_user=request.user).first()
	user1 = frequest.to_user
	user2 = from_user
	user1.profile.friends.add(user2.profile)
	user2.profile.friends.add(user1.profile)
	frequest.delete()
	return HttpResponseRedirect('/users/')

def delete_friend_request(request, id):
	from_user = get_object_or_404(User, id=id)
	frequest = FriendRequest.objects.filter(from_user=from_user, to_user=request.user).first()
	frequest.delete()
	return HttpResponseRedirect('/users/')

def profile_view(request, id):
	p = Profile.objects.filter(id=id).first()
	
	u = p.user
	sent_friend_requests = FriendRequest.objects.filter(from_user=p.user)
	rec_friend_requests = FriendRequest.objects.filter(to_user=p.user)

	friends = p.friends.all()

	# is this user our friend
	button_status = 'none'
	if p not in request.user.profile.friends.all():
		button_status = 'not_friend'

		# if we have sent him a friend request
		if len(FriendRequest.objects.filter(
			from_user=request.user).filter(to_user=p.user)) == 1:
				button_status = 'friend_request_sent'

	context = {
		'u': u,
		'button_status': button_status,
		'friends_list': friends,
		'sent_friend_requests': sent_friend_requests,
		'rec_friend_requests': rec_friend_requests
	}

	return render(request, "accounts/profile.html", context)

def uprof(request, user):
	b=0
	yes=0
	u=get_object_or_404(User,username=user)
	f=get_object_or_404(Profile,user=u)
	a=f.friends.all()
	user1=[]
	for i in range(0,len(a)):
		user1.append(a[i].user.username)

	if request.user.username in user1:
		yes=1
	if(len(FriendRequest.objects.filter(from_user=request.user).filter(to_user=u))>0):
		b=1
	e=get_object_or_404(Info,Email=u.email)
	s=Skill.objects.all().filter(semail=e.Email)
	z=s.count()
	return render(request,'uprof.html',{'z':z,'obj':e,'skill':s,'y':yes,'user':u,'b':b,'username':user})

def allfriends(request):
	q=request.user
	p=get_object_or_404(Profile,user=q)
	friend=p.friends.all()
	e = request.user.email
	obj = get_object_or_404(Info, Email=e)
	pic=[]
	first=[]
	last=[]
	email=[]
	mobile=[]
	id=[]
	for i in range(0,len(friend)):
		a=get_object_or_404(User,username=friend[i].user)
		b=get_object_or_404(Info,Email=a.email)
		pic.append(b.Profile_photo)
		first.append(b.First_name)
		last.append(b.Last_name)
		email.append(b.Email)
		mobile.append(b.Mobile_no)
		id.append(b.id)
	mylist=zip(friend,pic,first,last,email,mobile,id)
	return render(request,'allfriends.html',{'allfriends':mylist,'obj':obj})

def messageview(request,u=None):
	t = get_object_or_404(User, username=u)
	to = get_object_or_404(Info, Email=t.email)
	form = messageform(request.POST or None)
	if form.is_valid():
		mes = form.save(commit=False)
		mes.from_user=request.user.username
		mes.to_user=u

		mes.save()
		return redirect('/my_profile')
	return render(request,'update_book.html',{'form': form,"tof":to.First_name,"tol":to.Last_name,"pic":to.Profile_photo})

def messageviewn(request,u=None):
	t = get_object_or_404(User, username=u)
	to = get_object_or_404(Info, Email=t.email)
	form = messageform(request.POST or None)
	if form.is_valid():
		mes = form.save(commit=False)
		mes.from_user=request.user.username
		mes.to_user=u

		mes.save()
		return redirect('/message')
	return render(request,'update_book.html',{'form': form,"tof":to.First_name,"tol":to.Last_name,"pic":to.Profile_photo})



def delete_message(request, id):
	mess = get_object_or_404(Message,id=id)
	mess.delete()
	return HttpResponseRedirect('/my_profile/')

def delete_messagen(request, id):
	mess = get_object_or_404(Message,id=id)
	mess.delete()
	return HttpResponseRedirect('/message/')

def piceditv(request, id):
	instance = get_object_or_404(Info, id=id)
	form = picedit(request.POST or None, instance=instance)
	if form.is_valid():
		update_post = form.save(commit=False)
		update_post.save()
		return redirect('/my_profile/')
	context = {
		'form': form
	}
	return render(request, 'editform.html', context)

def editcontact(request, id):
	instance = get_object_or_404(Info, id=id)
	form = contactedit(request.POST or None, instance=instance)
	if form.is_valid():
		update_post = form.save(commit=False)
		update_post.save()
		return redirect('/my_profile/')
	context = {
		'form': form
	}
	return render(request, 'editcontactform.html', context)

def edueditv(request, id):
	instance = get_object_or_404(Info, id=id)
	form = eduedit(request.POST or None, instance=instance)
	if form.is_valid():
		update_post = form.save(commit=False)
		update_post.save()
		return redirect('/my_profile/')
	context = {
		'form': form
	}
	return render(request, 'edueditform.html', context)

def experteditv(request,id):
    instance = get_object_or_404(Info, id=id)
    form = expertedit(request.POST or None, instance=instance)
    if form.is_valid():
        update_post = form.save(commit=False)
        update_post.save()
        return redirect('/my_profile/')
    context = {
        'form': form
    }
    return render(request, 'experteditform.html', context)

def uprof1(request,id):
	yes=0
	b=0
	i = get_object_or_404(Info,id=id)
	print(i.Profile_photo)
	u=get_object_or_404(User,email=i.Email)
	f = get_object_or_404(Profile, user=u)
	a = f.friends.all()
	user = []
	if (len(FriendRequest.objects.filter(from_user=request.user).filter(to_user=u)) > 0):
		b = 1
	for j in range(0, len(a)):
		user.append(a[j].user.username)

	if request.user.username in user:
		yes = 1
	s=Skill.objects.all().filter(semail=u.email)
	z=s.count()
	return render(request,'uprof1.html',{'z':z,'obj':i,'skill':s,'y':yes,'user':u,'b':b,'id':id,'kk':'kk'})


def validj(request):
	email=[]
	a=Info.objects.all()
	for i in range(0,len(a)):
		email.append(a[i].Email)

	if request.user.email in email:
		q=get_object_or_404(Info,Email=request.user.email)
		if q.valid==True:
			return redirect('/job')
		else:
			return redirect('/infov')

	return redirect('/infov')

def validp(request):
	email = []
	a = Info.objects.all()
	for i in range(0,len(a)):
		email.append(a[i].Email)

	if request.user.email in email:
		q = get_object_or_404(Info, Email=request.user.email)
		if q.valid == True:
			return redirect('/my_profile')
		else:
			return redirect('/infov')

	return redirect('/infov')
def infov(request):
		email=[]
		r = 0
		if request.user.is_authenticated:
			r = 1
		a=Info.objects.all()
		for i in range(0,len(a)):
			email.append(a[i].Email)

		if request.user.email in email:
			b=get_object_or_404(Info,Email=request.user.email)
			if b.valid==True:
				return redirect('/my_profile')
			elif b.Profile_photo!='':
				return render(request,'approve.html',{})
			elif b.Degree!='':
				form=ContactForm3(request.POST or None, request.FILES or None ,instance=b)
				if form.is_valid():
					f=form.save(commit=False)
					f.save()
					subject2='CDAC ALUMNI PORTAL'
					message2='Thanks for filling your details ,your profile is gathered by us .Please wait for approval from admin'
					try:
						send_mail(subject2,message2,settings.EMAIL_HOST_USER,[request.user.email])
					except:
						flag=1
					subject = 'New User Wants to Register fo CDAC Alumni'
					message = 'New Alumni'+str(b.First_name)+' '+str(b.Last_name)+'with email address'+str(b.Email)+'had requested to connect with Alumni Portal'
					email_from = settings.EMAIL_HOST_USER
					recipient_list = ['sarthak@gmail.com']				#email id of TPO
					send_mail(subject, message, email_from, recipient_list)
					return redirect('/done')

				return render(request,'infov3.html',{'form':form,'r':r})
			elif b.Role!='':
				form = ContactForm4(request.POST or None,instance=b)
				if form.is_valid():
					f = form.save(commit=False)
					f.save()
					return redirect('/infov')

				return render(request, 'infov2.html', {'form': form,'r':r})

			elif b.City!='':
				form = ContactForm2(request.POST or None,instance=b)
				if form.is_valid():
					f = form.save(commit=False)
					f.save()
					return redirect('/infov')

				return render(request, 'infov1.html', {'form': form,'r':r})



		else:
			form=ContactForm1(request.POST or None)
			if form.is_valid():
				f=form.save(commit=False)
				f.Email=request.user.email
				f.save()
				return redirect('/infov')
			return render(request,'infov.html',{'form':form,'r':r})





def prev1(request):
	r = 0
	if request.user.is_authenticated:
		r = 1
	a=get_object_or_404(Info,Email=request.user.email)
	form=ContactForm1(request.POST or None , instance=a)
	if form.is_valid():
		f=form.save(commit=False)
		f.Email=request.user.email
		f.save()
		return redirect('/infov')
	return render(request,'infov.html',{'form':form,'r':r})

def prev2(request):
	r = 0
	if request.user.is_authenticated:
		r = 1
	a=get_object_or_404(Info,Email=request.user.email)
	form=ContactForm2(request.POST or None , instance=a)
	if form.is_valid():
		f=form.save(commit=False)
		f.save()
		return redirect('/infov')
	return render(request,'infov1.html',{'form':form,'r':r})

def prev3(request):
	r = 0
	if request.user.is_authenticated:
		r = 1
	a=get_object_or_404(Info,Email=request.user.email)
	form=ContactForm4(request.POST or None , instance=a)
	if form.is_valid():
		f=form.save(commit=False)
		f.save()
		return redirect('/infov')
	return render(request,'infov2.html',{'form':form,'r':r})



def get_document(request):
    template = os.path.join(os.path.dirname(__file__),
    'static\\sam1.docx')
    a = get_object_or_404(Info,Email=request.user.email)


    document = MailMerge(template)
    document.merge(user='testcoy',
                   Name = a.First_name,
                   email = request.user.email,
                   phone = a.Mobile_no,
                   Degree = a.Degree,
                   College = a.College,
                   department = a.Department,
                    address=a.Address,
                   )
    f = io.BytesIO()
    document.write(f)
    length = f.tell()
    f.seek(0)
    response = HttpResponse(
        f.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
         )
    response['Content-Disposition'] = 'attachment; filename=example.docx'
    response['Content-Length'] = length
    return response


def search(request,querry=None):
	if request.method=='GET':
		stud = None
		p = []
		f = []
		username = request.user
		today = timezone.now()
		y = Job.objects.all().filter(Q(Job_title__icontains=querry))
		k = Info.objects.all().filter(Q(First_name__icontains=querry)).exclude(Email=request.user.email)
		stud = k.exclude(valid=False)
		for i in range(0, len(stud)):
			p.append(get_object_or_404(User, email=stud[i].Email))

		for j in range(0, len(p)):
			f.append(get_object_or_404(Profile, user=p[j]))

		button = []
		pic = []
		first = []
		last = []
		batch = []
		tech = []
		obj=[]
		for i in range(0, len(f)):
			button.append('None')
			if f[i] not in request.user.profile.friends.all():
				button[i] = 'not_friend'

				# if we have sent him a friend request
				if len(FriendRequest.objects.filter(
						from_user=request.user).filter(to_user=f[i].user)) == 1:
					button[i] = 'friend_request_sent'
		for i in range(0, len(f)):
			a = get_object_or_404(User, username=f[i].user)
			b = get_object_or_404(Info, Email=a.email)
			pic.append(b.Profile_photo)
			first.append(b.First_name)
			last.append(b.Last_name)
			batch.append(b.Batch)
			tech.append(b.Technology)
			obj.append(b)
		mylist = zip(f, obj, button, pic, first, last, batch, tech)
		context = {
			'my': mylist,
			'querry': querry,
			'ycount': y.count() + stud.count(),
		}
		return render(request, "search.html", context)

	if request.method=='POST':
		query = None

		stud = None
		p=[]
		f=[]
		query = request.POST.get('q')
		today = timezone.now()
		y = Job.objects.all().filter(Q(Job_title__icontains=query))
		k = Info.objects.all().filter(Q(First_name__icontains=query))
		stud = k.exclude(valid=False)

		for i in range(0,len(stud)):
			p.append(get_object_or_404(User,email=stud[i].Email))

		for j in range(0,len(p)):
			f.append(get_object_or_404(Profile,user=p[j]))


		button = []
		pic = []
		first = []
		last = []
		batch = []
		tech = []
		obj =[]
		for i in range(0, len(f)):
			button.append('None')
			if f[i] not in request.user.profile.friends.all():
				button[i] = 'not_friend'

				# if we have sent him a friend request
				if len(FriendRequest.objects.filter(
						from_user=request.user).filter(to_user=f[i].user)) == 1:
					button[i] = 'friend_request_sent'
		for i in range(0, len(f)):
			a = get_object_or_404(User, username=f[i].user)
			b = get_object_or_404(Info, Email=a.email)
			pic.append(b.Profile_photo)
			first.append(b.First_name)
			last.append(b.Last_name)
			batch.append(b.Batch)
			tech.append(b.Technology)
			obj.append(b)


		mylist = zip(f, obj, button, pic, first, last, batch,tech)
		context = {
			'my': mylist,
			'querry':query,
			'y':y,
			'today':today,
			'ycount': y.count() + stud.count(),

		}
		return render(request, "search.html", context)


def send_friend_request_s(request, id,querry):
	if request.user.is_authenticated:
		user = get_object_or_404(User, id=id)
		frequest, created = FriendRequest.objects.get_or_create(
			from_user=request.user,
			to_user=user)
		return redirect('sea',querry=querry)

def cancel_friend_request_s(request, id,querry):
	if request.user.is_authenticated:
		user = get_object_or_404(User, id=id)
		frequest = FriendRequest.objects.filter(
			from_user=request.user,
			to_user=user).first()
		frequest.delete()
		return redirect('sea',querry=querry)


def searchp(request, querry=None):
	if request.method == 'GET':
		stud = None
		p = []
		f = []
		username = request.user
		k = Info.objects.all().filter(Q(First_name__icontains=querry))
		stud = k.exclude(valid=False)
		for i in range(0, len(stud)):
			p.append(get_object_or_404(User, email=stud[i].Email))
		for j in range(0, len(p)):
			f.append(get_object_or_404(Profile, user=p[j]))

		button = []
		pic = []
		first = []
		last = []
		batch = []
		tech = []
		obj=[]
		for i in range(0, len(f)):
			button.append('None')
			if f[i] not in request.user.profile.friends.all():
				button[i] = 'not_friend'

				# if we have sent him a friend request
				if len(FriendRequest.objects.filter(
						from_user=request.user).filter(to_user=f[i].user)) == 1:
					button[i] = 'friend_request_sent'
		for i in range(0, len(f)):
			a = get_object_or_404(User, username=f[i].user)
			b = get_object_or_404(Info, Email=a.email)
			pic.append(b.Profile_photo)
			first.append(b.First_name)
			last.append(b.Last_name)
			batch.append(b.Batch)
			tech.append(b.Technology)
			obj.append(b)
		mylist = zip(f, obj, button, pic, first, last, batch, tech)
		context = {
			'my': mylist,
			'querry': querry,
			'c':stud.count()
		}
		return render(request, "searchp.html", context)

	if request.method == 'POST':
		query = None

		stud = None
		p = []
		f = []
		username = request.user
		query = request.POST.get('q')

		k = Info.objects.all().filter(Q(First_name__icontains=query))
		stud = k.exclude(valid=False)

		for i in range(0, len(stud)):
			p.append(get_object_or_404(User, email=stud[i].Email))

		for j in range(0, len(p)):
			f.append(get_object_or_404(Profile, user=p[j]))

		button = []
		pic = []
		first = []
		last = []
		batch = []
		tech = []
		obj = []
		for i in range(0, len(f)):
			button.append('None')
			if f[i] not in request.user.profile.friends.all():
				button[i] = 'not_friend'

				# if we have sent him a friend request
				if len(FriendRequest.objects.filter(
						from_user=request.user).filter(to_user=f[i].user)) == 1:
					button[i] = 'friend_request_sent'
		for i in range(0, len(f)):
			a = get_object_or_404(User, username=f[i].user)
			b = get_object_or_404(Info, Email=a.email)
			pic.append(b.Profile_photo)
			first.append(b.First_name)
			last.append(b.Last_name)
			batch.append(b.Batch)
			tech.append(b.Technology)
			obj.append(b)

		mylist = zip(f, obj, button, pic, first, last, batch, tech)
		context = {
			'my': mylist,
			'querry': query,
			'c':stud.count,


		}
		return render(request, "searchp.html", context)


def send_friend_request_p(request, id, querry):
	if request.user.is_authenticated:
		user = get_object_or_404(User, id=id)
		frequest, created = FriendRequest.objects.get_or_create(
			from_user=request.user,
			to_user=user)
		return redirect('seap', querry=querry)


def cancel_friend_request_p(request, id, querry):
	if request.user.is_authenticated:
		user = get_object_or_404(User, id=id)
		frequest = FriendRequest.objects.filter(
			from_user=request.user,
			to_user=user).first()
		frequest.delete()
		return redirect('seap', querry=querry)

def searchj(request):
	query = request.POST.get('q')
	city = request.POST.get('c')
	today = timezone.now()
	y = Job.objects.all().filter(Q(Job_title__icontains=query))
	x = y.filter(Q(Location__icontains=city))

	context = {
		'today': today,
		'y': x,
		'c': x.count()
	}
	return render(request, 'searchj.html', context)


def network(request):
	rec = FriendRequest.objects.filter(to_user=request.user)
	count = FriendRequest.objects.filter(to_user=request.user).count()
	counts = FriendRequest.objects.filter(from_user=request.user).count()
	id = []
	pic = []
	first = []
	last = []
	batch = []
	tech = []
	picf = []
	firstf = []
	lastf = []
	batchf = []
	techf = []
	p = get_object_or_404(Profile, user=request.user)
	friend = p.friends.all().exclude(user=request.user)
	countf = p.friends.all().count()
	for i in range(0, len(rec)):
		b = get_object_or_404(Info, Email=rec[i].from_user.email)
		pic.append(b.Profile_photo)
		first.append(b.First_name)
		last.append(b.Last_name)
		batch.append(b.Batch)
		tech.append(b.Technology)
		id.append(b.id)
	for i in range(0, len(friend)):
		a = get_object_or_404(User, username=friend[i].user)
		b = get_object_or_404(Info, Email=a.email)
		picf.append(b.Profile_photo)
		firstf.append(b.First_name)
		lastf.append(b.Last_name)
		batchf.append(b.Batch)
		techf.append(b.Technology)
	flist = zip(friend, picf, lastf, firstf, batchf, techf)
	list = zip(pic, first, last, batch, tech, rec, id)
	return render(request, 'network.html',  {'list': list, 'count': count, 'flist': flist, 'countf': countf, 'counts': counts})


def message(request):
	if request.method=='GET':
		m = Message.objects.filter(to_user=request.user.username)
		k=Message.objects.filter(from_user=request.user.username)
		f=[]
		l=[]
		p=[]
		fs=[]
		ls=[]
		ps=[]
		for i in range(0,len(m)):
			a=get_object_or_404(User,username=m[i].from_user)
			b=get_object_or_404(Info,Email=a.email)
			f.append(b.First_name)
			l.append(b.Last_name)
			p.append(b.Profile_photo)
		for j in range(0,len(k)):

			a=get_object_or_404(User,username=k[j].to_user)
			b=get_object_or_404(Info,Email=a.email)
			fs.append(b.First_name)
			ls.append(b.Last_name)
			ps.append(b.Profile_photo)
		list=zip(m,f,l,p)
		lists=zip(k,fs,ls,ps)

		p=get_object_or_404(Profile,user=request.user)
		u=p.friends.all()
		count=Message.objects.filter(to_user=request.user.username).count()
		countn=k.count()
		return render(request,'message.html',{'list':list,'countn':countn,'count':count,'u':u,'lists':lists})
	if request.method=='POST':
		username = request.POST.get('name')
		message = request.POST.get('message')
		obj=Message()
		obj.from_user=request.user.username
		obj.to_user=username
		obj.message=message
		obj.save()
		return redirect('/message')


def yeart(request):
    a=Info.objects.all().filter(Batch='2019').count()
    b = Info.objects.all().filter(Batch='2018').count()
    c = Info.objects.all().filter(Batch='2017').count()
    d = Info.objects.all().filter(Batch='2016').count()
    e = Info.objects.all().filter(Batch='2015').count()
    f = Info.objects.all().filter(Batch='2014').count()
    g = Info.objects.all().filter(Batch='2013').count()
    h = Info.objects.all().filter(Batch='2012').count()
    i = Info.objects.all().filter(Batch='2011').count()
    j = Info.objects.all().filter(Batch='2010').count()
    k = Info.objects.all().filter(Batch='2009').count()
    l = Info.objects.all().filter(Batch='2008').count()

    return render(request,'yeart.html',{'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'g':g,'h':h,'i':i,'j':j,'k':k,'l':l})
def b2019t(request):
    m = []
    a = []
    bat = Info.objects.all().filter(Q(Batch__icontains=2019))
    for i in range(0, len(bat)):
        c = Apply_job.objects.all().filter(Email_apply=bat[i].Email)
        if c.count() == 0:
            m.append(0)
        for i in range(0, len(c)):
            q = 0
            if c[i].selected == True:
                q += 1
            m.append(q)
        a.append(c.count())

    batz = zip(bat, a, m)
    return render(request, 'batcht.html', {'obj_list': batz, 'b': 2019,'z':bat.count()})
def b2018t(request):
    m = []
    a = []
    bat = Info.objects.all().filter(Q(Batch__icontains=2018))
    for i in range(0, len(bat)):
        c = Apply_job.objects.all().filter(Email_apply=bat[i].Email)
        if c.count() == 0:
            m.append(0)
        for i in range(0, len(c)):
            q = 0
            if c[i].selected == True:
                q += 1
            m.append(q)

        a.append(c.count())
    batz = zip(bat, a, m)
    return render(request, 'batcht.html', {'obj_list': batz, 'b': 2018,'z':bat.count()})
def b2017t(request):
    m = []
    a = []
    bat = Info.objects.all().filter(Q(Batch__icontains=2017))
    for i in range(0, len(bat)):
        c = Apply_job.objects.all().filter(Email_apply=bat[i].Email)
        if c.count() == 0:
            m.append(0)
        for i in range(0, len(c)):
            q = 0
            if c[i].selected == True:
                q += 1
            m.append(q)

        a.append(c.count())
    batz = zip(bat, a, m)
    return render(request, 'batcht.html', {'obj_list': batz, 'b': 2017,'z':bat.count()})
def b2016t(request):
    m = []
    a = []
    bat = Info.objects.all().filter(Q(Batch__icontains=2016))
    for i in range(0, len(bat)):
        c = Apply_job.objects.all().filter(Email_apply=bat[i].Email)
        if c.count() == 0:
            m.append(0)
        for i in range(0, len(c)):
            q = 0
            if c[i].selected == True:
                q += 1
            print('kunal')
            m.append(q)

        a.append(c.count())
    batz = zip(bat, a, m)
    return render(request, 'batcht.html', {'obj_list': batz, 'b': 2016,'z':bat.count()})
def b2015t(request):
    m = []
    a = []
    bat = Info.objects.all().filter(Q(Batch__icontains=2015))
    for i in range(0, len(bat)):
        c = Apply_job.objects.all().filter(Email_apply=bat[i].Email)
        if c.count() == 0:
            m.append(0)
        for i in range(0, len(c)):
            q = 0
            if c[i].selected == True:
                q += 1
            m.append(q)

        a.append(c.count())

    batz = zip(bat, a, m)
    return render(request, 'batcht.html', {'obj_list': batz, 'b': 2015,'z':bat.count()})
def b2014t(request):
    m = []
    a = []
    bat = Info.objects.all().filter(Q(Batch__icontains=2014))
    for i in range(0, len(bat)):
        c = Apply_job.objects.all().filter(Email_apply=bat[i].Email)
        if c.count() == 0:
            m.append(0)
        for i in range(0, len(c)):
            q = 0
            if c[i].selected == True:
                q += 1
            m.append(q)

        a.append(c.count())

    batz = zip(bat, a, m)
    return render(request, 'batcht.html', {'obj_list': batz, 'b': 2014,'z':bat.count()})
def b2013t(request):
    m = []
    a = []
    bat = Info.objects.all().filter(Q(Batch__icontains=2013))
    for i in range(0, len(bat)):
        c = Apply_job.objects.all().filter(Email_apply=bat[i].Email)
        if c.count() == 0:
            m.append(0)
        for i in range(0, len(c)):
            q = 0
            if c[i].selected == True:
                q += 1
            m.append(q)

        a.append(c.count())

    batz = zip(bat, a, m)
    return render(request, 'batcht.html', {'obj_list': batz, 'b': 2013,'z':bat.count()})
def b2012t(request):
    m=[]
    a = []
    bat = Info.objects.all().filter(Q(Batch__icontains=2012))
    for i in range(0, len(bat)):
        c = Apply_job.objects.all().filter(Email_apply=bat[i].Email)
        if c.count()==0:
            m.append(0)
        for i in range(0,len(c)):
            q=0
            if c[i].selected==True:
                q+=1
            m.append(q)

        a.append(c.count())

    batz = zip(bat, a, m)
    return render(request, 'batcht.html', {'obj_list': batz, 'b': 2012,'z':bat.count()})
def b2011t(request):
    m = []
    a = []
    bat = Info.objects.all().filter(Q(Batch__icontains=2011))
    for i in range(0, len(bat)):
        c = Apply_job.objects.all().filter(Email_apply=bat[i].Email)
        if c.count() == 0:
            m.append(0)
        for i in range(0, len(c)):
            q = 0
            if c[i].selected == True:
                q += 1
            m.append(q)

        print('k')
    print(len(a))
      
    batz = zip(bat, a, m)
    return render(request, 'batcht.html', {'obj_list': batz, 'b': 2011,'z':bat.count()})
def b2010t(request):
    m = []
    a = []
    bat = Info.objects.all().filter(Q(Batch__icontains=2010))
    for i in range(0, len(bat)):
        c = Apply_job.objects.all().filter(Email_apply=bat[i].Email)
        if c.count() == 0:
            m.append(0)
        for i in range(0, len(c)):
            q = 0
            if c[i].selected == True:
                q += 1
            m.append(q)

        a.append(c.count())

    batz = zip(bat, a, m)
    return render(request, 'batcht.html', {'obj_list': batz, 'b': 2010,'z':bat.count()})
def b2009t(request):
    m = []
    a = []
    bat = Info.objects.all().filter(Q(Batch__icontains=2009))
    for i in range(0, len(bat)):
        c = Apply_job.objects.all().filter(Email_apply=bat[i].Email)
        if c.count() == 0:
            m.append(0)
        for i in range(0, len(c)):
            q = 0
            if c[i].selected == True:
                q += 1
            m.append(q)

        a.append(c.count())

    batz = zip(bat, a, m)
    return render(request, 'batcht.html', {'obj_list': batz, 'b': 2009,'z':bat.count()})
def b2008t(request):
    m = []
    a = []
    bat = Info.objects.all().filter(Q(Batch__icontains=2008))
    for i in range(0, len(bat)):
        c = Apply_job.objects.all().filter(Email_apply=bat[i].Email)
        if c.count() == 0:
            m.append(0)
        for i in range(0, len(c)):
            q = 0
            if c[i].selected == True:
                q += 1
            m.append(q)

        a.append(c.count())

    batz = zip(bat, a, m)
    return render(request, 'batcht.html', {'obj_list': batz, 'b': 2008,'z':bat.count()})
def sdata(request,id=None):
    status=[]
    instance=get_object_or_404(Info,id=id)
    data=Apply_job.objects.all().filter(Email_apply=instance.Email)
    for i in range(0,len(data)):
        if data[i].selected==True:
            status.append('Selected')
        else:
            status.append('Not Selected')
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment;filename="Data.csv"'
    writer=csv.writer(response)
    writer.writerow(['Company Name','Profile','status'])
    for candidate in range(0,len(data)):
        writer.writerow([data[i].Company_name,data[i].Job_title,status[i]])
    return response

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)

def validateuser(request):
	username = request.GET.get('username', None)
	is_taken = any(c.isalpha() for c in username)
	if is_taken == False:
		is_taken = True
	else:
		is_taken = False
	data = {
		'is_taken': is_taken
	}
	return JsonResponse(data)


def validate_email(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': Info.objects.filter(Email__iexact=email).exists()
    }
    return JsonResponse(data)

def validate_skill(request):
    skills = request.GET.get('skill', None)
    data = {
        'is_taken': Skill.objects.filter(skill__iexact=skills).filter(semail__iexact=request.user.email).exists()
    }
    return JsonResponse(data)

def validate_date(request):
	startd = request.GET.get('startd', None)
	endd = request.GET.get('endd', None)
	startdate = datetime.strptime(startd, "%Y-%m-%d").date()
	enddate = datetime.strptime(endd, "%Y-%m-%d").date()
	is_taken=False
	pro=project.objects.all().filter(semail=request.user.email)
	for i in range(0,len(pro)):
		if(startdate>pro[i].startd and startdate<pro[i].endd):
			is_taken=True
		elif(startdate<pro[i].startd and enddate>pro[i].startd):
			is_taken=True
		elif(enddate>pro[i].startd and enddate<pro[i].endd):
			is_taken=True
	 
	data = {
		'is_taken': is_taken
	}
	return JsonResponse(data)


def validate_datej(request):
	startd = request.GET.get('startd', None)
	endd = request.GET.get('endd', None)
	startdate = datetime.strptime(startd, "%Y-%m-%d").date()
	enddate = datetime.strptime(endd, "%Y-%m-%d").date()
	is_taken=False
	pro=Sjob.objects.all().filter(semail=request.user.email)
	for i in range(0,len(pro)):
		if(startdate>pro[i].startd and startdate<pro[i].endd):
			is_taken=True
		elif(startdate<pro[i].startd and enddate>pro[i].startd):
			is_taken=True
		elif(enddate>pro[i].startd and enddate<pro[i].endd):
			is_taken=True
	 
	data = {
		'is_taken': is_taken
	}
	return JsonResponse(data)



def validate_datei(request):
	startd = request.GET.get('startd', None)
	endd = request.GET.get('endd', None)
	startdate = datetime.strptime(startd, "%Y-%m-%d").date()
	enddate = datetime.strptime(endd, "%Y-%m-%d").date()
	is_taken=False
	pro=Intern.objects.all().filter(semail=request.user.email)
	for i in range(0,len(pro)):
		if(startdate>pro[i].startd and startdate<pro[i].endd):
			is_taken=True
		elif(startdate<pro[i].startd and enddate>pro[i].startd):
			is_taken=True
		elif(enddate>pro[i].startd and enddate<pro[i].endd):
			is_taken=True
	 
	data = {
		'is_taken': is_taken
	}
	return JsonResponse(data)



def validate_datet(request):
	startd = request.GET.get('startd', None)
	endd = request.GET.get('endd', None)
	startdate = datetime.strptime(startd, "%Y-%m-%d").date()
	enddate = datetime.strptime(endd, "%Y-%m-%d").date()
	is_taken=False
	pro=Training.objects.all().filter(semail=request.user.email)
	for i in range(0,len(pro)):
		if(startdate>pro[i].startd and startdate<pro[i].endd):
			is_taken=True
		elif(startdate<pro[i].startd and enddate>pro[i].startd):
			is_taken=True
		elif(enddate>pro[i].startd and enddate<pro[i].endd):
			is_taken=True
	 
	data = {
		'is_taken': is_taken
	}
	return JsonResponse(data)


def validate_datee(request):
	startd = request.GET.get('startd', None)
	endd = request.GET.get('endd', None)
	startdate = datetime.strptime(startd, "%Y-%m-%d").date()
	enddate = datetime.strptime(endd, "%Y-%m-%d").date()
	is_taken=False
	prop=project.objects.all().filter(semail=request.user.email).exclude(startd=startdate)
	pro=prop.exclude(endd=enddate)
	for i in range(0,len(pro)):
		if(startdate>pro[i].startd and startdate<pro[i].endd):
			is_taken=True
		elif(startdate<pro[i].startd and enddate>pro[i].startd):
			is_taken=True
		elif(enddate>pro[i].startd and enddate<pro[i].endd):
			is_taken=True
	 
	data = {
		'is_taken': is_taken
	}
	return JsonResponse(data)


def validate_dateje(request):
	startd = request.GET.get('startd', None)
	endd = request.GET.get('endd', None)
	startdate = datetime.strptime(startd, "%Y-%m-%d").date()
	enddate = datetime.strptime(endd, "%Y-%m-%d").date()
	is_taken=False
	prop=Sjob.objects.all().filter(semail=request.user.email).exclude(startd=startdate)
	pro=prop.exclude(endd=enddate)
	for i in range(0,len(pro)):
		if(startdate>pro[i].startd and startdate<pro[i].endd):
			is_taken=True
		elif(startdate<pro[i].startd and enddate>pro[i].startd):
			is_taken=True
		elif(enddate>pro[i].startd and enddate<pro[i].endd):
			is_taken=True
	 
	data = {
		'is_taken': is_taken
	}
	return JsonResponse(data)



def validate_dateie(request):
	startd = request.GET.get('startd', None)
	endd = request.GET.get('endd', None)
	startdate = datetime.strptime(startd, "%Y-%m-%d").date()
	enddate = datetime.strptime(endd, "%Y-%m-%d").date()
	is_taken=False
	prop=Intern.objects.all().filter(semail=request.user.email).exclude(startd=startdate)
	pro=prop.exclude(endd=enddate)
	for i in range(0,len(pro)):
		if(startdate>pro[i].startd and startdate<pro[i].endd):
			is_taken=True
		elif(startdate<pro[i].startd and enddate>pro[i].startd):
			is_taken=True
		elif(enddate>pro[i].startd and enddate<pro[i].endd):
			is_taken=True
	 
	data = {
		'is_taken': is_taken
	}
	return JsonResponse(data)



def validate_datete(request):
	startd = request.GET.get('startd', None)
	endd = request.GET.get('endd', None)
	startdate = datetime.strptime(startd, "%Y-%m-%d").date()
	enddate = datetime.strptime(endd, "%Y-%m-%d").date()
	is_taken=False
	prop=Training.objects.all().filter(semail=request.user.email).exclude(startd=startdate)
	pro=prop.exclude(endd=enddate)
	for i in range(0,len(pro)):
		if(startdate>pro[i].startd and startdate<pro[i].endd):
			is_taken=True
		elif(startdate<pro[i].startd and enddate>pro[i].startd):
			is_taken=True
		elif(enddate>pro[i].startd and enddate<pro[i].endd):
			is_taken=True
	data = {
		'is_taken': is_taken
	}
	return JsonResponse(data)







def search_text(request):
    if request.method == "GET":
        search_text = request.GET.get('search_text',False)
        if search_text is not None and search_text != u"":
            search_text = request.GET.get('search_text',False)
            k=' '
            if k in search_text:
                s,x=search_text.split()
                z = Info.objects.all().filter(First_name=s,valid=True).exclude(Email=request.user.email)
                statuss=z.filter(Last_name__contains=x)


            else:
                statuss = Info.objects.filter(First_name__contains=search_text,valid=True).exclude(Email=request.user.email)

        else:
            statuss = []
        return render(request,"ajaxsearch.html",{'statuss':statuss})


def resumemaker(request):
    obj=get_object_or_404(Info,Email=request.user.email)
    p=project.objects.all().filter(semail=request.user.email)
    j=Sjob.objects.all().filter(semail=request.user.email)
    i=Intern.objects.all().filter(semail=request.user.email)
    t=Training.objects.all().filter(semail=request.user.email)
    s=Skill.objects.all().filter(semail=request.user.email)
    formp=Projectform( request.POST or None )
    formj=Jobform(request.POST or None)
    formi=Internshipform(request.POST or None)
    formsk=Skillform(request.POST or None)
    formt=Trainingform(request.POST or None)
    return render(request,'resume1.html',{'formp':formp,'formj':formj,'formt':formt,'formi':formi,'forms':formsk
                                         ,'pro':p,'job':j,'intern':i,'train':t,'skill':s,'obj':obj})

def rpro(request):
	form=Projectform(request.POST)
	if form.is_valid():
		startdate = form.cleaned_data.get('startd')
		enddate = form.cleaned_data.get('endd')
		pro = project.objects.all().filter(semail=request.user.email)
		for i in range(0, len(pro)):
			if (startdate > pro[i].startd and startdate < pro[i].endd):
				return redirect('/rmaker')
			elif (startdate < pro[i].startd and enddate > pro[i].startd):
				return redirect('/rmaker')
			elif (enddate > pro[i].startd and enddate < pro[i].endd):
				return redirect('/rmaker')
		f = form.save(commit=False)
		f.semail = request.user.email
		f.save()
		return redirect('/rmaker')
	else:

		return redirect('/rmaker')


def rjob(request):
	form = Jobform(request.POST)
	if form.is_valid():
		startdate=form.cleaned_data.get('startd')
		enddate=form.cleaned_data.get('endd')
		pro = Sjob.objects.all().filter(semail=request.user.email)
		for i in range(0, len(pro)):
			if (startdate > pro[i].startd and startdate < pro[i].endd):
				return redirect('/rmaker')
			elif (startdate < pro[i].startd and enddate > pro[i].startd):
				return redirect('/rmaker')
			elif (enddate > pro[i].startd and enddate < pro[i].endd):
				return redirect('/rmaker')
		f = form.save(commit=False)
		f.semail = request.user.email
		f.save()
		return redirect('/rmaker')
	else:

		return redirect('/rmaker')


def rtra(request):
	form = Trainingform(request.POST)
	if form.is_valid():
		startdate = form.cleaned_data.get('startd')
		enddate = form.cleaned_data.get('endd')
		pro = Training.objects.all().filter(semail=request.user.email)
		for i in range(0, len(pro)):
			if (startdate > pro[i].startd and startdate < pro[i].endd):
				return redirect('/rmaker')
			elif (startdate < pro[i].startd and enddate > pro[i].startd):
				return redirect('/rmaker')
			elif (enddate > pro[i].startd and enddate < pro[i].endd):
				return redirect('/rmaker')
		f = form.save(commit=False)
		f.semail = request.user.email
		f.save()
		return redirect('/rmaker')
	else:

		return redirect('/rmaker')


def rint(request):
	form = Internshipform(request.POST)
	if form.is_valid():
		startdate = form.cleaned_data.get('startd')
		enddate = form.cleaned_data.get('endd')
		pro = Intern.objects.all().filter(semail=request.user.email)
		for i in range(0, len(pro)):
			if (startdate > pro[i].startd and startdate < pro[i].endd):
				return redirect('/rmaker')
			elif (startdate < pro[i].startd and enddate > pro[i].startd):
				return redirect('/rmaker')
			elif (enddate > pro[i].startd and enddate < pro[i].endd):
				return redirect('/rmaker')
		f = form.save(commit=False)
		f.semail = request.user.email
		f.save()
		return redirect('/rmaker')
	else:

		return redirect('/rmaker')


def rskill(request):
	form = Skillform(request.POST)
	if form.is_valid():
		skill=form.cleaned_data.get('skill')
		if Skill.objects.filter(skill__iexact=skill).filter(semail__iexact=request.user.email).exists():
			return redirect('/rmaker')
		f = form.save(commit=False)
		f.semail = request.user.email
		f.save()
		return redirect('/rmaker')
	else:

		return redirect('/rmaker')



def skilleditv(request, id):
	instance = get_object_or_404(Skill, id=id)
	form = Skillform(request.POST or None, instance=instance)
	if form.is_valid():
		skill = form.cleaned_data.get('skill')
		if Skill.objects.filter(skill__iexact=skill).filter(semail__iexact=request.user.email).exclude(id=id).exists():
			return redirect('/rmaker')
		update_post = form.save(commit=False)
		update_post.save()
		return redirect('/rmaker/')
	context = {
		'forms': form
	}
	return render(request, 'editpic.html', context)


def traineditv(request, id):
	instance = get_object_or_404(Training, id=id)
	form = Trainingform(request.POST or None, instance=instance)
	if form.is_valid():
		startdate = form.cleaned_data.get('startd')
		enddate = form.cleaned_data.get('endd')
		pro = Sjob.objects.all().filter(semail=request.user.email).exclude(id=id)
		for i in range(0, len(pro)):
			if (startdate > pro[i].startd and startdate < pro[i].endd):
				return redirect('/rmaker')
			elif (startdate < pro[i].startd and enddate > pro[i].startd):
				return redirect('/rmaker')
			elif (enddate > pro[i].startd and enddate < pro[i].endd):
				return redirect('/rmaker')
		update_post = form.save(commit=False)
		update_post.save()
		return redirect('/rmaker/')
	context = {
		'formt': form
	}
	return render(request, 'editrain.html', context)

def proeditv(request, id):
	instance = get_object_or_404(project, id=id)
	form = Projectform(request.POST or None, instance=instance)
	if form.is_valid():
		startdate = form.cleaned_data.get('startd')
		enddate = form.cleaned_data.get('endd')
		pro = Sjob.objects.all().filter(semail=request.user.email).exclude(id=id)
		for i in range(0, len(pro)):
			if (startdate > pro[i].startd and startdate < pro[i].endd):
				return redirect('/rmaker')
			elif (startdate < pro[i].startd and enddate > pro[i].startd):
				return redirect('/rmaker')
			elif (enddate > pro[i].startd and enddate < pro[i].endd):
				return redirect('/rmaker')
		update_post = form.save(commit=False)
		update_post.save()
		return redirect('/rmaker/')

	context = {
		'formt': form
	}
	return render(request, 'editpro.html', context)

def interneditv(request, id):
	instance = get_object_or_404(Intern, id=id)
	form = Internshipform(request.POST or None, instance=instance)
	if form.is_valid():
		startdate = form.cleaned_data.get('startd')
		enddate = form.cleaned_data.get('endd')
		pro = Intern.objects.all().filter(semail=request.user.email).exclude(id=id)
		for i in range(0, len(pro)):
			if (startdate > pro[i].startd and startdate < pro[i].endd):
				return redirect('/rmaker')
			elif (startdate < pro[i].startd and enddate > pro[i].startd):
				return redirect('/rmaker')
			elif (enddate > pro[i].startd and enddate < pro[i].endd):
				return redirect('/rmaker')
		update_post = form.save(commit=False)
		update_post.save()
		return redirect('/rmaker/')
	context = {
		'formt': form
	}
	return render(request, 'editintern.html', context)

def jobeditv(request, id):
	instance = get_object_or_404(Sjob, id=id)
	form = Jobform(request.POST or None, instance=instance)
	if form.is_valid():
		startdate = form.cleaned_data.get('startd')
		enddate = form.cleaned_data.get('endd')
		pro = Sjob.objects.all().filter(semail=request.user.email).exclude(id=id)
		for i in range(0, len(pro)):
			if (startdate > pro[i].startd and startdate < pro[i].endd):
				return redirect('/rmaker')
			elif (startdate < pro[i].startd and enddate > pro[i].startd):
				return redirect('/rmaker')
			elif (enddate > pro[i].startd and enddate < pro[i].endd):
				return redirect('/rmaker')
		update_post = form.save(commit=False)
		update_post.save()
		return redirect('/rmaker/')
	context = {
		'formt': form
	}
	return render(request, 'editjob.html', context)

def tresume(request,id=None):
	obj=get_object_or_404(Info,id=id)
	p=project.objects.all().filter(semail=obj.Email)
	j=Sjob.objects.all().filter(semail=obj.Email)
	i=Intern.objects.all().filter(semail=obj.Email)
	t=Training.objects.all().filter(semail=obj.Email)
	s=Skill.objects.all().filter(semail=obj.Email)
	return render(request,'tresume.html',{'pro':p,'job':j,'intern':i,'train':t,'skill':s,'obj':obj})
def deletejob(request,id):
	j=get_object_or_404(Sjob,id=id)
	j.delete()
	return redirect('/rmaker')

def deletetrain(request,id):
	j=get_object_or_404(Training,id=id)
	j.delete()
	return redirect('/rmaker')
def deleteskill(request,id):
	j=get_object_or_404(Skill,id=id)
	j.delete()
	return redirect('/rmaker')
def deletepro(request,id):
	j=get_object_or_404(project,id=id)
	j.delete()
	return redirect('/rmaker')
def deleteint(request,id):
	j=get_object_or_404(Intern,id=id)
	j.delete()
	return redirect('/rmaker')

def send_friend_request0(request, id, name):
	if request.user.is_authenticated:
		user = get_object_or_404(User, id=id)
		frequest, created = FriendRequest.objects.get_or_create(
			from_user=request.user,
			to_user=user)
		url = reverse('uprof', kwargs={'user': name})

		return HttpResponseRedirect(url)

def cancel_friend_request0(request, id, name):
	if request.user.is_authenticated:
		user = get_object_or_404(User, id=id)
		frequest = FriendRequest.objects.filter(
			from_user=request.user,
			to_user=user).first()
		frequest.delete()
		url = reverse('uprof', kwargs={'user': name})

		return HttpResponseRedirect(url)


def send_friend_request1(request, id,id2):
	if request.user.is_authenticated:
		user = get_object_or_404(User, id=id)
		frequest, created = FriendRequest.objects.get_or_create(
			from_user=request.user,
			to_user=user)
		url = reverse('uprof1', kwargs={'id': id2})

		return HttpResponseRedirect(url)


def cancel_friend_request1(request, id,id2):
	if request.user.is_authenticated:
		user = get_object_or_404(User, id=id)
		frequest = FriendRequest.objects.filter(
			from_user=request.user,
			to_user=user).first()
		frequest.delete()
		url = reverse('uprof1', kwargs={'id': id2})

		return HttpResponseRedirect(url)

def postjobt(request):
	if request.user.is_authenticated:
		form = JobForm(request.POST or None)
		if form.is_valid():
			flag = 0
			countr = 0
			countc = 0
			cn = form.cleaned_data.get('Company_name')
			jt = form.cleaned_data.get('Job_title')
			loc = form.cleaned_data.get('Location')
			ar = form.cleaned_data.get('About_role')
			ac = form.cleaned_data.get('About_company')
			if (any(c.isalpha() for c in cn) == False):
				flag = 1

			elif (any(c.isalpha() for c in loc) == False):
				flag = 1

			elif (any(c.isnumeric() for c in jt) == False):
				flag = 1

			for i in ar:
				if i.isalpha():
					countr = countr + 1

			for i in ac:
				if i.isalpha():
					countc = countc + 1

			if countr < 6:
				flag = 1
			elif countc < 6:
				flag = 1

			if flag == 1:
				return redirect('/demo')

			new_post = form.save(commit=False)
			new_post.Deadline = request.POST.get('date')
			new_post.Your_name = "TPO"
			new_post.Email = request.user.email
			new_post.save()
			return redirect('/tpo/')
		context = {
			'form': form}
		return render(request, 'postjobt.html', context)
	else:
		return redirect('/login/')


def validatecn(request):
	field = request.GET.get('field', None)
	is_taken=any(c.isalpha() for c in field)
	if is_taken==False:
		is_taken=True
	else:
		is_taken=False
	print(is_taken)
	data = {
		'is_taken': is_taken
	}
	return JsonResponse(data)

def validatejt(request):
	field = request.GET.get('field', None)
	is_taken=any(c.isnumeric() for c in field)
	print(is_taken)
	data = {
		'is_taken': is_taken
	}
	return JsonResponse(data)

def validateloc(request):
	field = request.GET.get('field', None)
	is_taken=any(c.isalpha() for c in field)
	if is_taken==False:
		is_taken=True
	else:
		is_taken=False
	data = {
		'is_taken': is_taken
	}
	return JsonResponse(data)
def validatear(request):
	field = request.GET.get('field', None)
	count=0
	for i in field:
		if i.isalpha():
			count+=1
	if count<6:
		is_taken=True

	else:
		is_taken=False
	data = {
		'is_taken': is_taken
	}
	return JsonResponse(data)
def validateac(request):
	field = request.GET.get('field', None)
	count = 0
	for i in field:
		if i.isalpha():
			count += 1
	if count < 6:
		is_taken = True

	else:
		is_taken = False
	data = {
		'is_taken': is_taken
	}
	return JsonResponse(data)
