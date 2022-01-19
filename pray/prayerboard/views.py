from django.shortcuts import render

# Create your views here.
def latest(request):
	#Retrieve top 20 latest prayers -- modify retrieval 
	latest_prayer_list = Prayer.objects.all()
	template = loader.get_template('prayerboard.html')
	context = {
		'latest_prayer_list' : latest_prayer_list
	}
	return HttpResponse(template.render(context,request))

def mostprayedfor(request):
        #Retrieve top 20 most active prayers -- modify retrieval 
        latest_prayer_list = Prayer.objects.all()
        template = loader.get_template('prayerboard.html')
        context = {
                'latest_prayer_list' : latest_prayer_list
        }
        return HttpResponse(template.render(context,request))

def recentlyanswered(request):
        #Retrieve top 20 latest answered prayers -- modify retrieval 
        latest_prayer_list = Prayer.objects.all()
        template = loader.get_template('prayerboard.html')
        context = {
                'latest_prayer_list' : latest_prayer_list
        }
        return HttpResponse(template.render(context,request))
