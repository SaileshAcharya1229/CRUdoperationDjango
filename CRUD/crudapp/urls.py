
from django.urls import path
from . import views

urlpatterns = [
 
    path("",views.home,name="home"),
    #path("",views.home),
    path("addstudent", views.addStudent),
    path("deletestudent<int:roll>",views.deleteStudent),
    path("updatestudent<int:roll>",views.updateStudent)

]