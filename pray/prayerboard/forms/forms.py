from django import forms
from django.core.files.uploadedfile import SimpleUploadedFile
from ..models import Prayer


#Form to view individual public request and pray for it
class PrayerRequestViewForm(forms.ModelForm):
	class Meta:
		model = Prayer
		exclude = ('prayer_id','prayer_recipients','prayer_recipients_email','prayer_categories')
	prayer_id = forms.CharField(label = 'ID', max_length = 100)
	prayer_request_date = forms.DateTimeField(required=True,disabled=True)
	prayer_answer_date = forms.DateTimeField(required=False,disabled=True)
	prayer_description = forms.CharField(max_length = 1000, required = True, widget=forms.Textarea,disabled=True)
	prayer_recipients = forms.CharField(max_length = 100, required = False)
	prayer_recipients_email = forms.CharField(max_length = 100, required = False)
	#prayer_categories = forms.MultipleChoiceField(required=True,widget=forms.CheckboxSelectMultiple,choices=prayerCategories)
	prayer_answered = forms.BooleanField(required=False,disabled=True)
	prayer_updates = forms.CharField(max_length = 1400,required=False,widget=forms.Textarea,disabled=True)
	prayer_image = forms.ImageField(required=False,disabled=True)
	prayer_answered_image = forms.ImageField(required=False,disabled=True)
	prayer_count = forms.IntegerField(disabled=True,widget=forms.NumberInput)
