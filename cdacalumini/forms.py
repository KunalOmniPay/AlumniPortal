from django import forms
from bootstrap_modal_forms.forms import BSModalForm
from .models import *
from django.utils import timezone
import datetime
from datetime import datetime
from datetime import date

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100','id':"materialLoginFormEmail"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100', 'id':"materialLoginFormPassword"}))


class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','id':'materialLoginFormuser'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','id':'materialLoginFormPassword'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','id':'materialLoginFormEmail'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','id':'materialLoginFormcPassword'}))


    class Meta:
            model = User
            help_texts = {
                'username': None,
            }
            fields = [
                'username',
                'email',
                'password',
                'confirm_password',

            ]
class ContactForm1(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactForm1, self).__init__(*args, **kwargs)
        self.fields['First_name'].widget.attrs.update({'class': 'form-control','id':'Fname'})
        self.fields['Last_name'].widget.attrs.update({'class': 'form-control','id':'Lname' })
        self.fields['Mobile_no'].widget.attrs.update({'class': 'form-control','id':'Mobile','pattern':'[0-9]+'})
        self.fields['Gender'].widget.attrs.update({'class': 'form-control'})
        self.fields['Address'].widget.attrs.update({'class': 'form-control','id':'Address'})
        self.fields['City'].widget.attrs.update({'class': 'form-control','id':'City'})
        self.fields['Gender'].empty_label = "Please, choose value"

    class Meta:
        model = Info

        fields = [
            'First_name',
            'Last_name',
            'Mobile_no',
            'Gender',
            'Address',
            'City',

        ]


