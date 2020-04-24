from django.shortcuts import render,redirect
from .models import Question,Service,Campaign,Customer_query

# Create your views here.
def home(request):
    dests=Question.objects.all()
    yo=Service.objects.all()
    p=[]
    a=[]
    m=[]
    l= Question.objects.exclude(tags__exact='')
    
    for d in l:
        if d.tags is not None:  
            print(d.tags)
            a=(d.tags).split(",")

             
            for ele in a:
                if ele not in p:
                    p.append(ele)
   
    

    for pp in yo:
        if pp.cat not in m:
            m.append(pp.cat)
            
    return render(request,'home.html',{'services':m,'dests':p})
def tags(request):
    query = request.GET.get('query_name')
    dests=Question.objects.all()
    lol=Campaign.objects.all()
    c=[]
    for var in lol:
        c.append(var)
    print(query)
    return render(request,'tags.html',{'dests':query,'dests2':dests,'camp':c})
    
        



    
def ask(request):
    if request.method=='POST':
        question=request.POST['question']
        category=request.POST['c']
        subcategory=request.POST['sc']
        if category == 'DigitalPresence':
            category='Digital Presence'
        


        d=Question(question=question,category=category,subcategory=subcategory)

        d.save();
        return redirect('/')

    
def dp(request):
    return render(request,'dp.html')

def ds(request):
    query = request.GET.get('qu')
    k=Service.objects.all()
    m=[]
    for pp in k:
        if pp.subcat not in m and pp.cat==query:
            m.append(pp.subcat)
    return render(request,'ds.html',{'sent':query,'sent2':m})

def wd(request):
    query = request.GET.get('qu')
    k=Question.objects.all()
    lol=Campaign.objects.all()
    m=[]
    c=[]
    for var in lol:
        c.append(var)
    for pp in k:
        if pp.subcategory==query:
            m.append(pp)
    return render(request,'wd.html',{'sent':m,'sent2':query,'camp':c})


def open(request):
    dests=Question.objects.all()
    yo=Service.objects.all()
    p=[]
    a=[]
    m=[]
    l= Question.objects.exclude(tags__exact='')
    
    for d in l:
        if d.tags is not None:  
            print(d.tags)
            a=(d.tags).split(",")

             
            for ele in a:
                if ele not in p:
                    p.append(ele)
   
    

    for pp in yo:
        if pp.cat not in m:
            m.append(pp.cat)
            
    return render(request,'open.html',{'services':m,'dests':p})

def answer(request):
    query = request.GET.get('qu')
    k=Question.objects.all()
    m =[]
    lol=Campaign.objects.all()
    c=[]
    for var in lol:
        c.append(var)

    for pp in k:
        if pp.question==query:
            m.append(pp)
            r=pp.subcategory

    return render(request,'answer.html',{'sent':m,'sent2':r,'camp':c})
def camp_qs(request):
    query=request.POST['question']
    phone=request.POST['phone']
    d=Customer_query(query=query,phone=phone);
    d.save();
    return redirect(request.META['HTTP_REFERER'])

        
   