from django.shortcuts import render , redirect
from . models import case
from accounts.models import Custom_user
from django.contrib import messages
# Create your views here.

def newReport(request):
    if request.method == 'POST':
        case_name = request.POST['case_name']
        case_type = request.POST['case_type']
        case_description = request.POST['case_description']
        case_date = request.POST['case_date']
        case_location = request.POST['case_location']
        address = request.POST['address']
        case_files = request.FILES['case_files']
        user = request.user
        new_case = case(case_name = case_name , case_type = case_type , case_description = case_description ,address=address, case_date = case_date , case_location = case_location , case_files = case_files , user = user)
        new_case.save()
    return render(request , 'reports/add.html')

def editReport(request):
    return render(request , 'reports/edit.html')


def cases(request):
    if request.user.is_inspector:
        cases = case.objects.filter(inspector = request.user)
    elif request.user.is_superuser:
        cases = case.objects.all()
    else:
        cases = case.objects.filter(user = request.user)
    context = {'cases': cases}   
    return render(request , 'reports/cases.html' , context)


def view_case(request , id):
    case_obj = case.objects.get(case_id = id)
    if request.method == 'POST':
        
        if request.user.is_superuser:
            case_obj.case_status = request.POST['case_status']
            if request.POST['inspector']:
                case_obj.inspector = Custom_user.objects.get(id = request.POST['inspector'])
            case_obj.save()
            messages.success(request , 'Case updated successfully')
            return render(request , 'reports/view_case.html' , {'case': case_obj})
        elif request.user.is_inspector:
            case_obj.case_status = request.POST['case_status']
            case_obj.save()
            messages.success(request , 'Case updated successfully')
            return render(request , 'reports/view_case.html' , {'case': case_obj})
        else:
            
            
            return redirect('/reports/cases/'+str(id))
    inspectors = Custom_user.objects.filter(is_inspector = True)
    context = {'case': case_obj, 'inspectors': inspectors}
    return render(request , 'reports/view_case.html' , context)

