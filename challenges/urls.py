from django.urls import path
from . import views

urlpatterns=[
    path("",views.index),
    path('create',views.create),
    path('show',views.show),
    path('<int:month>',views.month_by_number),
    path('<str:month>',views.monthly_challenge,name='monthly_challenge')

]