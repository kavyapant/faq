from django.shortcuts import render,redirect
from .models import Destination,Services

# Create your views here.
def home(request):
    dests=Destination.objects.all()
    yo=Services.objects.all()
    p=[]
    a=[]
    m=[]
    l= Destination.objects.exclude(tags__exact='')
    for d in l:
        

        a=(d.tags).split(",")
        print(a)
        for ele in a:
            if ele not in p:
                p.append(ele)
    
    for pp in yo:
        if pp.cat not in m:
            m.append(pp.cat)
            
    return render(request,'home.html',{'dests':p,'services':m})
def tags(request):
    query = request.GET.get('query_name')
    dests=Destination.objects.all()
    print(query)
    return render(request,'tags.html',{'dests':query,'dests2':dests})
    
        



    
def ask(request):
    if request.method=='POST':
        question=request.POST['question']
        category=request.POST['c']
        subcategory=request.POST['sc']
        if category == 'DigitalPresence':
            category='Digital Presence'
        


        d=Destination(question=question,category=category,subcategory=subcategory)

        d.save();
        return redirect('/')
    else:
        return render(request,'ask.html')
def dp(request):
    return render(request,'dp.html')

def ds(request):
    query = request.GET.get('qu')
    k=Services.objects.all()
    m=[]
    for pp in k:
        if pp.subcat not in m and pp.cat==query:
            m.append(pp.subcat)
    return render(request,'ds.html',{'sent':query,'sent2':m})

def wd(request):
    query = request.GET.get('qu')
    k=Destination.objects.all()
    m=[]
    for pp in k:
        if pp.subcategory==query:
            m.append(pp)
    return render(request,'wd.html',{'sent':m,'sent2':query})


