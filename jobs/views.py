from django.shortcuts import render, redirect, get_object_or_404
from .models import Job
from .forms import JobForm

def job_list(request):
    jobs = Job.objects.all()
    return render(request, "job_list.html", {"jobs": jobs})

def add_job(request):
    if request.method == "POST":
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("job_list")
    
    else:
        form = JobForm()
    return render(request, "add_job.html", {"form": form})

def edit_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == "POST":
        form = JobForm(request.POST, request.FILES, instance=job)
        if form.is_valid():
            form.save()
            return redirect("job_list")
    else:
        form = JobForm(instance=job)
    return render(request, "edit_job.html", {"form": form, "job": job})

def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == "POST":
        job.delete()
        return redirect("job_list")
    return render(request, "delete_job.html", {"job": job})
