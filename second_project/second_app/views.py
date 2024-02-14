from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def courses(request):
    return HttpResponse('''
                        <h1>There are so many courses</h1>
                        <a href='/second_app/feedback/'>FeedBack</a>
                        <a href='/first_app/contact/'>Contact</a>
                        <a href='/first_app/about/'>About</a>
                        '''
                        )


def feedback(request):
    return HttpResponse('''
                        <h1>Give your feedback</h1>
                        <a href='/second_app/courses/'>Courses</a>
                        <a href='/first_app/contact/'>Contact</a>
                        <a href='/first_app/about/'>About</a>
                        ''')