from django.db import models

# Create your models here.
class Question(models.Model):
    question=models.TextField(null=True,blank=True)
    answer=models.TextField(null=True,blank=True)
    category=models.TextField(null=True,blank=True)
    subcategory=models.TextField(null=True,blank=True)
    tags=models.TextField(null=True,blank=True)


class Service(models.Model):
    cat=models.TextField(null=True,blank=True)
    subcat=models.TextField(null=True,blank=True)

class Campaign(models.Model):
    heading1=models.TextField(null=True,blank=True)
    heading2=models.TextField(null=True,blank=True)
class Customer_query(models.Model):
    query=models.TextField(null=True,blank=True)
    phone=models.TextField(null=True,blank=True)
    
    


    