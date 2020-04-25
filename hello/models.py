from django.db import models


class Category(models.Model):
    cat=models.TextField(null=True,blank=True)
    
    
    def __str__(self):
          template = '{0.cat}'
          return template.format(self)
class Subcategory(models.Model):
    subcat=models.TextField(null=True,blank=True)
    cate=models.ForeignKey(Category,related_name='cate',null=True,on_delete=models.CASCADE)
    
    def __str__(self):
          template = '{0.subcat}'
          return template.format(self)

class Question(models.Model):
   
    question=models.TextField(null=True,blank=True)
    answer=models.TextField(null=True,blank=True)
    category=models.ForeignKey(Category,null=True, related_name='category',on_delete=models.CASCADE)
    subcategory=models.ForeignKey(Subcategory,null=True, related_name='subcategory',on_delete=models.CASCADE)
    question=models.TextField(null=True,blank=True) 
    tags=models.TextField(null=True,blank=True)  
   



class Campaign(models.Model):
    heading1=models.TextField(null=True,blank=True)
    heading2=models.TextField(null=True,blank=True) 


class Customer_query(models.Model):
    query=models.TextField(null=True,blank=True)
    phone=models.TextField(null=True,blank=True)
    
    


    