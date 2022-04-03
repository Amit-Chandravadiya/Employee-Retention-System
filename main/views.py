import imp
import re
from django.shortcuts import render,redirect
from main.forms import Contactforms
from main.forms import Mlforms
import os
import joblib
import numpy as np
from . models import ContactDetails
# Create your views here.

def home(request):
    return render(request,'Home.html')

def contact(request):
    context={
        'data':True
    }
    return render(request,'ContactUS1.html',context)

def upload2(request):
    form1=Contactforms(request.POST)
    context={
        'data':True,
        'form':form1,
        }
    if form1.is_valid():
        value=request.POST['submit']
        if value=='submit':
            context['data']=False
        
        cstmr=ContactDetails()
        cstmr.name=request.POST['name']
        cstmr.email=request.POST['email']
        cstmr.message=request.POST['txtarea']
        cstmr.save()
        return render(request,'ContactUS1.html',context)
    else:
        return render(request,'ContactUS1.html',context)
            
    

def service(request):
    return render(request,'ERS.html')

def upload(request):
    # return render(request,'Res.html',context)
    form=Mlforms(request.POST)
    if form.is_valid():
        sal=request.POST['salary']
        sal=str.lower(sal)
        prmtn=request.POST['promotion']
        exp=request.POST['exp']
        hrs=request.POST['hrs']
        prj=request.POST['projects']
        lperfev=request.POST['perc1']
        satisfl=request.POST['perc2']
        workacc=request.POST['workacc']
        if sal!='high' or sal!='low' or sal!='medium':
            return render(request,'ERS.html',{'form':form})
        if sal=='high':
            s=[0,0]
        elif sal=='medium':
            s=[0,1]
        elif sal=='low':
            s=[1,0]
        
        
        
        p=int(prmtn)
        e=int(exp)
        h=int(hrs)
        pr=int(prj)
        l=float(lperfev)/100
        stf=float(satisfl)/100
        wa=int(workacc)
        
        cwd=os.getcwd()
        loc=os.path.join(cwd,'main/DecisionTree.pkl')
        print(loc)    
        model=joblib.load(loc)
        
        # print(s)
        # print(p)
        # print(e)
        # print(h)
        # print(pr)
        # print(l)
        # print(stf)
        # print(wa)
        
        
        ls=[stf,l,pr,h,e,wa,p,s[0],s[1]]
        arr=np.array(ls)
        
        res=model.predict([arr])
        print(ls)
        print(f'Result of the prediction is : {res}')
        
        context={
        'data':False
        }
        if res[0]:
            context['data']=True
        else:
            context['data']=False
        
        return render(request,'Res.html',context)
    return render(request,'ERS.html',{'form':form})
