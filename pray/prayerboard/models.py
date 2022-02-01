from django.db import models

# Create your models here.
class Prayer(models.Model):
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
	prayerCategoriesDefault = [('thanks'),('Thanksgiving')]
	prayer_id = models.BigAutoField(primary_key=True,unique=True)
	prayer_request_date = models.DateTimeField('prayer request date')
	prayer_answer_date = models.DateTimeField('prayer answer date',blank=True,null=True)
	prayer_description = models.CharField(max_length=1000)
	prayer_recipients = models.CharField(max_length=100,blank=True,null=True)
	prayer_recipients_email = models.EmailField(max_length=100,blank=True,null=True)
	#prayer_categories = models.ManyToManyField(choices=prayerCategories,max_length=100,blank=False,default=prayerCategoriesDefault)
	prayer_answered = models.BooleanField(editable=True)
	prayer_updates = models.CharField(max_length=1400,blank=True,null=True)
	prayer_image = models.ImageField(upload_to='prayer_images/%Y/%m/%d',blank=True,null=True)
	prayer_answered_image = models.ImageField(upload_to='answered_prayer_images/%Y/%m/%d',blank=True,null=True)
	prayer_count = models.IntegerField('prayer count',blank=False,editable=False)
	def __str__(self):
		return self.prayer_id
