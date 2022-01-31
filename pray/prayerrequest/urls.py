from django.urls import path

from . import views

urlpatterns = [
	path('', views.viewprayerrequests, name = 'View Prayer Requests'),
	path('new/', views.prayerrequestinput, name='Submit Prayer Request'),
	path('edit/<int:prayer_id>', views.prayerrequestedit, name='Edit Prayer Request'),
]
