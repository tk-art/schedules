# Generated by Django 3.2.23 on 2023-12-30 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0024_alter_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrequest',
            name='eventId',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
