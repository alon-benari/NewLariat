from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Patient
from LariatApp import utils 
from .forms import PatientForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
@login_required
def index(request):
    """
    A method to direct to the index home page of the application
    """
    num_patients = Patient.objects.all().count()
    return render(request,'index.html',context={'num_patients': num_patients})



@login_required
def add_patient(request):
    """
    A method to render a form for adding patient details to the database
    """
    form = PatientForm()
    print('Getting the form')
    if request.method=="POST":
        form = PatientForm(request.POST)
        rai_list = ['age',
                    'snf',
                    'nephrologist',
                    'chf',
                    'sob',
                    'cancer',
                    'weight_loss',
                    'appetite',
                    'memory',
                    'mobility',
                    'eating',
                    'toileting',
                    'hygiene']
        features = [int(form.data[r]) for r in rai_list]
        print(utils.age_map(int(form.data['age']),int(form.data['cancer'])))

        print(features)
        print('******')
        print(utils.get_rai(form))
        rai = utils.get_rai(form)
        print('******')

        if form.is_valid():
            form.save()
            return render (request, 
                           'show_rai.html', 
                            context = {'rai':rai,
                                      'Age':form.data['age'],
                                      'FirstName': form.data['first_name'],
                                      'LastName': form.data['last_name'],
                                      'MiddleInit': form.data['middle_initial'],
                                      'SSN':form.data['SSN']})
            #print('saving')
            form = PatientForm()
    else:		
        form=PatientForm
        return render(request, 'add_patient.html',{'form':form})

def contact_us(request):
    """
    A method to add contact information
    """
    contact_info = "alon.ben-ari@va.gov"
    return render(request,'contactus.html',context = {'contact_info':contact_info})
    
def about(request):
    """
    A method to add text  about piece
    """
    about_text = "This is a cloud based application where Veterans may answer a screening questionnaire to the pre-operative clinic"
    return render(request,'about.html',context = {'about_text':about_text})

    

def admin(request):
    """
    A method to display the content of the table database
    """
    form = Patient.objects.all()
    return render(request,'admin.html',context = {'form':form})
        
    
