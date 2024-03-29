from django.shortcuts import render
from first_app.forms import StudentForm
from . models import Teacher,Student
# Create your views here.
def home(request):
    if request.method=='POST':
        form= StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form= StudentForm()
    return render(request, 'home.html',{'form':form})

def showData(request):
    # Student list for one teacher
    teacher=Teacher.objects.get(name='Tarek')
    students=teacher.student.all()
    for stud in students:
        print(stud.name,stud.roll,stud.class_name)
        
    # teacher list for one student
    student=Student.objects.get(name='jonak')
    # teachers=student.teacher_set.all()
    teachers=student.teachers.all()
    for teacher in teachers:
        print(f"{teacher.name} {teacher.subject} {teacher.mobile}")
    return render(request,'show_data.html')


    