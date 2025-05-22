from django.shortcuts import render, redirect

# Create your views here.

from .forms import CreateEmployeersForm

from .models import Employeers

from django.views import View

from jobs.models import Jobs



class EmployeersListView(View):

    def get(self, request, *args, **kwargs):


        employeers = Employeers.objects.all()

        data = {
            'employeers' : employeers
        }

        return render(request, 'employeers/employeers-list.html', context=data)

class EmployersDetailView(View):

    def get(self, request, *args, **kwargs):

        uuid = kwargs.get('uuid')

        employer = Employeers.objects.get(uuid=uuid)

        data = {
            'employer' : employer,
            
        }

        return render (request,'employeers/employers-detail.html', context=data)

class EmployerJobView(View):

    def get(self, request, *args, **kwargs):

        uuid = kwargs.get('uuid')

        employer = Employeers.objects.get(uuid=uuid)

        jobs = Jobs.objects.filter(employer=employer)

        data = {
            'jobs' : jobs
        }

        return render(request,'employeers/employer-jobs.html', context=data)
