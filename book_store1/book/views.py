from django.shortcuts import render,redirect
from book.forms import BookStoreForm
from book.models import BookStoreModel
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
# Create your views here.

#function based view
# def home(request):
#     return render(request,'store_book.html')

#class based view
class MyTemplateView(TemplateView):
    template_name='home.html'
    def get_context_data(self,**kwargs):
            context = super().get_context_data(**kwargs)
            context = {'name':'rahim','age':21}
            print(kwargs)
            context.update(kwargs)#dictionary update kora
            
            print(context)
            return context
        
#function based view
# def store_book(request):
#     # book=BookStoreForm(request.POST)
#     # print(book)
#     if request.method=='POST':
#         book=BookStoreForm(request.POST)
#         if book.is_valid():
#             # book.save(commit=False)
#             book.save()
#             print(book.cleaned_data)
#             return redirect('show_books')
            
#     else:
#         book=BookStoreForm()
#     return render(request,'store_book.html',{'form':book})

#class based view
# class BookFormView(FormView):
#     template_name='store_book.html'
#     form_class=BookStoreForm
   
#     # success_url='/show_books/'
#     # success_url= reverse_lazy('show_books')
#     def form_valid(self,form):
#         print(form.cleaned_data)
#         form.save()
#         # return HttpResponse('form submitted')
#         return redirect('show_books')
class BookFormView(CreateView):
    model=BookStoreModel
    template_name='store_book.html'
    form_class=BookStoreForm
    success_url=reverse_lazy('show_books')


#** function based view
# def show_books(request):
#     book=BookStoreModel.objects.all()
#     # print(book)
#     # for item in book:
#     #     print(item.first_pub)
#     return render(request,'show_book.html',{'data':book})

#class based view
class BookListView(ListView):
    model=BookStoreModel
    template_name='show_book.html'
    context_object_name='booklist'
    # def get_queryset(self):
    #     # return BookStoreModel.objects.filter(author='rahim')
    #     return BookStoreModel.objects.filter(id='3')
    # def get_context_data(self,**kwargs):
    #     context=super().get_context_data(**kwargs)
    #     context={'Rahim' : BookStoreModel.objects.all().order_by('author')}
    #     return context
    # ordering=['author']
    # ordering=['category']
    # ordering=['-id']
    def get_template_names(self):
        if self.request.user.is_superuser:
            template_name='superuser.html'
        elif self.request.user.is_staff:
            template_name=''
        else:
            template_name=self.template_name
        return [template_name]

class BookDetailsView(DetailView):
    model=BookStoreModel
    template_name='book_details.html'
    context_object_name='item'
    pk_url_kwarg='id'

#function based view
# def edit_book(request,id):
#     book=BookStoreModel.objects.get(pk = id)
#     form=BookStoreForm(instance = book)
#     if request.method=='POST':
#         form=BookStoreForm(request.POST,instance = book)
#         if form.is_valid():
#             # book.save(commit=False)
#             form.save()
#             return redirect('show_books')
#     return render(request,'store_book.html',{'form':form})

class BookUpdateView(UpdateView):
    model=BookStoreModel
    template_name='store_book.html'
    form_class=BookStoreForm
    success_url=reverse_lazy('show_books')

#function based view
# def delete_book(request,id):
#     book = BookStoreModel.objects.get(pk = id).delete()
#     return redirect('show_books')

#class based view
class DeleteBookView(DeleteView):
    model = BookStoreModel
    template_name='delete_confirmation.html'
    success_url=reverse_lazy('show_books')