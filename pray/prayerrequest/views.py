from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Prayer
from .forms import forms
from django.template import loader

# Create your views here.

def viewprayerrequests(request):
	#Load completed and current as separate lists
	latest_prayer_list = Prayer.objects.all()
	template = loader.get_template('viewprayerrequests.html')
	context = {
		'latest_prayer_list' : latest_prayer_list
	}
	return HttpResponse(template.render(context,request))
	

def prayerrequestinput(request):
	form = forms.PrayerRequestForm()
	return render(request, 'prayerrequestinputform.html',{'form': form})

def prayerrequestedit(request):
	form = forms.PrayerRequestEditForm()
	return render(request, 'prayerrequesteditform.html',{'form': form})
