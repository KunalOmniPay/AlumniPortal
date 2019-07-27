from django.conf.urls import url,include
from .views import tpo,detail,getcsv,deadjob,activejob
#create your url here
urlpatterns=[

        url(r'^tpo/$',tpo,name='tpo'),
        url(r'^dead/$',deadjob,name='deadjob'),
        url(r'^active/$',activejob,name='activejob'),
        url(r'^detail/(?P<id>\d+)/$',detail, name='detail'),
        url(r'^get/(?P<id>\d+)/$',getcsv, name='getcsv'),

]
