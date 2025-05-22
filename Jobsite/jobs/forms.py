from .models import Jobs,CandidateTypeChoice,WorkModeChoice,JobTypeChoice

from django import forms

from employeers.models import Employeers



class JobCreateEmployerForm(forms.ModelForm):

    class Meta:

        model = Jobs

        exclude = ['uuid','active_status']

        widgets = {

            'title' : forms.TextInput( attrs={
                                            'class' : 'form-control',
                                            'required' : 'required',
                                            'placeholder' : 'Enter Job Title '
                                    }),
            'description' : forms.Textarea( attrs={
                                            'class' : 'form-control',
                                            'required' : 'required',
                                            'placeholder' : "Enter course description"

                                    }),
            
            'experiance' : forms.NumberInput(attrs={

                                            'class' : 'form-control',
                                            'required' : 'required',
                                            
                                    }),
            
            'skills'  :  forms.TextInput( attrs={
                                            'class' : 'form-control',
                                            'required' : 'required',
                                            'placeholder' : 'Enter the skills required '
                                    }),
            'location' :  forms.TextInput( attrs={
                                            'class' : 'form-control',
                                        
                                            'placeholder' : 'Enter the location if any '
                                    }),
            'closing_date' : forms.DateInput(attrs= {
                                            'class' : 'form-control',
                                            'type': 'date',
                                        
                                            'placeholder' : 'Enter the closing date '

                                    }),
            'posted_date' : forms.DateInput(attrs= {
                                            'class' : 'form-control',
                                            'type': 'date',
                                        
                                            'placeholder' : 'Enter the posting date ',

                                    }),
            'salary_package' : forms.TextInput(attrs={

                                    'class' : 'form-control',
                                        
                                    'placeholder' : 'Enter the salary package if any ',

                                    }),
            

       
        }
    
    candidate_type  = forms.ChoiceField(choices=CandidateTypeChoice.choices, widget= forms.Select(
                                    attrs= {
                                            'class' : 'form-select',
                                            'required' : 'required',
                                    }))
    
    work_mode = forms.ChoiceField(choices=WorkModeChoice.choices, widget=forms.Select(
                                    attrs={
                                        'class' : 'form-select',
                                        'required' : 'required'
                                    }))
    job_type  = forms.ChoiceField(choices=JobTypeChoice.choices, widget= forms.Select( 
                                             attrs={
                                            'class' : 'form-select',
                                            'required' : 'required',
                                    }))
   

  

def __init__(self, *args, **kwargs):

        super(JobCreateEmployerForm,self).__init__(*args, **kwargs)

class JobCreateForm(forms.ModelForm):

    class Meta:

        model = Jobs

        exclude = ['uuid','active_status']

        widgets = {

            'title' : forms.TextInput( attrs={
                                            'class' : 'form-control',
                                            'required' : 'required',
                                            'placeholder' : 'Enter Job Title '
                                    }),
            'description' : forms.Textarea( attrs={
                                            'class' : 'form-control',
                                            'required' : 'required',
                                            'placeholder' : "Enter course description"

                                    }),
            
            'experiance' : forms.NumberInput(attrs={

                                            'class' : 'form-control',
                                            'required' : 'required',
                                            
                                    }),
            
            'skills'  :  forms.TextInput( attrs={
                                            'class' : 'form-control',
                                            'required' : 'required',
                                            'placeholder' : 'Enter the skills required '
                                    }),
            'location' :  forms.TextInput( attrs={
                                            'class' : 'form-control',
                                        
                                            'placeholder' : 'Enter the location if any '
                                    }),
            'closing_date' : forms.DateInput(attrs= {
                                            'class' : 'form-control',
                                            'type': 'date',
                                        
                                            'placeholder' : 'Enter the closing date '

                                    }),
            'posted_date' : forms.DateInput(attrs= {
                                            'class' : 'form-control',
                                            'type': 'date',
                                        
                                            'placeholder' : 'Enter the posting date ',

                                    }),
            'salary_package' : forms.TextInput(attrs={

                                    'class' : 'form-control',
                                        
                                    'placeholder' : 'Enter the salary package if any ',

                                    }),
            

       
        }
    
    candidate_type  = forms.ChoiceField(choices=CandidateTypeChoice.choices, widget= forms.Select(
                                    attrs= {
                                            'class' : 'form-select',
                                            'required' : 'required',
                                    }))
    
    work_mode = forms.ChoiceField(choices=WorkModeChoice.choices, widget=forms.Select(
                                    attrs={
                                        'class' : 'form-select',
                                        'required' : 'required'
                                    }))
    job_type  = forms.ChoiceField(choices=JobTypeChoice.choices, widget= forms.Select( 
                                             attrs={
                                            'class' : 'form-select',
                                            'required' : 'required',
                                    }))


    employer = forms.ModelChoiceField( queryset=Employeers.objects.all(), widget=forms.Select(attrs={
                                                                'class' : 'form-control'
                                }))


def __init__(self, *args, **kwargs):

        super(JobCreateForm,self).__init__(*args, **kwargs)
