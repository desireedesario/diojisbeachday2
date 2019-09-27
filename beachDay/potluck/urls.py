from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from potluck import views as potluck_views

urlpatterns = [
	url(r'^$', potluck_views.IndexView.as_view(), name="index"),
	# url(r'^user/', potluck_views.UserFormView.as_view(), name="user"),
	# url(r'^potluckitem/', potluck_views.PotluckFormView.as_view(), name="potluckitem"),

	# url(r'^(?P<pk>\d+)/$',potluck_views.DetailView.as_view(), name="detail"),
	# url(r'^(?P<pk>\d+)/results/$', potluck_views.ResultsView.as_view(), name="results"),
	# url(r'^newitem/$', potluck_views.create_potluckitem, name="newitem"),
	# url(r'^(?P<question_id>\d+)/vote/$', potluck_views.vote, name="vote"),
 ]