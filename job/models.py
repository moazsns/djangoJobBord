from django.db import models

# Create your models here.
JOB_TYPE = (
	('Full_time','Full_time'),
	('Part_time','Part_time'))


class Job(models.Model):
 	title = models.CharField(max_length = 100)
 	#location 
 	job_type = models.CharField(max_length = 15 , choices = JOB_TYPE)
 	descriotion = models.TextField(max_length = 1000)
 	published_at = models.DateTimeField(auto_now=True)
 	vacancy = models.IntegerField(default=1)
 	salary = models.IntegerField(default = 0)
 	experiance = models.IntegerField(default = 1)
 	category = models.ForeignKey('Ctegory', on_delete = models.CASCADE)


 	def __str__(self):
 		return self.title


class Ctegory(models.Model):
	name = models.CharField(max_length = 40)

	def __str__(self):
		return self.name