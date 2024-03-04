from django.urls import path
from . import views
urlpatterns = [
    # path('',views.home),
    path('',views.set_session),
    path('get/',views.get__session),
    # path('del/',views.delete_cookie),
    path('del/',views.delete_session)
]


    