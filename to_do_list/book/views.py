from django.shortcuts import render,redirect
from book.forms import TaskForm
from book.models import TaskModel
# Create your views here.
def home(request):
    return render(request,'store.html')


def store(request):
    if request.method=='POST':
        book=TaskForm(request.POST)
        if book.is_valid():
            # book.save(commit=False)
            book.save()
            print(book.cleaned_data)
            return redirect('show')
            
    else:
        book=TaskForm()
    return render(request,'store.html',{'form':book})

def show(request):
    book=TaskModel.objects.all()
    # print(book)
    # for item in book:
    #     print(item.first_pub)
    return render(request,'show.html',{'data':book})

def edit(request,id):
    task=TaskModel.objects.get(pk=id)
    form=TaskForm(instance=task)
    if request.method=='POST':
        form=TaskForm(request.POST,instance = task)
        if form.is_valid():
            # book.save(commit=False)
            form.save()
            return redirect('show')
    return render(request,'store.html',{'form':form})

def delete(request,id):
    book = TaskModel.objects.get(pk = id).delete()
    return redirect('show')