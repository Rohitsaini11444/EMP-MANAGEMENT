from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Emp

# Create your views here.
def emp_home(request):
    emps=Emp.objects.all()

    return render (request, "emp/home.html",{ 'emps':emps})

#ye form ki request h 
def add_emp (request):
    if request.method=="POST":

        #data fatch
        emp_name=request.POST.get("emp_name") #ye humne add_emp.html ka sara data fatch ker liya
        emp_id=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")

        #create model object and set the data
        #phale hum Emp ki class (models.py) ko apne views.py me impoet ker le ge. 
        #fir hum apne "Emp" class ka "object" creat ker le ge.
        e=Emp()
        #yeha hum ne apne class(models) ko apne name(add_emp.html) se mila diya.
        e.name=emp_name
        e.emp_id=emp_id
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None :
            e.working=False
        else:
            e.working=True  

        #save the object
        e.save()  
        # or fir hum ise migrate ker le ge (python manage.py make migration then pyton manage.py migrate)    

       
        print("data is comming")
        return redirect ("/emp/home/")
    return render (request, "emp/add_emp.html",{})



def delete_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/emp/home")



def update_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    return redirect("emp/update_emp.html",{'emp':emp})