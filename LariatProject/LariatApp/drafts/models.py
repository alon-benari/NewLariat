from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models
from django.urls import reverse
from django.utils import timezone
import uuid

# Create your models here.
class Patient(models.Model):
    """
    A method to represet fields for the screening questionnaire
    """
    pid = models.UUIDField(primary_key=True,
                           default=uuid.uuid4, 
                           help_text="Unique ID ")
    created_date = models.DateTimeField(default = timezone.now)
    first_name = models.CharField(max_length=50)
    middle_initial = models.CharField(max_length=2)
    last_name = models.CharField(max_length=50)
    female = models.BooleanField(default=False)
    SSN = models.CharField(max_length=9)
    #active_smoker = models.BooleanField(default=False)
    #osa =  models.BooleanField(default=False)
    #climb2 =  models.BooleanField(default=False,help_text = 'can climb 2 flights of steps')
    age = models.IntegerField(help_text = 'age')
    snf = models.CharField(max_length=3,help_text = 'snf')
    nephrologist = models.CharField(max_length=3)
    chf =  models.CharField(max_length=3,help_text = 'CHF')
    sob =  models.CharField(max_length=3,help_text = 'sob')
    cancer =  models.CharField(max_length=3,help_text = 'cancer')
    weight_loss = models.CharField(default = 'no',max_length=3,help_text = 'cancer')
    appetite =  models.CharField(default = 'no',max_length=3,help_text = 'appetite')
    memory =   models.CharField(default = 'no',max_length=3,help_text = 'memory')
    mobility =  models.CharField(default = 'no',max_length=3,help_text = 'mobility')
    eating =  models.CharField(default = 'no',max_length=3,help_text = 'eating')
    toileting =  models.CharField(default = 'no',max_length=3,help_text = 'toileting')
    hygiene =  models.CharField(default = 'no',max_length=3,help_text = 'personal hygiene')
    created_by = models.ForeignKey(User)

    def published(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
      """
      A method to return the name 
      """
      return self.first_name+self.last_name+self.SSN
