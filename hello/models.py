from django.db import models

# Create your models here.
class Destination(models.Model):
    question=models.TextField(null=True,blank=True)
    answer=models.TextField(null=True,blank=True)
    category=models.TextField(null=True,blank=True)
    subcategory=models.TextField(null=True,blank=True)
    tags=models.TextField(null=True,blank=True)

class Services(models.Model):
    cat=models.TextField(null=True,blank=True)
    subcat=models.TextField(null=True,blank=True)
    


    