from django.shortcuts import render, get_object_or_404
from .models import Job

# Create your views here.

def job_ls(request):
	''' view for listing jobs'''
	jobs = Job.objects.all().order_by('-posted_on')
	return render(request, 'job_ls.html', {'jobs': jobs})

def job_detail(request, job_id):
	''' view for job details '''
	job = get_object_or_404(Job, id=job_id)
	return render(request, 'job_detail.html', {'job': job})


