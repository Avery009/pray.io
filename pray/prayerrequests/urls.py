from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('specifics/<int:prayer_id>/', views.detail, name='prayerrequest'),
	path('example/', views.example, name = 'example'),
	path('request/', views.prayerrequestinput, name='Submit Prayer Request'),
]
