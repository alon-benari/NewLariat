from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    """
    A form to capture data from a patient
    """
    YES = 1
    NO = 0
    MALE = 0
    FEMALE = 1
    ONE = 0;TWO = 1;THREE = 2;FOUR = 3;FIVE=4
    YES_NO= ((YES,'yes'),(NO,'no'))
    GENDER = ((MALE,'male'),(FEMALE,'female'))
    #
    mobility_options = ((ONE,'Can get around without any help'),
                        (TWO,'Needs help from a cane/walker/scooter'),
                        (THREE,'Needs help from other to get around the house or neighborhood'),
                        (FOUR,'Needs help getting in or out of a chair'),
                        (FIVE,'Totally dependent on other to get around'))
    #
    eating_options = ((ONE,'Can plan and prepare his/her own meals'),
                        (TWO,'Needs help planning his/her meals'),
                       (THREE,'Needs preparing his/her meals'),
                        (FOUR,'Needs help eating his.her meals'),
                        (FIVE,'Totally dependent on others to eat his/her meals'))
    #
    toilet_options = ((ONE,'Can use the toilet without help'),
                        (TWO,'Needs help getting to or from toilet'),
                       (THREE,'Needs help to use toilet paper'),
                        (FOUR,'Cannot use standard toilet , but with help can use badpan/urinal'),
                        (FIVE,'Totally dependent on others to manage toileting'))
    #
    hygiene_options = ((ONE,'Can shower or bath without prompting or help'),
                        (TWO,'Can shower or bath without help when prompted'),
                       (THREE,'Needs help preparing the tub or shower'),
                        (FOUR,'Needs some help with some elements of washing'),
                        (FIVE,'Totally dependent on others to shower or bathe'))
    #
    
    #######
    first_name = forms.CharField(label = 'First Name',max_length = 50)
    middle_initial =  forms.CharField(label = 'Middle initial',max_length = 1)
    last_name = forms.CharField(label = 'Last Name',max_length = 50)
    SSN = forms.CharField(label = 'SSN',max_length=9)
    age = forms.IntegerField()
    #
    female = forms.ChoiceField(
         choices = GENDER,
         required=True, 
         widget = forms.RadioSelect(),
         label= 'Gender')
    #
    snf = forms.ChoiceField(
         choices = YES_NO,
         required=True, 
         widget = forms.RadioSelect(),
         label= 'Does the patient live in an assited living/nursing home environment?')  
    nephrologist = forms.ChoiceField(
         choices = YES_NO,
         required=True, 
         widget = forms.RadioSelect(),
         label = 'Has the patient ever seen a nephrologist or has a history of kidney disease?')
    #
    chf = forms.ChoiceField(
         choices = YES_NO,
         required=True, 
         widget = forms.RadioSelect(),
         label = 'Does the patient has chronic (long-standing) congestive heart failure?') 
     #
    sob = forms.ChoiceField(
         choices = YES_NO,
         required=True, 
         widget = forms.RadioSelect(),
         label = 'Does the patient CURRENTLY have shortness of breath at rest or mininal activity?')

    #
    cancer = forms.ChoiceField(
         choices = YES_NO,
         required=True, 
         widget = forms.RadioSelect(),
         label = 'Was the patient treated in the past 5 years for cancer?')
    #
    weight_loss = forms.ChoiceField(
         choices = YES_NO,
         required=True, 
         widget = forms.RadioSelect(),
         label = 'In the past 3 months, has the patient lost 10 pounds or more unintentionally?')
    #
    appetite = forms.ChoiceField(
         choices = YES_NO,
         required=True, 
         widget = forms.RadioSelect(),
         label = 'Is the patient appetite currently poor?')

    memory = forms.ChoiceField(
         choices = YES_NO,
         required = True,
         widget  = forms.RadioSelect(),
         label = 'During the last 3 months, has it become more difficult for the patient to remember things/organize thoughts')
    
    mobility = forms.ChoiceField(choices = mobility_options,
                                          required = True,
                                          widget = forms.RadioSelect(),
                                          label = 'Mobility:Activity of daily living: please select the most appropriate')

    #
    eating = forms.ChoiceField(choices = eating_options,
                                         required = True, 
                                         widget = forms.RadioSelect(),
                                         label = 'Eating: please select the most appropriate')
#    #
    toileting = forms.ChoiceField(choices = toilet_options,
                                          required = True,
                                          widget = forms.RadioSelect(),
                                          label = 'Personal toileting: please select the most appropriate')
#    #
    hygiene = forms.ChoiceField(choices = hygiene_options,
                                          required = True,
                                          widget = forms.RadioSelect(),
                                          label = 'Personal hygiene: please select the most appropriate')
    
  

 #
    class Meta:
        model= Patient
        fields = ('female','first_name','middle_initial','last_name','age',
                  'SSN','snf','nephrologist','chf','sob','cancer',
                  'weight_loss','appetite','memory','mobility','eating','toileting','hygiene')

