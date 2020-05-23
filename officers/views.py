from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import Case

from advocates.models import Filing, Response

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/accounts/login/')
def office_dashboard(request):
    is_advocate = request.user.groups.filter(name='Advocates').exists()
    is_judge = request.user.groups.filter(name='Judges').exists()
    is_officer = request.user.groups.filter(name='Officers').exists()

    filings = Filing.objects.all().order_by('filing_time').filter(filing_status=3)

    print('advocate: ' + str(is_advocate))
    print('judge: ' + str(is_judge))
    print('officer: ' + str(is_officer))

    context = {
        'is_advocate': is_advocate,
        'is_judge': is_judge,
        'is_officer': is_officer,
        'filings': filings,
    }

    if is_officer:
        return render(request, 'officers/dashboard.html', context)
    else:
        return render(request, 'accounts/dashboard.html', context)

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/accounts/login/')
def office_history(request):
    is_advocate = request.user.groups.filter(name='Advocates').exists()
    is_judge = request.user.groups.filter(name='Judges').exists()
    is_officer = request.user.groups.filter(name='Officers').exists()

    filings = Filing.objects.order_by('filing_time').exclude(filing_status=3)
    responses = Response.objects.order_by('response_time').exclude(response_status=3)

    print('advocate: ' + str(is_advocate))
    print('judge: ' + str(is_judge))
    print('officer: ' + str(is_officer))

    context = {
        'is_advocate': is_advocate,
        'is_judge': is_judge,
        'is_officer': is_officer,
        'filings': filings,
        'responses': responses,
    }
    if is_officer:
        return render(request, 'officers/stat_history.html', context)
    else:
        return render(request, 'accounts/dashboard.html', context)

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/accounts/login/')
def view_filing(request, filing_id):
    is_advocate = request.user.groups.filter(name='Advocates').exists()
    is_judge = request.user.groups.filter(name='Judges').exists()
    is_officer = request.user.groups.filter(name='Officers').exists()

    filing = Filing.objects.get(id=filing_id)

    print('advocate: ' + str(is_advocate))
    print('judge: ' + str(is_judge))
    print('officer: ' + str(is_officer))

    context = {
        'is_advocate': is_advocate,
        'is_judge': is_judge,
        'is_officer': is_officer,
        'filing': filing,
    }

    if is_officer:
        return render(request, 'officers/filing_view.html', context)
    else:
        return render(request, 'accounts/dashboard.html', context)

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/accounts/login/')
def view_response(request, response_id):
    is_advocate = request.user.groups.filter(name='Advocates').exists()
    is_judge = request.user.groups.filter(name='Judges').exists()
    is_officer = request.user.groups.filter(name='Officers').exists()

    response = Response.objects.get(id=response_id)

    print('advocate: ' + str(is_advocate))
    print('judge: ' + str(is_judge))
    print('officer: ' + str(is_officer))

    context = {
        'is_advocate': is_advocate,
        'is_judge': is_judge,
        'is_officer': is_officer,
        'response': response,
    }

    if is_officer:
        return render(request, 'officers/response_view.html', context)
    else:
        return render(request, 'accounts/dashboard.html', context)

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/accounts/login/')
def view_sorted_filing(request, filing_id):
    is_advocate = request.user.groups.filter(name='Advocates').exists()
    is_judge = request.user.groups.filter(name='Judges').exists()
    is_officer = request.user.groups.filter(name='Officers').exists()

    filing = Filing.objects.get(id=filing_id)

    print('advocate: ' + str(is_advocate))
    print('judge: ' + str(is_judge))
    print('officer: ' + str(is_officer))

    context = {
        'is_advocate': is_advocate,
        'is_judge': is_judge,
        'is_officer': is_officer,
        'filing': filing,
    }

    if is_officer:
        return render(request, 'officers/sorted_filing.html', context)
    else:
        return render(request, 'accounts/dashboard.html', context)

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/accounts/login/')
def view_sorted_response(request, response_id):
    is_advocate = request.user.groups.filter(name='Advocates').exists()
    is_judge = request.user.groups.filter(name='Judges').exists()
    is_officer = request.user.groups.filter(name='Officers').exists()

    response = Response.objects.get(id=response_id)

    print('advocate: ' + str(is_advocate))
    print('judge: ' + str(is_judge))
    print('officer: ' + str(is_officer))

    context = {
        'is_advocate': is_advocate,
        'is_judge': is_judge,
        'is_officer': is_officer,
        'response': response,
    }

    if is_officer:
        return render(request, 'officers/sorted_response.html', context)
    else:
        return render(request, 'accounts/dashboard.html', context)


