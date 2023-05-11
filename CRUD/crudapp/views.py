from django.shortcuts import render,redirect
from .models import Student

# Create your views here.
def home(request):
    stu = Student.objects.all()
    context ={
        'st':stu,
    }
    for st in stu:
        print(st.name)
    return render(request,'index.html',context)

def addStudent(request):
    if request.method == 'POST':
        #print("Added")
        #  retrieve the data from user
        
        roll = request.POST.get('roll')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        

        #create an object for models
        s = Student()
        s.roll = roll
        s.name = name
        s.email = email
        s.phone = phone

        s.save()
        return redirect('/')
    return render(request,'addstudent.html')


def deleteStudent(request,roll):
    s = Student.objects.get(pk = roll)
    s.delete()

    return redirect("/")



def updateStudent(request,roll):

    std = Student.objects.get(pk = roll)
    context = {
        'std':std,
    }
    return render(request,"updatestudent.html",context)



