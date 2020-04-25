from django.contrib import admin
from .models import Question,Campaign,Customer_query,Category,Subcategory
# Register your models here.
class Qn(admin.ModelAdmin):
    list_display =['question','answer','category','subcategory','tags']
class Ct(admin.ModelAdmin):
    list_display =['cat']
class Sub(admin.ModelAdmin):
    list_display =['cate','subcat']

class Camp(admin.ModelAdmin):
    list_display =['heading1','heading2']
class Cq(admin.ModelAdmin):
    list_display =['query','phone']

admin.site.register(Question,Qn)
admin.site.register(Category,Ct)
admin.site.register(Subcategory,Sub)

admin.site.register(Campaign,Camp)
admin.site.register(Customer_query,Cq)

