from django.shortcuts import render, HttpResponse

# Create your views here.
from celery.schedules import crontab
from celery.task import periodic_task


@periodic_task(run_every=crontab(hour=12, minute=8, day_of_week="tues"))
def every_monday_morning():
    print("This is run every Monday morning at 7:30")


@periodic_task(run_every=crontab(hour=12, minute=9, day_of_week="tues"))
def test(request):
    return HttpResponse("This function runs everyday at 9 am")
