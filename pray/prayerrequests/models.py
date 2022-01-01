from django.db import models

# Create your models here.

class Prayer(models.Model):
	prayer_id = models.BigAutoField(primary_key=True,unique=True)
	prayer_request_date = models.DateTimeField('prayer request date')
	prayer_answer_date = models.DateTimeField('prayer answer date',blank=True,null=True)
	prayer_description = models.CharField(max_length=1000)
	prayer_recipients = models.CharField(max_length=100)
	prayer_categories = models.CharField(max_length=200,blank=True,null=True)
	prayer_answered = models.BooleanField(editable=True)
	prayer_updates = models.CharField(max_length=1400,blank=True,null=True)
#	prayer_image = models.ImageField()
#	prayer_answered_image = models.ImageField()
	
