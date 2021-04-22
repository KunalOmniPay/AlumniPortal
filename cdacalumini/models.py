from django.db import models
from django.utils import timezone
import datetime
from .validators import validate_file_extension
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
# Create your models here.
import django.utils
from datetime import date

class Info(models.Model):
    Role=(
        ('','Role'),
        ('Intern','Intern'),

        ('Trainee','Trainee')
    )
    Technology=(
        ('','Technology'),
        ('Python','Python'),
        ('Big data','Big data'),
        ('Java','java'),
        ('Data science','Data science'),
        ('IOT','IOT'),
        ('Security','Security')
    )
    Batch=(
        ('','Batch'),
        ('2010','2010'),
        ('2011','2011'),
        ('2012','2012'),
        ('2013','2013'),
        ('2014','2014'),
        ('2015','2015'),
        ('2016','2016'),
        ('2017','2017'),
        ('2018','2018'),
        ('2019','2019')
    )
    Gender=(
        ('','Gender'),
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other')
    )

    degree=(
        ('', 'Degree'),
        ('B.Tech', 'B.Tech'),
        ('M.Tech', 'M.Tech'),
        ('B.Ca', 'B.CA'),
        ('M.Ca', 'M.Ca')
    )
    Role = models.CharField(choices=Role, max_length=50,blank=False)
    Technology = models.CharField(choices=Technology, max_length=50, blank=False)
    Batch = models.CharField(choices=Batch, max_length=50, blank=False)
    Profile_photo = models.ImageField(upload_to='media/', blank=False)
    Gender = models.CharField(choices=Gender, max_length=50, blank=False)
    City = models.CharField(max_length=20, blank=False)
    Mobile_no = models.CharField(max_length=12, blank=False)
    Address = models.CharField(blank=False, max_length=50)
    First_name = models.CharField(blank=False, max_length=50)
    Last_name = models.CharField(blank=False, max_length=50)
    Email = models.EmailField(max_length=50, blank=False)
    College = models.CharField(max_length=200, blank=False)
    Degree = models.CharField(max_length=50, choices=degree, blank=False)
    Department = models.CharField(max_length=200,blank=False)
    valid = models.BooleanField(default=False)

def no_future(value):
    today = date.today()
    if value > today:
        raise ValidationError('Purchase_Date cannot be in the future.')

class Job(models.Model):
    Company_name = models.CharField(max_length=50, blank=False)
    Job_title = models.CharField(max_length=50, blank=False)
    Location = models.CharField(max_length=20, blank=False)
    Deadline = models.DateField(blank=False,validators=[no_future])
    Salary = models.CharField(max_length=20, blank=False)
    link = models.CharField(max_length=20, blank=True)
    About_company = models.TextField(blank=False)
    About_role = models.TextField(blank=False)
    Your_name = models.CharField(max_length=50, blank=False)
    Email = models.EmailField(max_length=50, blank=False)
    Currentdate=models.DateField(default=timezone.now)

def user_directory_path(instance, filename):
    return 'media/resume/{0}_{1}/{2}'.format(instance.user.username,instance.user.id, filename)
class Apply_job(models.Model):
    Company_name = models.CharField(max_length=50, blank=False)
    Job_title = models.CharField(max_length=50, blank=False)
    Posted_by = models.CharField(max_length=50, blank=False)
    Email_post = models.EmailField(max_length=50, blank=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Email_apply = models.EmailField(max_length=50, blank=False)
    Apply_date = models.DateField(default=timezone.now)
    Deadline = models.DateField(blank=False)
    resume = models.FileField(upload_to=user_directory_path,validators=[validate_file_extension], blank=False)
    Salary = models.CharField(max_length=20,null=True, blank=True)
    About_company = models.TextField(blank=True,null=True)
    About_role = models.TextField(null=True,blank=True)
    Location = models.CharField(null=True,max_length=20, blank=True)
    Mobile_no = models.CharField(max_length=12, blank=True,null=True)
    selected = models.BooleanField(default=False)






class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    slug = models.SlugField()
    friends = models.ManyToManyField("Profile", blank=True)

    def __str__(self):
        return str(self.user.username)

    def get_absolute_url(self):
    	return "/users/{}".format(self.slug)


def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except:
            pass

post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)


class FriendRequest(models.Model):
	to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='to_user',on_delete=models.CASCADE)
	from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='from_user',on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True) # set when created

	def __str__(self):
		return "From {}, to {}".format(self.from_user.username, self.to_user.username)


class Message(models.Model):
    to_user = models.CharField(blank=True,max_length=50)
    from_user = models.CharField(blank=True,max_length=50)
    message = models.TextField(blank=True,null=True)
    datetime = models.DateTimeField(default=timezone.now)



class carousel(models.Model):
    pic1 = models.ImageField(upload_to='media/', blank=False)
    pic2 = models.ImageField(upload_to='media/', blank=False)
    pic3 = models.ImageField(upload_to='media/', blank=False)

class dir(models.Model):
    dir_pic = models.ImageField(upload_to='media/', blank=False)
    message = models.TextField(blank=False)

class testimonial(models.Model):
    tpic = models.ImageField(upload_to='media/', blank=False)
    tmessage = models.TextField(blank=False)
    tname = models.CharField(max_length=50, blank=False)
    tsign = models.ImageField(upload_to='media/', blank=False)

class Con(models.Model):
    phone1 = models.IntegerField(blank=False)
    phone2 = models.IntegerField(blank=False)
    email = models.EmailField(max_length=50,blank=False)
    location = models.TextField(blank=False)

class project(models.Model):
    semail=models.CharField(max_length=50,blank=False)
    title=models.CharField(max_length=50,blank=False)
    description=models.TextField(max_length=300,blank=False)
    startd = models.DateField(default=django.utils.timezone.now,blank=False)
    endd = models.DateField(default=django.utils.timezone.now,blank=False)
    link=models.CharField(max_length=100,blank=True)

class Skill(models.Model):
    lev=(('','level'),('beginner','beginner'),('Intermediate','Intermdeiate'),('Advanced','Advanced'))
    skill=models.CharField(max_length=50,blank=False)
    semail = models.CharField(max_length=50, blank=False)
    level=models.CharField(choices=lev,max_length=100,default='beginner',blank=False)

class Intern(models.Model):
    semail=models.CharField(max_length=50,blank=False)
    profile=models.CharField(max_length=50,blank=False)
    organisation = models.CharField(max_length=50, blank=False)
    description=models.TextField(max_length=300,blank=False)
    startd = models.DateField(default=django.utils.timezone.now,blank=False)
    endd = models.DateField(default=django.utils.timezone.now,blank=False)

class Training(models.Model):
    semail=models.CharField(max_length=50,blank=False)
    program=models.CharField(max_length=50,blank=False)
    organisation = models.CharField(max_length=50, blank=False)
    description=models.TextField(max_length=300,blank=False)
    startd = models.DateField(default=django.utils.timezone.now,blank=False)
    endd = models.DateField(default=django.utils.timezone.now,blank=False)

class Sjob(models.Model):
    semail=models.CharField(max_length=50,blank=False)
    profile=models.CharField(max_length=50,blank=False)
    organisation = models.CharField(max_length=50, blank=False)
    description=models.TextField(max_length=300,blank=False)
    startd=models.DateField(blank=False)
    endd = models.DateField(blank=False)

class Technology(models.Model):
    name=models.CharField(max_length=80,blank=False)

