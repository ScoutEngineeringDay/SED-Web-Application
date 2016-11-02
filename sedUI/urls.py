from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$', views.index, name='index'),
	url(r'^about/', views.about, name='about'),
	url(r'^contact/', views.contact, name='contact'),
	url(r'^registration1/', views.registration1, name='registration1'),
	url(r'^registration2/', views.registration2, name='registration2'),
	url(r'^registration3/', views.registration3, name='registration3'),
	url(r'^registration4/', views.registration4, name='registration4'),
	url(r'^registration5/', views.registration5, name='registration5'),
	url(r'^scouts/', views.scouts, name='scouts'),
	url(r'^courses/$', views.courses, name='courses'),
	url(r'^reportAnalysis/$', views.reportAnalysis, name='reportAnalysis'),
	#url(r'^course/(?P<class_id>)$', views.course_detail, name='course_detail'),
	url(r'^profile/', views.profile, name='profiles'),
	url(r'^loginOrRegister/', views.loginOrRegister, name='loginOrRegister'),
]
