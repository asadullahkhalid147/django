from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'./first_app/home.html',{"name" : "I am Khalid","marks":86,"courses" : [
        {
            'id' : 1,
            'course' : 'C',
            'teacher' : 'Rahim'
        },
        {
            'id' : 2,
            'course': 'c++',
            'teacher' : 'karim'
        },
        {
            'id' : 3,
            'course': 'python',
            'teacher' : 'fahim'
        },
    ]})
def about(request):
    return render(request,'./first_app/about.html',{'author' : 'glenn maxwell'})