class ContactForm2(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactForm2, self).__init__(*args, **kwargs)
        self.fields['Role'].widget.attrs.update({'class': 'form-control','placeholder': 'Role'})
        self.fields['Technology'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Technology'})
        self.fields['Batch'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Batch'})
        self.fields['Role'].empty_label = 'Please, choose value'

    class Meta:
        model = Info

        fields = [
            'Role',
            'Technology',
            'Batch',
        ]

class ContactForm3(forms.ModelForm):
    class Meta:
        model = Info

        fields = [
            'Profile_photo',
                    ]

class Emailform(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    mobile = forms.CharField()
    message = forms.Textarea()

class JobForm(forms.ModelForm):

        def __init__(self, *args, **kwargs):

            super(JobForm, self).__init__(*args, **kwargs)
            self.fields['Company_name'].widget.attrs.update({'id':'cn','class': 'input-text','placeholder': 'Company Name'})
            self.fields['Job_title'].widget.attrs.update({'id':'jt','class': 'input-text', 'placeholder': 'Job title'})
            self.fields['Location'].widget.attrs.update({'class': 'company','id':'loc', 'placeholder': 'Location'})
            self.fields['link'].widget.attrs.update({'class': 'company','id':'link', 'placeholder': 'Site Link'})
            self.fields['Salary'].widget.attrs.update({'class': 'business','placeholder': 'Salary','pattern':'[0-9]+'})
            self.fields['About_company'].widget.attrs.update({'rows':6,'cols':40,'id':'ac','class': 'md-textarea form-control', 'placeholder': 'Write About Company'})
            self.fields['About_role'].widget.attrs.update({'rows':6,'cols':40,'id':'ar','class': 'md-textarea form-control', 'placeholder': 'Write About Role,Responsibility,Eligibility,etc'})


        class Meta:
            model = Job


            fields = ['Company_name','link','Job_title','Location','Salary','About_company','About_role',]

class Apply_form(forms.ModelForm):
        def __init__(self, *args, **kwargs):
            super(Apply_form, self).__init__(*args, **kwargs)







        class Meta:
            model = Apply_job

            fields =['resume']


class messageform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(messageform, self).__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update( {'rows': 4, 'cols': 40,'class': 'md-textarea form-control','id':'form29'})

    class Meta:
        model=Message
        fields=['message']


class picedit(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(picedit, self).__init__(*args, **kwargs)
        self.fields['First_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'First Name','id':"materialRegisterFormFirstName"})
        self.fields['Last_name'].widget.attrs.update({'class': 'form-control','placeholder': 'Last Name','id':"materialRegisterFormFirstName"})
        self.fields['Batch'].widget.attrs.update({'class': 'form-control','id':"materialRegisterFormEmail"})

    class Meta:
        model=Info
        fields=['First_name','Last_name','Batch']

class contactedit(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(contactedit, self).__init__(*args, **kwargs)
        self.fields['Email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'E-mail','id':"materialRegisterFormFirstName"})
        self.fields['Mobile_no'].widget.attrs.update({'class': 'form-control','placeholder': 'Mobile No.','pattern':'[0-9]+','id':"materialRegisterFormFirstName"})
        self.fields['Address'].widget.attrs.update({'placeholder':'Address','id':"materialRegisterFormEmail"})

    class Meta:
        model=Info
        fields=['Email','Mobile_no','Address']



class eduedit(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(eduedit, self).__init__(*args, **kwargs)
        self.fields['College'].widget.attrs.update({'class': 'form-control', 'placeholder': 'College','id':"materialRegisterFormFirstName"})
        self.fields['Degree'].widget.attrs.update({'class': 'form-control','placeholder': 'Degree','id':"materialRegisterFormFirstName"})
        self.fields['Department'].widget.attrs.update({'class': 'form-control','placeholder': 'Department','id':"materialRegisterFormEmail"})

    class Meta:
        model=Info
        fields=['College','Degree','Department']


class expertedit(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(expertedit, self).__init__(*args, **kwargs)
        self.fields['Role'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Role', 'id': "materialRegisterFormFirstName"})
        self.fields['Technology'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Technology', 'id': "materialRegisterFormFirstName"})

    class Meta:
        model = Info
        fields = ['Role','Technology']


class ContactForm4(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactForm4, self).__init__(*args, **kwargs)
        self.fields['College'].widget.attrs.update({'class': 'form-control','id':'College'})
        self.fields['Degree'].widget.attrs.update({'class': 'form-control'})
        self.fields['Department'].widget.attrs.update({'class': 'form-control','id':'Department'})


    class Meta:
        model = Info

        fields = [
            'College',
            'Degree',
            'Department',
        ]

class Projectform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Projectform, self).__init__(*args, **kwargs)
        self.fields['startd'].widget.attrs.update({'id': 'startd'})
        self.fields['endd'].widget.attrs.update({'id': 'endd'})
        self.fields['title'].widget.attrs.update({'class': 'form-control validate','id':'title'})
        self.fields['description'].widget.attrs.update({'rows': 4, 'cols': 40,'class': 'md-textarea form-control','id':'description'})
        self.fields['link'].widget.attrs.update({'class': 'form-control validate', 'id': 'link'})


    class Meta:
        model = project

        fields = [
            'title',
            'description',
             'endd',
            'startd',
            'link',

        ]
class Jobform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Jobform, self).__init__(*args, **kwargs)
        self.fields['startd'].widget.attrs.update({'id':'startdj'})
        self.fields['endd'].widget.attrs.update({'id':'enddj'})
        self.fields['profile'].widget.attrs.update({'class': 'form-control validate','id':'profile'})
        self.fields['description'].widget.attrs.update({'rows': 4, 'cols': 40,'class': 'md-textarea form-control','id':'descriptionj'})
        self.fields['organisation'].widget.attrs.update({'class': 'form-control validate', 'id': 'organisation'})


    class Meta:
        model = Sjob

        fields = [
            'profile',
            'description',
            'endd',
            'startd',
            'organisation'

        ]
class Skillform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Skillform, self).__init__(*args, **kwargs)
        self.fields['skill'].widget.attrs.update({'class': 'form-control validate','id':'skill'})
        self.fields['level'].widget.attrs.update({'class': 'form-control'})


    class Meta:
        model = Skill

        fields = [
            'skill',
            'level',

        ]
class Trainingform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Trainingform, self).__init__(*args, **kwargs)
        self.fields['startd'].widget.attrs.update({'id': 'startdt'})
        self.fields['endd'].widget.attrs.update({'id': 'enddt'})
        self.fields['program'].widget.attrs.update({'class': 'form-control validate','id':'program'})
        self.fields['description'].widget.attrs.update({'rows': 4, 'cols': 40,'class': 'md-textarea form-control','id':'descriptiont'})
        self.fields['organisation'].widget.attrs.update({'class': 'form-control validate', 'id': 'organisationt'})


    class Meta:
        model = Training

        fields = [
            'program',
            'description',
             'endd',
            'startd',
            'organisation',

        ]
class Internshipform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Internshipform, self).__init__(*args, **kwargs)
        self.fields['startd'].widget.attrs.update({'id': 'startdi'})
        self.fields['endd'].widget.attrs.update({'id': 'enddi'})
        self.fields['profile'].widget.attrs.update({'class': 'form-control validate','id':'profilei'})
        self.fields['description'].widget.attrs.update({'rows': 4, 'cols': 40,'class': 'md-textarea form-control','id':'descriptioni'})
        self.fields['organisation'].widget.attrs.update({'class': 'form-control validate', 'id': 'organisationi'})


    class Meta:
        model = Intern

        fields = [
            'profile',
            'description',
             'endd',
            'startd',
            'organisation',


        ]