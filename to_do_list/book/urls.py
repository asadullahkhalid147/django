from django.urls import path
from book.views import home,store,show,edit,delete
urlpatterns = [
    path('',home),
    path('store/',store,name='store'),
    path('show_tasks/',show,name='show'),
    path('edit_tasks/<int:id>',edit,name="edit"),
    path('delete/<int:id>',delete,name="delete"),
]
