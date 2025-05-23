from django.shortcuts import render, redirect

# Create your views here.

from django.db.models import Q

from .forms import CreateEmployeersForm

from .models import Employeers

from django.views import View

from jobs.models import Jobs



class EmployeersListView(View):

    def get(self, request, *args, **kwargs):


        employeers = Employeers.objects.all()

        data = {
            'page':'employers-page',
            'employeers' : employeers
        }

        return render(request, 'employeers/employeers-list.html', context=data)

class EmployersDetailView(View):

    def get(self, request, *args, **kwargs):

        uuid = kwargs.get('uuid')

        employer = Employeers.objects.get(uuid=uuid)

        profile =employer.profile

        is_owner = request.user

        data = {
            'employer' : employer,
            'profile'   : profile,
            'is_owner'  : is_owner
            
        }

        return render (request,'employeers/employers-detail.html', context=data)

class EmployerJobView(View):

    def get(self, request, *args, **kwargs):

        query = request.GET.get('query')

        print(query)

        uuid = kwargs.get('uuid')

        employer = Employeers.objects.get(uuid=uuid)

        jobs = Jobs.objects.filter(employer=employer)

        if query:

            jobs = Jobs.objects.filter(Q(title__icontains = query)|
                                                Q(description__icontains = query)|
                                                Q(employer__company_name__icontains =query)| # since instructor is a forign key we have to specify the name of instructor
                                                Q(candidate_type__icontains = query)|
                                                Q(experiance__icontains = query)|
                                                Q(job_type__icontains =query)|
                                                Q(location__icontains = query)|
                                                Q(work_mode__icontains = query))
        
        data = {
            'jobs' : jobs
        }

        return render(request,'employeers/employer-jobs.html', context=data)

class EmployerJobDeleteView(View):

   def get(self, request, *args, **kwargs):

        uuid = kwargs.get('uuid')

        job = Jobs.objects.get(uuid=uuid)
        job.delete()

        return redirect ('employers')