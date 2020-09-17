from django.db import models

branches = [('CSE', 'CSE'), ('ECE', 'ECE'), ('BIOTECH', 'BIOTECH')]
semesters = [(1, 'SEM 1'), (2, 'SEM 2'), (3, 'SEM 3'), (4, 'SEM 4'),
             (5, 'SEM 5'), (6, 'SEM 6'), (7, 'SEM 7'), (8, 'SEM 8')]
# Create your models here.


def upload_path_handler(instance, filename):
    return "subject/sem_{semester}/{branch}/{name}_{file}".format(semester=instance.semester, branch=instance.branch, name=instance.name, file=filename)


class Subject(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to=upload_path_handler)
    semester = models.IntegerField(choices=semesters)
    branch = models.CharField(max_length=200, choices=branches)
    description = models.TextField()

    def __str__(self):
        return self.name


def tutorial_upload_path_handler(instance, filename):
    return "tutorial/sem_{semester}/{branch}/{name}_{file}".format(semester=instance.subject.semester, branch=instance.subject.branch, name=instance.name, file=filename)


class Tutorial(models.Model):
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name="tutorials")
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to=tutorial_upload_path_handler)

    def __str__(self):
        return "{subject}_{name}".format(subject=self.subject, name=self.name)
