from django.shortcuts import render
from .models import Member

def leadership(request):
    leaders = Member.objects.filter(department='administration')
    return render(request, 'members/leadership.html', {'leaders': leaders})

def teachers(request):
    teachers_list = Member.objects.filter(department='teacher').order_by('occupation')
    
    context = {
        'teachers': teachers_list
    }
    return render(request, 'members/teachers.html', context)
