from django.db import models
# from employeers.models import Employeers

import uuid

# Create your models here.

class JobTypeChoice(models.TextChoices):

    INTERNSHIP = 'Internship','Internship'

    FULL_TIME       = 'Full Time','Full Time'

    CONTRACT     = 'Contract', 'Contract'

    
class CandidateTypeChoice(models.TextChoices):

    EXPERIANCED = 'Experianced', 'Experianced'

    FRESHER     = 'Fresher' ,'Fresher' 

class WorkModeChoice(models.TextChoices):

    REMOTE = 'Remote','Remote'

    ON_SITE = 'On-site','On-site' 


class BaseClass(models.Model):

    uuid = models.SlugField(unique=True,default=uuid.uuid4 )

    active_status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)    

    class Meta:

        abstract = True 

class Jobs( BaseClass):



    title = models.CharField(max_length=75)

    description = models.TextField()

    employer = models.ForeignKey('employeers.Employeers',on_delete=models.CASCADE)

    candidate_type = models.CharField(max_length=25,choices= CandidateTypeChoice)

    experiance = models.DecimalField(max_digits = 2, decimal_places=0)

    job_type = models.CharField(max_length=30,choices=JobTypeChoice.choices)

    skills = models.TextField()

    location = models.CharField(max_length=50)

    closing_date = models.DateField()

    salary_package = models.CharField(max_length=20)

    posted_date = models.DateField()

    work_mode = models.CharField(max_length=20, choices=WorkModeChoice)


    def __str__(self):
        return f'{self.employer}--{self.title}--{self.salary_package}'
    

    class Meta:

        verbose_name = 'Jobs'

        verbose_name_plural = 'Jobs'

        ordering = ['id']


