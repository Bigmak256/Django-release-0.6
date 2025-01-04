from django.shortcuts import render
import datetime
# Create your views here.

def index_page(request):
    context = {}
    context["author"] = "Валера"
    context["pages"] = 3

    return render(request, 'index.html', context)

def time_page(request):
    context = {}
    context["seconds"] = datetime.datetime.now().time().second
    context["minutes"] = datetime.datetime.now().time().minute
    context["hours"] = datetime.datetime.now().time().hour
    context["month"] = datetime.datetime.now().date().month
    context["day"] = datetime.datetime.now().date().day
    context["year"] = datetime.datetime.now().date().year

    return render(request, 'time.html', context)

def calc_page(request):
    context = {}
    a = request.GET.get("a", 0)
    b = request.GET.get("b", 0)
    if a == "":
        a = 0
    if b == "":
        b = 0
    c = int(a) + int(b)
    context["summ"] = c
    return render(request, 'calc.html', context)