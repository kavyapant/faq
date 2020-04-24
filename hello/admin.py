from django.contrib import admin
from .models import Question,Service,Campaign,Customer_query
# Register your models here.
class Qn(admin.ModelAdmin):
    list_display =['question','answer','category','subcategory','tags']
class Sr(admin.ModelAdmin):
    list_display =['cat','subcat']
class Camp(admin.ModelAdmin):
    list_display =['heading1','heading2']
class Cq(admin.ModelAdmin):
    list_display =['query','phone']

admin.site.register(Question,Qn)
admin.site.register(Service,Sr)
admin.site.register(Campaign,Camp)
admin.site.register(Customer_query,Cq)

