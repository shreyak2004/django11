from django.shortcuts import render, HttpResponse

from .models import student, faculty, message, reply,register
from django.db.models import Q

from io import BytesIO
from django.template.loader import get_template
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')

    
def view_students(request):

    stds = student.objects.all()
    context = {
        'stds' : stds 
    }

    print(context)
    return render(request, 'view_students.html', context)


def view_faculty(request):

    fack = faculty.objects.all()
    context = {
        'fack' : fack 
    }

    print(context)
    return render(request, 'view_faculty.html', context)



def send_message(request):
    if request.method == 'POST':
        toname = request.POST['toname']
        fromw = request.POST['fromw']
        regno1 = request.POST['regno1']
        messageis = request.POST['messageis']
        # phone = int(request.POST['phone'])
        # dept = int(request.POST['dept'])
        # role = int(request.POST['role'])
        new_message = message(toname= toname, fromw=fromw, regno1=regno1, messageis=messageis)
        new_message.save()
        return HttpResponse('Message sent Successfully')
    elif request.method=='GET':
        return render(request, 'message.html')
    else:
        return HttpResponse("An Exception Occured! Employee Has Not Been Added")


       


def view_reply(request):

    rep = reply.objects.all()
    context ={
        'rep' : rep
    }
    print(context)
    return render(request, 'reply.html', context)
   




def addstudent(request):
    if request.method == 'POST':
        name = request.POST['name']
        regno = request.POST['regno']
        branch = request.POST['branch']
        year = request.POST['year']
       
        new_stud = student(name=name, regno=regno, branch=branch, year=year)
        new_stud.save()
        return HttpResponse('student added Successfully')
    elif request.method=='GET':
        return render(request, 'add_student.html')
    else:
        return HttpResponse("An Exception Occured! Employee Has Not Been Added")

def registerc(request):
    if request.method == 'POST':
        name = request.POST['name']
        regno = request.POST['regno']
        complaint = request.POST['complaint']
        
       
        complaint = register(name=name, regno=regno, complaint=complaint,)
        complaint.save()
        return HttpResponse('complaint registered Successfully')
    elif request.method=='GET':
        return render(request, 'register.html')
    else:
        return HttpResponse("An Exception Occured! Employee Has Not Been Added")

