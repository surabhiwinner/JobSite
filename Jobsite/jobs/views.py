from django.shortcuts import render,redirect

from django.db.models import Q

from .models import Jobs

from django.views import View

from employeers.models import Employeers

from .forms import JobCreateEmployerForm,JobCreateForm

from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from authentication.permissions import permission_role

from authentication.models import Profile

# Create your views here.



class HomeView(View):

    def get(self, request , *args , **kwargs):

        data = {
            'page'  : 'home-page'
        }
        

        return render(request, 'jobs/home.html', context=data)
    
    
class JobListView(View):

    def get(self, request , *args , **kwargs):

        query = request.GET.get('query')
        print(query)

        jobs = Jobs.objects.all()

        if query:
            jobs = Jobs.objects.filter(Q(title__icontains = query)|
                                                Q(description__icontains = query)|
                                                Q(employer__company_name__icontains =query)| # since instructor is a forign key we have to specify the name of instructor
                                                Q(candidate_type__icontains = query)|
                                                Q(experiance__icontains = query)|
                                                Q(job_type__icontains =query)|
                                                Q(location__icontains = query)|
                                                Q(work_mode__icontains = query))
        

        print(jobs)
        data = {
            'query': query,
            'jobs' : jobs,
            'page'  : 'job-list-page'
        }
        return render(request, 'jobs/joblist.html', context=data)

        
class JobDetailView(View):

    def get(self, request, *args, **kwargs):
     
     uuid = kwargs.get('uuid')
     job = Jobs.objects.get(uuid = uuid)

     data = {
         'job' :job,
         'page' : 'job-detail-view-page'
     }

     return render(request, 'jobs/job-details.html', context = data)

# class EmployerJobUpdateView(View):

#     def get(self, request , *args , **kwargs):

#             uuid = kwargs.get('uuid')

#             job = Jobs.objects.get(uuid=uuid)

#             form = JobCreateEmployerForm(instance=job)

#             data = {
#                 'form' : form
#             }
#             return render(request, 'jobs/create-employer-jobs.html', context=data)
    
#     def post(self, request, *args, **kwargs):

#             uuid = kwargs.get('uuid')

#             job = Jobs.objects.get(uuid = uuid)

#             form = JobCreateEmployerForm(request.POST,request.FILES, instance=job)

#             if form.is_valid():

#                 form.save()

#             data = { 'form' : form }

#             return render(request, 'jobs/employers.html',context=data)

@method_decorator(permission_role(roles=['Employer']), name='dispatch')
class CreateJobView(View):

    def get(self, request, *args , **kwargs):
    
        form = JobCreateForm()
        # uuid = request.GET.get('uuid')
        
        # employer = Employeers.objects.get(profile= request.user )
        
       
        data = {
                        'form': form, 
                        # 'employers' : employer,
                        'page' : 'create-job-page'
                        }


        return render(request, 'jobs/create-job.html', context=data)
    
    def post(self, request, *args, **kwargs):

        # uuid = kwargs.get('uuid')

        if request.method == 'POST':

            form = JobCreateForm(request.POST)


            print(form.errors)
        
            if form.is_valid():


                job = form.save( commit=False)
                employer = Employeers.objects.get(profile= request.user)
                job.employer = employer
                job.save()

                return redirect('joblist')
            data = { 'form' : form ,
                    'employer' : Employeers.objects.all()}

            return render(request, 'jobs/create-job.html',context=data)
        

    