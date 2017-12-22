from django.db import models
from django.contrib.auth.models import User
# Create your models here
from django.db import models
from django.urls import reverse
from django.utils import timezone
import uuid



# Create your models here.
class Patient(models.Model):
    """
    A method to represet fields for the screening questionnaire
    """
    #pid = models.UUIDField(primary_key=True,
    #                       default=uuid.uuid4, 
    #                       help_text="Unique ID ")
    created_date = models.DateTimeField(default = timezone.now)
    first_name = models.CharField(max_length=50)
    middle_initial = models.CharField(max_length=2)
    last_name = models.CharField(max_length=50)
    female = models.BooleanField(default=False)
    SSN = models.CharField(max_length=9)
    age = models.IntegerField(help_text = 'age')
    #
    snf = models.CharField(blank=True,max_length=3,help_text = 'snf')
    nephrologist = models.CharField(blank = True, help_text = 'nephrology',max_length=3)
    chf =  models.CharField(blank = True, max_length=3,help_text = 'CHF')
    sob =  models.CharField(blank = True, max_length=3,help_text = 'sob')
    #
    cancer =  models.CharField(blank=True,max_length=3,help_text = 'cancer')
    weight_loss = models.CharField(blank=True,default = 'no',max_length=3,help_text = 'cancer')
    appetite = models.CharField(blank=True,default = 'no',max_length=3,help_text = 'appetite')
    memory =  models.CharField(blank=True,default = 'no',max_length=3,help_text = 'memory')
    mobility =  models.CharField(blank=True,default = 'no',max_length=3,help_text = 'mobility')
    eating =  models.CharField(blank=True,default = 'no',max_length=3,help_text = 'eating')
    toileting =  models.CharField(blank=True,default = 'no',max_length=3,help_text = 'toileting')
    hygiene =  models.CharField(blank=True,default = 'no',max_length=3,help_text = 'personal hygiene')
    
    rai = models.IntegerField(default = 0,help_text = 'RAI')
    created_by = models.CharField(User, null = True,default = '1', max_length =20)
    
    def save(self, *args, **kwargs):
        self.rai = self.get_rai()
        #self.created_by = CuserMiddleware.get_user()
        super(Patient,self).save(*args, **kwargs)
   
    #
    #    """
    #	A set of methods to compute RAI
    #    """

    def age_map(self):
        """
        A method to compute the age factor
        """ 
        print(self.age,self.cancer)
        ranges =  [(0,70),(70,75),(75,80),(80,85),(85,90),(90,95),(95,100),(100,150)]
        f = True
        scores = [(2,20),(3,19),(4,18),(5,17),(6,15),(7,14),(8,14),(9,13)]
        #
        while f:
            for i,r in enumerate(ranges):
                if int(self.age) in range(ranges[i][0],ranges[i][1]):
                    f = False
                    s=scores[i]
                    break
        return s[int(self.cancer)]

    


    def get_adl(adl_score,cog):
        """
 	   A method to  compute adl corrected fo cognition
    	"""
        found = True
        ranges = [(0),(1,2),(3,4),(5,6,7),(8,9),(10,11),(12,13),(14,15,16)]
        modifier = [-2,-1,0,1,2,3,4,5]
        while found:
            for i,r in enumerate(ranges):
                print(adl_score,range[i])
                if adl_score in ranges[i]:
                    adl_score = adl_score+modifier[i]
                    found = False
                    break
       	return adl_score
    
   	

   	

    def get_rai(self):
        """
    	 A method to compute rai from the form:
        """
        age_score = self.age_map()
        print(age_score)
        co_morbid_features = [int(self.weight_loss), 
                              int(self.nephrologist),int(self.chf), int(self.appetite), int(self.sob)]
        co_morbid_vals = [5,6,4,4,8]
        co_morbid_score = sum([i[0]*i[1] for i in zip(co_morbid_features,co_morbid_vals)])
        
        #
        snf_score = int(self.snf)*8
    	#
        adl_score = int(self.mobility)+int(self.eating)+int(self.toileting)+int(self.hygiene)
        cog = int(self.memory)

    	#if cog:
    	#    adl_score = get_adl(adl_score,cog)
        return co_morbid_score+age_score+snf_score+adl_score

    
    def published(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
      """
      A method to return the name 
      """
      return self.first_name+self.last_name+self.SSN
