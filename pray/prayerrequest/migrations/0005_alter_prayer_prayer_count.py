# Generated by Django 3.2.4 on 2022-01-31 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prayerrequest', '0004_prayer_prayer_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prayer',
            name='prayer_count',
            field=models.IntegerField(editable=False, null=True),
        ),
    ]