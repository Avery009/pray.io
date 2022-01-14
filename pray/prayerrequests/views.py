from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Prayer
from .forms import forms
from django.template import loader
# Create your views here.

def index(request):
	latest_prayer_list = Prayer.objects.all()
	template = loader.get_template('prayerrequests/index.html')
	context = {
		'latest_prayer_list' : latest_prayer_list
	}
	return HttpResponse(template.render(context,request))

def detail(request, prayer_id):
	try:
		prayer = Prayer.objects.get(pk=prayer_id)
	except Prayer.DoesNotExist:
		raise Http404('Prayer ID not located')
	return render(request, 'prayerrequests/detail.html', {'prayer' : prayer})

def example(request):
	template = loader.get_template('prayerrequests/components00.html')
	context = {}
	return HttpResponse(template.render(context,request))
def prayerrequestinput(request):
	form = forms.PrayerRequestForm()
	return render(request, 'prayerrequestinputform.html',{'form': form})
