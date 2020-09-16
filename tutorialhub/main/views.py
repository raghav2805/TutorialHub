from django.shortcuts import render, get_object_or_404
from .models import Subject, Tutorial
# Create your views here.


def home(request):
    return render(request, 'main/index.html')


def branches(request, sem):
    print(sem)
    return render(request, 'main/branches.html', {'sem': sem})


def subjects(request, sem, branch):
    print(sem)
    print(branch)
    subjects = Subject.objects.filter(semester=sem, branch=branch.upper())

    return render(request, 'main/subjects.html', {'subjects': subjects, 'sem': sem, 'branch': branch})


def tutorials(request,  sem, branch, sub_id):
    subject = get_object_or_404(Subject, id=sub_id)
    tutorials = Tutorial.objects.filter(subject=subject)
    return render(request, 'main/tuts.html', {'tutorials': tutorials, 'subject': subject})
