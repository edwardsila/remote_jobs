from django.db import models

# Create your models here.

class Job(models.Model):
	title = models.CharField(max_length=255)
	company = models.CharField(max_length=255)
	location = models.CharField(max_length=100, default="Remote")
	job_type = models.CharField(max_length=50, choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Contract', 'Contract')])
	description = models.CharField(max_length=250, default='', blank=True,
                                   null=True)
	requirements = models.CharField(max_length=250, default='', blank=True,
                                   null=True)
	link_to_apply = models.URLField(max_length=200)
	posted_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
