from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Schedule
from datetime import date

def index(request):
    if request.method == "GET":
        return render(request, "index.html")

def add(request):
    if request.method == "POST":
        topic = request.POST['topic']
        subject = request.POST['subject']
        clss = request.POST['class']
        board = request.POST['board']
        description = request.POST['description']
        date = request.POST['date']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        link = request.POST['link']
        language = request.POST['language']

        obj = Schedule(topic=topic, subject=subject, clss=clss, board=board, description=description, date=date, start_time=start_time, end_time=end_time, meeting_link=link, language=language)
        obj.save()
        return redirect(reverse('index'))

def get_schedule_classes(request):
    list__ = []
    if request.method == "GET":
        token = "unique-token"
        if 'access_token' not in request.GET:
            return JsonResponse({'error':'Token not Available'})
        get_token = request.GET['access_token']
        if token != get_token:
            return JsonResponse({'error':'Token Authentication Failed'})
        schedule_classes = Schedule.objects.filter(date__gte=date.today()).all()
        for clsss in schedule_classes:
            dict_ = {
                'topic':clsss.topic, 'subject':get_subject(clsss.subject),
                'class':clsss.clss, 'board':clsss.board,
                'description':clsss.description, 'date':clsss.date,
                'start':clsss.start_time, 'end':clsss.end_time,
                'link':clsss.meeting_link, 'language':get_language(clsss.language)
            }
            list__.append(dict_)
        return JsonResponse({'data':list__})

def get_subject(subject):
    if subject == 1:
        return 'Mathematics'
    elif subject == 2:
        return 'Social Science'
    elif subject == 3:
        return 'Science and Technology'
    elif subject == 4:
        return 'Hindi'
    elif subject == 5:
        return 'English'
    elif subject == 6:
        return 'Environment Studies'

def get_language(index):
    if index == 1:
        return 'English'
    if index == 2:
        return 'Hindi'