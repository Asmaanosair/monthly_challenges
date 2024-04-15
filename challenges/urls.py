from django.urls import path
from . import views

urlpatterns=[
    path("",views.index),
    path('create',views.create),
    path('show',views.show),
    path('list',views.list_monthes),
    path('test',views.test_page),
    path('test_html/<str:month>',views.test_html),
    path('<int:month>',views.month_by_number),
    path('<str:month>',views.monthly_challenge,name='monthly_challenge')

]