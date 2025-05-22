from django.shortcuts import render,redirect

from .models import Jobs

from django.views import View

from employeers.models import Employeers

from .forms import JobCreateEmployerForm,JobCreateForm

from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from authentication.permissions import permission_role

# Create your views here.



class HomeView(View):

    def get(self, request , *args , **kwargs):

        data = {
            'page'  : 'home-page'
        }
        

        return render(request, 'jobs/home.html', context=data)
    
class JobListView(View):

    def get(self, request , *args , **kwargs):

        jobs = Jobs.objects.all()

        print(jobs)
        data = {
            'jobs' : jobs,
            'page'  : 'job-list-page'
        }
        return render(request, 'jobs/joblist.html', context=data)


class EmployersJobView(View):

    def get(self, request, *args , **kwargs):

        jobs = Jobs.objects.all()


        data = {
            'jobs' : jobs
        }

        return render(request,'jobs/employers.html', context=data)
# class JobEmployerDeleteView(View):

#     def get(self, request, *args, **kwargs):

#         uuid = kwargs.get('uuid')

#         job = Jobs.objects.get(uuid=uuid)
#         job.delete()

#         return redirect ('employers')


# class CreateEmployerJobsView(View):

#     def get(self, request, *args , **kwargs):
#         form = JobCreateEmployerForm()
        
#         data = {
#             'form': form
#             }


#         return render(request, 'jobs/create-employer-jobs.html', context=data)
    
#     def post(self, request, *args, **kwargs):

#         form = JobCreateEmployerForm(request.POST, request.FILES)

#         if form.is_valid():

#             # print(form.cleaned_data)

#             # form.cleaned_data['instructor'] = 'John Doe'

#             # form.save()

#             job = form.save(commit=False)

#             # job.emp
#             job.save()

#             print(job)
        

#             return redirect('employers')
        
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
        # uuid = kwargs.get('uuid')
        # job = Jobs.objects.get(uuid=uuid)
        form = JobCreateForm()

        employers = Employeers.objects.all()
        
        data = {
            'form': form, 
            'employers' : employers,
            'page' : 'create-job-page'
            }


        return render(request, 'jobs/create-job.html', context=data)
    
    def post(self, request, *args, **kwargs):

        # uuid = kwargs.get('uuid')

        if request.method == 'POST':

            form = JobCreateForm(request.POST)


            print(form.errors)
        
            if form.is_valid():


                form.save()


                return redirect('joblist')
            data = { 'form' : form ,
                    'employer' : Employeers.objects.all()}

            return render(request, 'jobs/create-job.html',context=data)
        

    