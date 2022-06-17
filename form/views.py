from ast import alias
from django.http import HttpRequest
from django.shortcuts import render
from . import models

def form(request: HttpRequest):
    if request.method == "POST":
        check_others = lambda current, other: request.POST[other] if current == 'other' else current
        check_checkbox = lambda check, file: request.POST[file] if not check == 'none' else None
        check_file = lambda check, data_name: request.FILES[data_name] if not check == 'none' else None
        check_image = lambda check, data_name: request.FILES[data_name] if check == '1' else None

        print(check_others(request.POST['form4title[]'], 'form4title-other'),)
        print(request.POST['form4given-name'],)
        print(request.POST['form4family-name'],)
        print(request.POST['form4gender[]'],)
        print(request.POST['form4email'],)
        print(request.POST['form4telephone'],)
        print(check_others(request.POST['form4academic-status[]'], 'form4academic-status-other'),)
        print(check_others(request.POST['form4country-origin[]'], 'form4origin-other'),)
        print(check_others(request.POST['form4current-location[]'], 'form4current-location-other'),)
        print(request.POST['form4profession'],)
        print(request.POST['form4university'],)
        print(request.POST['form4participation-type'],)
        print(request.POST['form4presentation-title'],)
        print(check_checkbox(request.POST['form4abstract-enter'], 'form4abstract'),)
        print(check_checkbox(request.POST['form4short-cv-enter'], 'form4short-cv'),)
        print(check_file(request.POST['form4presentation-upload-option'], 'form4presentation-upload'),)
        print(check_image(request.POST.get('form4announce'), 'form4portrait-upload'))

        title = f"{check_others(request.POST['form4title[]'], 'form4title-other')} {request.POST['form4given-name']} {request.POST['form4family-name']}"

        print(title)

        data = models.ConfContent(
            title = title
        )
        data.save()
        
        return render(request, 'thank.html')
    return render(request, 'form.html')