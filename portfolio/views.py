from django.shortcuts import render
from django.http import HttpResponse
from .models import Job
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(r):
    return HttpResponse("Hello welcome to portfolio")

@csrf_exempt
def job(r):
    if r.method == 'GET':
        result =[]
        jobs=Job.objects.all()
        for job in jobs:
            data ={
                "company": job.company,
                "description": job.description
                }
            result.append(data)
        return HttpResponse(json.dumps(result))
    if r.method == 'POST':
        body_unicode = r.body.decode('utf-8')
        data = json.loads(body_unicode)
        company = data['company']
        description = data['description']
        job1 =Job(company=company,description=description)
        job1.save()
        return HttpResponse("company added successfully")
    if r.method == 'DELETE':
        body_unicode = r.body.decode('utf-8')
        data = json.loads(body_unicode)
        company = data['company']
        job = Job.objects.filter(company=company)
        job.delete()
        return HttpResponse("company deleted successfully")

def show_job(r):
    jobs = Job.objects.all()
    return render(r, 'portfolio/index.html', context={'jobs': jobs})