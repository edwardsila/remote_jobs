from django.shortcuts import render, get_object_or_404, redirect
from .models import Job
from .forms import JobForm
from django.contrib import messages

# Create your views here.

def job_ls(request):
	''' view for listing jobs'''
	jobs = Job.objects.all().order_by('-posted_on')
	return render(request, 'job_ls.html', {'jobs': jobs})

def job_detail(request, job_id):
	''' view for job details '''
	job = get_object_or_404(Job, id=job_id)
	return render(request, 'job_detail.html', {'job': job})


def add_job(request):
	form = JobForm()
	
	if request.method == 'POST':
		form = JobForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Job succesfully added!")
			return redirect(job_ls)
		else:
			form = JobForm()
	return render(request, 'add_job.html', {'form': form})

def login_user(request):
	