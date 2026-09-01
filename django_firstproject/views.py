from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    data={
        'title':'Home Page',
        'bdata':'welcome to SaniaZ codes',
        'clist':['php','java','SQL'],
        'std_detail':[
            {'name':'Ahmad','phn':2344566788},
            {'name':'Amna','phn':2343544657},
        ]
        
    }
    return render(request,"index.html",data)

def about_us(request):
    return HttpResponse("<b>heloooo rahila sana</b>")
def courses(request):
    return HttpResponse(" rahila sana is provinding a web dev corurse")
"""concept of dynamic URLS/routing"""
"""it means page will remain same but data will be changed """

def courseDetail(request,courseid):
    return HttpResponse(f"this is my {courseid} course ")