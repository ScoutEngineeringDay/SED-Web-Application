from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$', views.index, name='index'),
	url(r'^about/', views.about, name='about'),
	url(r'^contact/', views.contact, name='contact'),
	url(r'^registration/', views.registration, name='registration'),
	url(r'^scouts/', views.scouts, name='scouts'),
	url(r'^courses/$', views.courses, name='courses'),
	#url(r'^course/(?P<class_id>)$', views.course_detail, name='course_detail'),
	url(r'^profile/', views.profile, name='profiles'),
	url(r'^loginOrRegister/', views.loginOrRegister, name='loginOrRegister'),
]
