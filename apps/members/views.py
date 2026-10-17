from django.shortcuts import render
from django.db.models import Case, When, Value, IntegerField
from .models import Member

def leadership(request):
    leaders = Member.objects.filter(department='administration').annotate(
        rank=Case(
            When(occupation__icontains='ijrochi', then=Value(1)),
            When(occupation__icontains='executive', then=Value(1)),
            When(occupation__icontains='akademik', then=Value(2)),
            When(occupation__icontains='academic', then=Value(2)),
            When(occupation__icontains='maxsus fan', then=Value(3)),
            When(occupation__icontains='specialized', then=Value(3)),
            When(occupation__icontains="ma'naviy", then=Value(4)),
            When(occupation__icontains="ma’naviy", then=Value(4)),
            When(occupation__icontains='manaviy', then=Value(4)),
            When(occupation__icontains='spiritual', then=Value(4)),
            When(occupation__icontains='maslahatchi', then=Value(5)),
            When(occupation__icontains='counselor', then=Value(5)),
            When(occupation__icontains="xo'jalik", then=Value(6)),
            When(occupation__icontains="xo’jalik", then=Value(6)),
            When(occupation__icontains='xojalik', then=Value(6)),
            When(occupation__icontains='household', then=Value(6)),
            default=Value(99),
            output_field=IntegerField(),
        )
    ).order_by('rank', 'id')
    return render(request, 'members/leadership.html', {'leaders': leaders})

def teachers(request):
    teachers_list = Member.objects.filter(department='teacher').order_by('occupation')
    
    context = {
        'teachers': teachers_list
    }
    return render(request, 'members/teachers.html', context)
