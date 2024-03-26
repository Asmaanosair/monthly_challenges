from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse , HttpResponseNotFound , HttpResponseRedirect
monthly_challenges = {
    'january':"this Month is January ",
    'february':"this Month is february ",
    'march':"this Month is march ",
    'april':"this Month is April ",
}

# Create your views here.
def index(request) : 
    list_montm = ""
    months= list(monthly_challenges.keys())
    for month in months :
        herf=reverse('monthly_challenge',args=[month])
        capital_month=month.capitalize()
        list_montm += f"<li><a href='{herf}'>{capital_month}</li>"
    respons_list=f"<ul>{list_montm}</ul>"
    return HttpResponse(respons_list)
def create(request) :
    return HttpResponse("Create Page")
def show(request) :
    return HttpResponse("Show Page")
# def monthly_challenge(request,month) :
#     text_month = None
#     if month=='january' :
#         text_month = "this Month is January "
#     elif month=="february" : 
#         text_month = "this Month is February "
#     elif month == "march" :
#         text_month = "this Month is March"
#     else :
#         return HttpResponseNotFound('this month not support')
#     return HttpResponse(text_month)
def monthly_challenge(request,month) :
    try :
        return HttpResponse(monthly_challenges[month])
    except :
        return HttpResponseNotFound('This Month Not Support')
def month_by_number(request,month) :
    monthes_list=list(monthly_challenges.keys())
    if month > len(monthes_list) :
        return HttpResponseNotFound("Invalid Month")
    month_str=monthes_list[month-1]
    redirect_path= reverse('monthly_challenge',args=[month_str]) # /challenges/january
    # return HttpResponseRedirect('/challenges/'+ monthes_list[month-1])
    return HttpResponseRedirect(redirect_path)


 