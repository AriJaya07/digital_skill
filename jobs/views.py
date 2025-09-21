from django.shortcuts import render, get_object_or_404, redirect
from .models import Job, JobApplication
from .forms import JobForm, JobApplicationForm

# List all jobs
def job_list(request):
    jobs = Job.objects.all().order_by("-posted_at")
    return render(request, "job_list.html", {"jobs": jobs})

# Job detail + applications
def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    applications = job.applications.all()

    return render(request, "job_detail.html", {
        "job": job,
        "applications": applications
    })

# Add job
def add_job(request):
    if request.method == "POST":
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            job.employer = request.user  # set logged-in user as employer
            job.save()
            form.save_m2m()
            return redirect("job_list")
    else:
        form = JobForm()
    return render(request, "job_form.html", {"form": form, "title": "Add Job"})

# Edit job
def edit_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == "POST":
        form = JobForm(request.POST, request.FILES, instance=job)
        if form.is_valid():
            form.save()
            return redirect("job_detail", job_id=job.id)
    else:
        form = JobForm(instance=job)
    return render(request, "edit_job.html", {"form": form, "title": "Edit Job"})

# Delete job
def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == "POST":
        job.delete()
        return redirect("job_list")
    return render(request, "delete_job.html", {"job": job})

# Apply to job
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == "POST":
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user  # student applying
            application.save()
            return redirect("job_detail", job_id=job.id)
    else:
        form = JobApplicationForm()
    return render(request, "apply_job.html", {"form": form, "job": job})
