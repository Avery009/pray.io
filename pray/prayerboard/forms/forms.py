from django import forms
from django.core.files.uploadedfile import SimpleUploadedFile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
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
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'id-PrayerRequestViewForm'
		self.helper.form_class = 'blueForms'
		self.helper.form_method = 'get'
		self.helper.form_action = '' #url format to view individual requests (requests/{prayer_id})
		self.helper.layout = Layout(
			FormActions(
				Submit('pray',css_class='btn-success')
			)
		)
