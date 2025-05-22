from django.shortcuts import render, redirect

# Create your views here.

from .forms import CreateEmployeersForm

from .models import Employeers

from django.views import View



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
