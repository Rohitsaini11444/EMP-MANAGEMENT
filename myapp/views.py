import datetime
from django.http import HttpResponse
from django.shortcuts import render

def home (request):  
      if request.method=='POST':
            check=request.POST ['check']
            print(check)

      isActive=True
      name="Learncodewith durgesh"
      list_of_programs=[
            'WAP to check even or odd',
            'WAP to check prime number',
            'WAP to print all prime numbers from 1 to 100',
            'wap to print pascals triangle'
            ]
      student={
            'student_name':"Rahul",
            'student_college':"ZYZ",
            'student_city':"JAIPUR",

            }
      data={
            'isActive':isActive,
            'name':name,
            'list_of_programs':list_of_programs,
            'student_data':student,
            }
      return render (request, "home.html", data)
def about (request): 
      return render ( request, "about.html", {} )