@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/accounts/login/')
def assign_case(request):
    if request.method == "POST":
        from .models import Case

        filing_id = request.POST['filing_id']
        filing = Filing.objects.get(id=filing_id)

        sr8 = request.POST.get('rule8', False)
        if sr8 == 'on':
            sr8 = True
        else:
            sr8 = False

        sr9 = request.POST.get('rule9', False)
        if sr9 == 'on':
            sr9 = True
        else:
            sr9 = False

        sr10 = request.POST.get('rule10', False)
        if sr10 == 'on':
            sr10 = True
        else:
            sr10 = False

        sr11 = request.POST.get('sr11', False)
        if sr11 == 'on':
            sr11 = True
        else:
            sr11 = False

        sr15 = request.POST.get('rule15', False)
        if sr15 == 'on':
            sr15 = True
        else:
            sr15 = False

        sr16 = request.POST.get('rule16', False)
        if sr16 == 'on':
            sr16 = True
        else:
            sr16 = False

        sr17 = request.POST.get('rule17', False)
        if sr17 == 'on':
            sr17 = True
        else:
            sr17 = False

        sr21 = request.POST.get('rule21', False)
        if sr21 == 'on':
            sr21 = True
        else:
            sr21 = False

        sr25 = request.POST.get('rule25', False)
        if sr25 == 'on':
            sr25 = True
        else:
            sr25 = False

        sr31 = request.POST.get('rule31', False)
        if sr31 == 'on':
            sr31 = True
        else:
            sr31 = False

        remarks = request.POST['remarks']

        status = request.POST['caseChoiceRadio']

        filing.filing_comments = ''

        filing.filing_comments += remarks

        if (not sr8):
            filing.filing_comments += " Refer Serial No. 8 of checklist."
        if (not sr9):
            filing.filing_comments += " Refer Serial No. 9 of checklist."
        if (not sr10):
            filing.filing_comments += " Refer Serial No. 10 of checklist."
        if (not sr11):
            filing.filing_comments += " Refer Serial No. 11 of checklist."
        if (not sr15):
            filing.filing_comments += " Refer Serial No. 15 of checklist."
        if (not sr16):
            filing.filing_comments += " Refer Serial No. 16 of checklist."
        if (not sr17):
            filing.filing_comments += " Refer Serial No. 17 of checklist."
        if (not sr21):
            filing.filing_comments += " Refer Serial No. 21 of checklist."
        if (not sr25):
            filing.filing_comments += " Refer Serial No. 25 of checklist."
        if (not sr31):
            filing.filing_comments += " Refer Serial No. 31 of checklist."

        if status == "True":
            if filing.filing_status == 3:
                case_type = request.POST['finalCT']
                case_num = request.POST['finalCNo']
                case_yr = request.POST['finalCYr']
                bench_type = request.POST['BenchFinal']

                print('Case filed: ' + case_type + '/' + str(case_num) +
                    '/' + str(case_yr) + ' for filing id ' + filing_id)

                filing.filing_case = case_type + '/' + \
                    str(case_num) + '/' + str(case_yr)
                filing.filing_status = 1
                filing.filing_comments = "Further case information available on High Court Website."
                filing.officer_stamp = request.user.get_username()

                file_case = Case(filing=filing, case_type=case_type, case_number=case_num,
                                case_year=case_yr, bench_type=bench_type)

                filing.save()
                file_case.save()
            else:
                print('Matter already sorted')
        else:
            filing.officer_stamp = request.user.get_username()
            filing.filing_case = 'N.A.'
            filing.filing_status = 0
            filing.save()

        return redirect('/dashboard')

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/accounts/login/')
def response_approval_list(request):
    is_advocate = request.user.groups.filter(name='Advocates').exists()
    is_judge = request.user.groups.filter(name='Judges').exists()
    is_officer = request.user.groups.filter(name='Officers').exists()

    responses = Response.objects.all().order_by('response_time').filter(response_status=3)

    print('advocate: ' + str(is_advocate))
    print('judge: ' + str(is_judge))
    print('officer: ' + str(is_officer))

    context = {
        'is_advocate': is_advocate,
        'is_judge': is_judge,
        'is_officer': is_officer,
        'responses': responses,
    }

    if is_officer:
        return render(request, 'officers/response_approval_list.html', context)
    else:
        return render(request, 'accounts/dashboard.html', context)

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/accounts/login/')
def accept_response(request):
    if request.method == "POST":
        response_id = request.POST['response_id']
        response = Response.objects.get(id=response_id)

        remarks = request.POST['remarks']
        response.response_comments = remarks

        status = request.POST['caseChoiceRadio']

        response.officer_stamp = request.user.get_username()

        if status == "True":
            response.response_status = 1
            response.response_comments += " Further case information available on High Court Website."
            response.save()

        else:
            response.response_status = 0
            response.save()

        return redirect('/dashboard')

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/accounts/login/')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('login')
