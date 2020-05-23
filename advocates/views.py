from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from django.core.files.storage import FileSystemStorage

from .models import Filing, Response

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/accounts/login/')
def lawyer_dashboard(request):
    is_advocate = request.user.groups.filter(name='Advocates').exists()
    is_judge = request.user.groups.filter(name='Judges').exists()
    is_officer = request.user.groups.filter(name='Officers').exists()

    filings = Filing.objects.all().filter(filing_advocate=request.user.id).order_by('filing_time')

    responses = Response.objects.all().filter(responding_advocate=request.user.id).order_by('response_time')
    
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
    
    if is_advocate:
        return render(request, 'advocates/dashboard.html', context)
    else:
        return render(request, 'accounts/dashboard.html', context)

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/accounts/login/')
def fresh_filing(request):
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
    
    if is_advocate:
        return render(request, 'advocates/fresh_filing.html', context)
    else:
        return render(request, 'accounts/dashboard.html', context)

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/accounts/login/')
def respond_case(request):
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
    
    if is_advocate:
        return render(request, 'advocates/respond_case.html', context)
    else:
        return render(request, 'accounts/dashboard.html', context)

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/accounts/login/')
def view_petetion(request, petetion_id):
    is_advocate = request.user.groups.filter(name='Advocates').exists()
    is_judge = request.user.groups.filter(name='Judges').exists()
    is_officer = request.user.groups.filter(name='Officers').exists()

    filing = Filing.objects.get(id=petetion_id)

    print('advocate: ' + str(is_advocate))
    print('judge: ' + str(is_judge))
    print('officer: ' + str(is_officer))

    context = {
        'is_advocate': is_advocate,
        'is_judge': is_judge,
        'is_officer': is_officer,
        'filing': filing,
    }

    if is_advocate:
        return render(request, 'advocates/petetion_detail.html', context)
    else:
        return render(request, 'accounts/dashboard.html', context)

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/accounts/login/')
def advocate_view_response(request, response_id):
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

    if is_advocate:
        return render(request, 'advocates/response_detail.html', context)
    else:
        return render(request, 'accounts/dashboard.html', context)

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/accounts/login/')
def file_matter(request):
    if request.method == 'POST':
        matterType = request.POST['TypeSelect']
        benchType = request.POST['BenchSelect']
        caseType = request.POST['CaseType']
        rules = request.POST['provision']
        connectedStatus = request.POST['connectedRadioOptions']
        advocate_hc_code = request.POST['AdvCode']
        sanat_number = request.POST['SanatNo']

        urgencyStatus = request.POST['urgentRadioOptions']
        urgencyFile = request.FILES.get('urgencyFile', False)

        indexFile = request.FILES['indexFile']
        LoEventsFile = request.FILES['LoEventsFile']
        synopsisFile = request.FILES['synopsisFile']
        memoFile = request.FILES['memoFile']
        pastFile = request.FILES['pastFile']
        annexFile = request.FILES.get('annexFile', False)
        vnamFile = request.FILES['vnamFile']
        othFile = request.FILES.get('othFile', False)

        print('Urgency files are: '+ str(urgencyFile))

        connected_case_type = ''
        connected_case_number = 0
        connected_case_year = 0

        if connectedStatus is "True":
            connected_case_type = request.POST['ConnectedCaseType']
            connected_case_number = request.POST['ccno']
            connected_case_year = request.POST['ccyr']
        else:
            connected_case_type = ''
            connected_case_number = 0
            connected_case_year = 0
        
        filing_matter = Filing(filing_advocate=request.user, sanat_number=sanat_number, rules=rules, matter_type=matterType, bench_type=benchType,
        case_type=caseType, connected_case=connectedStatus, connected_case_type=connected_case_type, connected_case_number=connected_case_number,
        connected_case_year=connected_case_year, filing_urgency=urgencyStatus, advocate_hc_code=advocate_hc_code, urgencyFile=urgencyFile,
        indexFile=indexFile, LoEventsFile=LoEventsFile, synopsisFile=synopsisFile, memoFile=memoFile, pastFile=pastFile, annexFile=annexFile,
        vnamFile=vnamFile,othFile=othFile)

        filing_matter.save()

        messages.success(request, 'Your filing has been submitted.')
        
        return redirect('lawyer_dashboard')

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/accounts/login/')
def file_response(request):
    if request.method == 'POST':
        sanat_number = request.POST['SanatNo']        
        advocate_hc_code = request.POST['advocate_hc_code']
        casetype = request.POST['casetype']
        casenumber = request.POST['ccno']
        caseyear = request.POST['ccyr']

        ruledmatter = request.POST.get('ruled_matter', False)
        if ruledmatter == 'on':
            ruledmatter = True
        else:
            ruledmatter = False
        
        vakalatnama = request.FILES['vakalatnama']
        affidavitInResponse = request.FILES.get('responseFile', False)
        furtherResponseFile = request.FILES.get('furtherResponseFile', False)
        otherFiles = request.FILES.get('otherFiles', False)

        response_note = request.POST['note']

        respond = Response(responding_advocate=request.user, sanat_number=sanat_number, advocate_hc_code=advocate_hc_code, respond_to_case_type=casetype, respond_to_case_number=casenumber, respond_to_case_year=caseyear,
        ruled_matter=ruledmatter, vnamFile=vakalatnama, affidavit_in_response=affidavitInResponse, further_affidavit=furtherResponseFile,
        othFile=otherFiles, response_note=response_note)

        respond.save()

        messages.success(request, 'Your response has been submitted.')
        
        return redirect('lawyer_dashboard')
    
    return redirect('lawyer_dashboard')

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/accounts/login/')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('login')
