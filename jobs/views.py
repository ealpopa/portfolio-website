from django.shortcuts import render
from .models import Job
from django.http import HttpResponse




def home(req):
    jobs = Job.objects
    return render(req, 'jobs/home.html', {'jobs': jobs})


def upload_file(request):
    if request.method == 'POST':
        with open('uploadedfile.txt', 'w') as f:
            for chunk in request.FILES['file'].chunks():
                f.write(chunk.decode())
    return HttpResponse('<p>Success</p>')