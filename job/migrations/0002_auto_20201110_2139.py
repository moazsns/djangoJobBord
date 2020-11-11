# Generated by Django 3.1.3 on 2020-11-11 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='descriotion',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Full_time', 'Full_time'), ('Part_time', 'Part_time')], default='', max_length=15),
            preserve_default=False,
        ),
    ]
