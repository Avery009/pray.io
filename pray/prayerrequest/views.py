from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from .models import Prayer
from .forms import forms
from django.template import loader

# Create your views here.

def viewprayerrequests(request):
	#Load completed and current as separate lists
	user_current_prayer_list = Prayer.objects.all()
	user_answered_prayer_list = Prayer.objects.all()
	template = loader.get_template('viewprayerrequests.html')
	print(user_current_prayer_list)
	context = {
		'prayer_list' : user_current_prayer_list,
		'answered_prayer_list': user_answered_prayer_list
	}
	return HttpResponse(template.render(context,request))
	

def prayerrequestinput(request):
	if request.method == 'GET':
		form = forms.PrayerRequestForm()
		return render(request, 'prayerrequestform.html',{'form': form})
	elif request.method == 'POST':
		#prayer_request_date = request.POST['prayer_request_date']
		#prayer_answer_date = request.POST['prayer_answer_date']
		#prayer_description = request.POST['prayer_description']
		#prayer_recipients = request.POST['prayer_recipients']
		#prayer_recipients_email = request.POST['prayer_recipients_email']
		#prayer_categories = request.POST['prayer_categories']
		#prayer_answered = request.POST['prayer_answered']
		#prayer_updates = request.POST['prayer_updates']
		#prayer_image = request.POST['prayer_image']
		#prayer_answered_image = request.POST['prayer_answered_image']
		#validate each field in some way to account for SQL injection, etc.
		form = forms.PrayerRequestForm(request.POST)
		print(request.POST)
		print(form.errors)
		if form.is_valid():
			#prayer = form.save(commit=False)
			#prayer.prayer_request_date = request.prayer_request_date
			#prayer.prayer_answer_date = request.prayer_answer_date
			#prayer.prayer_description = request.prayer_description
			#prayer.prayer_recipients = request.prayer_recipients
			#prayer.prayer_recipients_email = request.prayer_recipients_email
			#prayer.prayer_categories = request.prayer_categories
			#prayer.prayer_answered = request.prayer_answered
			#prayer.prayer_updates = request.prayer_updates
			#prayer.prayer_image = request.prayer_image
			#prayer.prayer_answered_image = request.prayer_answered_image
			form.save()
			return redirect('/requests/success')
		else:
			context = {
				'error' : 501
			}
			template = loader.get_template('error.html')
			return HttpResponse(template.render(context,request))

def prayerrequestedit(request,prayer_id):
	if request.method == 'GET':
		form = forms.PrayerRequestEditForm()
		return render(request, 'prayerrequestform.html',{'form': form})
	elif request.method == 'POST':
		#prayer_request_date = request.POST['prayer_request_date']
		#prayer_answer_date = request.POST['prayer_answer_date']
		#prayer_description = request.POST['prayer_description']
		#prayer_recipients = request.POST['prayer_recipients']
		#prayer_recipients_email = request.POST['prayer_recipients_email']
		#prayer_categories = request.POST['prayer_categories']
		#prayer_answered = request.POST['prayer_answered']
		#prayer_updates = request.POST['prayer_updates']
		#prayer_image = request.POST['prayer_image']
		#prayer_answered_image = request.POST['prayer_answered_image']
		#validate each field in some way to account for SQL injection, etc.
		form = forms.PrayerRequestEditForm(request.POST)
		if form.is_valid():
			#prayer = form.save(commit=False)
			prayer_request_date = form.cleaned_data.get('prayer_request_date')
			prayer_answer_date = form.cleaned_data.get('prayer_answer_date')
			prayer_description = form.cleaned_data.get('prayer_description')
			prayer_recipients = form.cleaned_data.get('prayer_recipients')
			prayer_recipients_email = form.cleaned_data.get('prayer_recipients_email')
			prayer_categories = form.cleaned_data.get('prayer_categories')
			prayer_answered = form.cleaned_data.get('prayer_answered')
			prayer_updates = form.cleaned_data.get('prayer_updates')
			prayer_image = form.cleaned_data.get('prayer_image')
			prayer_answered_image = form.cleaned_data.get('prayer_answered_image')
			#prayer.save()
			return redirect('/success')
		else:
			context = {
				'error' : 501
			}
			template = loader.get_template('error.html')
			return HttpResponse(template.render(context,request))
def success(request):
	template = loader.get_template('success.html')
	context = {
		#Add in username and prayer_id to validate successful DB entry
	}		
	return HttpResponse(template.render(context,request))
