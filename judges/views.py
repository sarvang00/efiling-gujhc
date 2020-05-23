from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from officers.models import Case
from advocates.models import Response


from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/accounts/login/')
def judge_dashboard(request):
    is_advocate = request.user.groups.filter(name='Advocates').exists()
    is_judge = request.user.groups.filter(name='Judges').exists()
    is_officer = request.user.groups.filter(name='Officers').exists()

    print('advocate: ' + str(is_advocate))
    print('judge: ' + str(is_judge))
    print('officer: ' + str(is_officer))

    context = {
        'is_advocate': is_advocate,
        'is_judge': is_judge,
        'is_officer': is_officer,
    }

    if is_judge:
        return render(request, 'judges/dashboard.html', context)
    else:
        return render(request, 'accounts/dashboard.html', context)

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/accounts/login/')
def all_cases(request):
    is_advocate = request.user.groups.filter(name='Advocates').exists()
    is_judge = request.user.groups.filter(name='Judges').exists()
    is_officer = request.user.groups.filter(name='Officers').exists()

    cases = Case.objects.all().order_by('id')

    print('advocate: ' + str(is_advocate))
    print('judge: ' + str(is_judge))
    print('officer: ' + str(is_officer))

    context = {
        'is_advocate': is_advocate,
        'is_judge': is_judge,
        'is_officer': is_officer,
        'cases': cases,
    }

    if is_judge:
        return render(request, 'judges/all_cases.html', context)
    else:
        return render(request, 'accounts/dashboard.html', context)

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/accounts/login/')
def findcase(request):
    is_advocate = request.user.groups.filter(name='Advocates').exists()
    is_judge = request.user.groups.filter(name='Judges').exists()
    is_officer = request.user.groups.filter(name='Officers').exists()

    if request.method == "POST":
        casetype = request.POST['casetype']
        caseno = request.POST['caseno']
        caseyr = request.POST['caseyr']

        case = Case.objects.get(
            case_type=casetype, case_number=caseno, case_year=caseyr)

        responses = Response.objects.filter(respond_to_case_type=casetype,
                                     respond_to_case_number=caseno,
                                     respond_to_case_year=caseyr,
                                     response_status=1).all()

        context = {
            'is_advocate': is_advocate,
            'is_judge': is_judge,
            'is_officer': is_officer,
            'case': case,
            'responses': responses,
        }

        if is_judge:
            return render(request, 'judges/case_details.html', context)
        else:
            return render(request, 'accounts/dashboard.html', context)

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/accounts/login/')
def view_case(request, case_id):
    is_advocate = request.user.groups.filter(name='Advocates').exists()
    is_judge = request.user.groups.filter(name='Judges').exists()
    is_officer = request.user.groups.filter(name='Officers').exists()

    case = Case.objects.get(id=case_id)

    responses = Response.objects.filter(respond_to_case_type=case.case_type,
                                     respond_to_case_number=case.case_number,
                                     respond_to_case_year=case.case_year,
                                     response_status=1).all()

    print('advocate: ' + str(is_advocate))
    print('judge: ' + str(is_judge))
    print('officer: ' + str(is_officer))

    context = {
        'is_advocate': is_advocate,
        'is_judge': is_judge,
        'is_officer': is_officer,
        'case': case,
        'responses': responses,
    }

    if is_judge:
        return render(request, 'judges/case_details.html', context)
    else:
        return render(request, 'accounts/dashboard.html', context)

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/accounts/login/')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('login')
