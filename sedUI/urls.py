from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.decorators import login_required, permission_required
from sedUI.forms import RegistrationForm1, RegistrationForm2, RegistrationForm3, RegistrationForm4

urlpatterns=[
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^about/', views.AboutView.as_view(), name='about'),
	url(r'^contact/', views.ContactView.as_view(), name='contact'),


	url(r'^registration/', views.RegistrationWizard.as_view([RegistrationForm1, RegistrationForm2, RegistrationForm3, RegistrationForm4]), name='registration'),

	url(r'^registration1/', views.registration1, name='registration1'),
	url(r'^registration2/', views.registration2, name='registration2'),
	url(r'^registration3/', views.registration3, name='registration3'),
	url(r'^registration4/', views.registration4, name='registration4'),
	url(r'^registration5/', views.registration5, name='registration5'),
	
	url(r'^scouts/', login_required(views.ScoutView.as_view()), name='scout'),
	# url(r'^scout/(?P<scout_id>)/', views.ScoutDetailView.as_view(), name='scout_detail'),
	url(r'^courses/', views.CourseView.as_view(), name='course'),
	# url(r'^course/(?P<class_id>)', views.CourseDetailView.as_view(), name='course_detail'),
	url(r'^reportAnalysis/$', login_required(views.ReportView.as_view()), name='reportAnalysis'),
	# url(r'^reportAnalysis/(?P<class_id>)', login_required(views.ReportViewDetail.as_view(), name='reportAnalysisDetail'),
	url(r'^profile/', login_required(views.ProfileView.as_view()), name='profiles'),



	#might need to look into class based view for later interation
    url(r'^login/$', auth_views.login, {'template_name': 'sedUI/pages/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'sedUI/pages/logged_out.html'}, name='logout'),

]
