from django.db import models

from jobs.models import BaseClass

import uuid
# Create your models here.


class Employeers(BaseClass):

    profile = models.OneToOneField('authentication.Profile', on_delete=models.CASCADE)

    company_name = models.CharField(max_length=150)

    location = models.CharField(max_length=75)

    description = models.TextField()

    image = models.ImageField(upload_to='employeers-images/')

    def __str__(self):

        return f'{self.company_name}--{self.location}'

    class Meta:

        verbose_name = 'Employers'

        verbose_name_plural = 'Employers'

        ordering = ['id']

