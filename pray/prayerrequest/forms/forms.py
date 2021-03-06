from django import forms
from django.core.files.uploadedfile import SimpleUploadedFile
from ..models import Prayer

class PrayerRequestForm(forms.ModelForm):
	class Meta:
		model = Prayer
		fields = '__all__'
	prayerCategories = [
		('thanks','Thanksgiving'),
		('healing','Healing'),
		('trauma','Trauma'),
		('conversion','Conversion'),
		('belief','Belief'),
		('strength','Strength'),
		('leaders','Leaders'),
		('needs','Needs'),
		('forgiveness','Forgiveness'),
	]
	template_name = 'prayerrequestform.html'
	prayer_id = forms.CharField(label = 'ID', max_length = 100)
	prayer_request_date = forms.DateTimeField(required=True)
	prayer_answer_date = forms.DateTimeField(required=False)
	prayer_description = forms.CharField(max_length = 1000, required = True, widget=forms.Textarea)
	prayer_recipients = forms.CharField(max_length = 100, required = False)
	prayer_recipients_email = forms.CharField(max_length = 100, required = False)
	#prayer_categories = forms.MultipleChoiceField(required=True,widget=forms.CheckboxSelectMultiple,choices=prayerCategories)
	prayer_answered = forms.BooleanField(required=False)
	prayer_updates = forms.CharField(max_length = 1400,required=False,widget=forms.Textarea)
	prayer_image = forms.ImageField(required=False)
	prayer_answered_image = forms.ImageField(required=False)
	prayer_count = forms.IntegerField(widget=forms.NumberInput)

class PrayerRequestEditForm(forms.Form):
	prayerCategories = [
                ('thanks','Thanksgiving'),
                ('healing','Healing'),
                ('trauma','Trauma'),
                ('conversion','Conversion'),
                ('belief','Belief'),
                ('strength','Strength'),
                ('leaders','Leaders'),
                ('needs','Needs'),
                ('forgiveness','Forgiveness'),
        ]
	template_name = 'prayerrequestform.html'
	prayer_id = forms.CharField(label = 'ID', max_length = 100, disabled=True)
	prayer_request_date = forms.DateTimeField(required=True, disabled=True)
	prayer_answer_date = forms.DateTimeField(required=False)
	prayer_description = forms.CharField(max_length = 1000, required = True, widget=forms.Textarea)
	prayer_recipients = forms.CharField(max_length = 100, required = False)
	prayer_recipients_email = forms.CharField(max_length = 100, required = False)
	#prayer_categories = forms.MultipleChoiceField(required=True,widget=forms.CheckboxSelectMultiple,choices=prayerCategories)
	prayer_answered = forms.BooleanField(required=False)
	prayer_updates = forms.CharField(max_length = 1400,required=False,widget=forms.Textarea)
	prayer_image = forms.ImageField(required=False)
	prayer_count = forms.IntegerField(widget=forms.NumberInput)
