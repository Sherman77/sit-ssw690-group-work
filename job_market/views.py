from django.shortcuts import render, get_object_or_404
from .models import JobPost

# Create your views here.
def jobslist(request):
    jobs = JobPost.objects
    return render(request, 'job_market/jobs.html', {'jobs':jobs})

def job_detail(request, item_id):
    job = get_object_or_404(JobPost, pk = item_id)
    return render(request, 'jobs/item_detail.html', {'job':job})