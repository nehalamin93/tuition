from django.shortcuts import render
from django.http import HttpResponse
from teaching.models import Teacher,Student

def index(request):
    return render(request,'index.html')

def searching(request):
    if request.method == 'POST':
        subject_search = request.POST.get('subject1')
        location_search = request.POST.get('location1')
        elems = Teacher.objects.filter(temp_address=str(location_search))
        context_dict = {}
        context_dict['persons'] = elems
    return render(request,'teacherslist.html',context_dict)