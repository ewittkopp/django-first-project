from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    dict = {
        'insert_me' : 'This is from views.py',
        'fname' : 'Mike',
        'lname' : 'Oldfield',
        'age' : '60' 
    }
    return render(request, 'first_app/index.html', context = dict)
    # return HttpResponse('Hello <a href="/about">World</a>')
def about(request):
    return HttpResponse('<h1> This is the About page!</h1>')