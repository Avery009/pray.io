from django.urls import path

from . import views

urlpatterns = [
	path('', views.latest, name = 'Latest Requests'),
	path('prayedfor/', views.mostprayedfor, name='Most Prayed For'),
	path('answered/', views.recentlyanswered, name='Answered Prayers'),
	path('<int:prayer_id>/', views.individual, name='Pray'),
]
