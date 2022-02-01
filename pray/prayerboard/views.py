from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from prayerrequest.models import Prayer
from django.template import loader
from .forms import forms
# Create your views here.

def home(request):
	template = loader.get_template('home.html')
	context = {}
	return HttpResponse(template.render(context,request))

def latest(request):
	#Retrieve top 20 latest prayers -- modify retrieval 
	latest_prayer_list = Prayer.objects.all()
	template = loader.get_template('prayerboard.html')
	context = {
		'prayer_list' : latest_prayer_list
	}
	return HttpResponse(template.render(context,request))

def mostprayedfor(request):
        #Retrieve top 20 most active prayers -- modify retrieval 
        most_prayer_list = Prayer.objects.all()
        template = loader.get_template('prayerboard.html')
        context = {
                'prayer_list' : most_prayer_list
        }
        return HttpResponse(template.render(context,request))

def recentlyanswered(request):
        #Retrieve top 20 latest answered prayers -- modify retrieval 
        recent_prayer_list = Prayer.objects.all()
        template = loader.get_template('prayerboard.html')
        context = {
                'prayer_list' : recent_prayer_list
        }
        return HttpResponse(template.render(context,request))

def individual(request,prayer_id):
	#View an individual prayer to pray for it
	if request.method == 'GET':
		try:
			prayer = Prayer.objects.get(pk=prayer_id)
			form = forms.PrayerRequestViewForm
			template = loader.get_template('viewprayerrequest.html')
			context = {
				'prayer' : prayer
			}
			return HttpResponse(template.render(context,request))
		except Prayer.DoesNotExist:
			raise Http404("Prayer ID is not in database")
	else:
		context = {
				'error' : 501
		}
		template = loader.get_template('error.html')
		return HttpResponse(template.render(context,request))
		
		
