from django.shortcuts import render
from .models import Object

# Create your views here.

def plan(request):

    DAY_CHOICES = (("saturday", "Saturday"), ("sunday", "Sunday"),("monday", "Monday"), ("tuesday", "Tuesday"), ("wensday", "Wensday"), ("thursday", "Thursday"), ("friday", "Friday"))
    TIME_CHOICES = (("9-10:30", "9-10:30"), ("10:30-12", "10:30-12"), ("13-15", "13-15"), ("15-17", "15-17"), ("17-19", "17-19"))
    
    lst = []
    for t in TIME_CHOICES:
        ls = [t[0]]
        for d in DAY_CHOICES:
            try:
                l = Object.objects.get(day=d[0], time=t[0])
                ls.append(l)
            except:
                l = []
                ls.append(l)
        lst.append(ls)
    
    context = {'lst':lst, "Time":list(map(lambda x:x[0], TIME_CHOICES)), "Day":list(map(lambda x:x[0], DAY_CHOICES))}
    return render(request, 'index.html', context)


def edit(request):

    DAY_CHOICES = (("saturday", "Saturday"), ("sunday", "Sunday"),("monday", "Monday"), ("tuesday", "Tuesday"), ("wensday", "Wensday"), ("thursday", "Thursday"), ("friday", "Friday"))
    TIME_CHOICES = (("9-10:30", "9-10:30"), ("10:30-12", "10:30-12"), ("13-15", "13-15"), ("15-17", "15-17"), ("17-19", "17-19"))
    object = Object.objects.all()
    lst = []
    for t in TIME_CHOICES:
        ls = [t[0]]
        for d in DAY_CHOICES:
            try:
                l = Object.objects.get(day=d[0], time=t[0])
                ls.append(l)
            except:
                l = []
                ls.append(l)
        lst.append(ls)
    
    context = {'lst':lst, "Time":list(map(lambda x:x[0], TIME_CHOICES)), "Day":list(map(lambda x:x[0], DAY_CHOICES)), "obj":object}
    return render(request, 'edit.html', context)
    

    