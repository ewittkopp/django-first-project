from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Department, Employee

# Create your views here.
def index(request):
    dict = {
        'insert_me' : 'This is from views.py',
        'fname' : 'Ethan',
        'lname' : 'Wittkopp',
        'age' : '19' 
    }
    return render(request, 'first_app/index.html', context = dict)
    # return HttpResponse('Hello <a href="/about">World</a>')
def emp_view(request):
    employee_list = Employee.objects.order_by('emp_name')
    emp_dict = {
        'emp_list' : employee_list,
    }
    return render(request, 'first_app/employee.html', context = emp_dict)
def about(request):
    return HttpResponse('<h1> This is the About page!</h1>')