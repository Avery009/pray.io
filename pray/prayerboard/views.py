from django.shortcuts import render
from django.http import HttpResponse, Http404
from prayerrequest.models import Prayer
from django.template import loader
# Create your views here.
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
