from django import forms


from .models import Employeers


class CreateEmployeersForm(forms.ModelForm):


    class Meta:

        model = Employeers

        exclude = [ 'uuid', 'active_status',]


        widgets = {

             'company_name' : forms.TextInput(attrs={
                 
                                            'class' :   'form-control',
                                            'required'  :   'required',
                                            'placeholder'   : " Enter compant's name "
             }),

             'image'    :   forms.FileInput(attrs={
                                            'class' :   'form-control',
                                            'required'  :   'required'
             }),
             'location' :   forms.TextInput(attrs={
                                            'class' :   'form-control',
                                            'placeholder'   :   'Enter the location '
             }),

             'description'  :   forms.Textarea(attrs={
                                            'class' :   'form-control',
                                            'required'  :   'required'
             })
        }

        def __init__(self, *args, **kwargs):
            super(CreateEmployeersForm,self).__init__(*args, **kwargs)