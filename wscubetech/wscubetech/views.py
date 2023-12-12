from django.http import HttpResponse
from django.shortcuts import render


def homePage(request):
    # data={
    #     'title':'Home Page new',
    #     'bdata':'Welcome to Home Pages of projects',
    #     'clist':['PHP','Java','Django'],
    #     'numbers':[10,20,30,40,50],
    #     'student_details':[
    #         {'name':'Pradeep','phone':9875641234},
    #         {'name':'Testing','phone':8765453214}
    #     ]
    # }
    return render(request,"index.html")

def aboutUs(request):
    return render(request,"about.html")

def Course(request):
    return render(request,"course.html")

def Webtech(request):
    return render(request,"web.html")

def CProgram(request):
    return render(request,"cpro.html")


def courseDetails(request,courseid):
    return HttpResponse(courseid)