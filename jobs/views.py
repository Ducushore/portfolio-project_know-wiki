from django.shortcuts import render

from .models import Job  # from the files models that we have in this folder, import the JOB one


def home(request):
    # defining a 'jobs' variable : where "Job.objects" is getting all the jobs from the DB,
    # and will turn them in Python objects, to be available in the code, later . . .
    jobs = Job.objects  #

    # . . . , or the 'jobs' can be passed forward when calling this 'home' function , through a dictionary :
    return render(request, 'jobs/home.html', {'jobs': jobs})
