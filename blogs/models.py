from django.db import models
from datetime import datetime

# Create your models here.
class Blogs(models.Model) :
    title=models.CharField(max_length=25)
    body=models.CharField(max_length=500)
    created_at=models.DateTimeField(default=datetime.now,blank=True)
    
