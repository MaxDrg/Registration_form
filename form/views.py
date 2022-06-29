from django.http import HttpRequest
from django.shortcuts import render
from . import models

def form(request: HttpRequest):
    if request.method == "POST":
        check_title = lambda title: title if not title == 'Choose a value' else ''
        check_others = lambda current, other: request.POST[other] if current == 'other' else current
        check_checkbox = lambda check, file: request.POST[file] if not check == 'none' else None
        check_file = lambda check, data_name: request.FILES[data_name] if not check == 'none' and not request.POST.get(data_name) == '' else None
        check_image = lambda check, data_name: request.FILES[data_name] if check == '1' and not request.POST.get(data_name) == '' else None
        check_access = lambda abstract, cv, check: 1 if abstract and cv and image and check == '1' else 0

        academic_title = check_title(request.POST['form4title[]'])

        title = f"{request.POST['form4given-name']} {request.POST['form4family-name']}"
        if academic_title:
            title = f"{academic_title} {request.POST['form4given-name']} {request.POST['form4family-name']}"

        announce = request.POST.get('form4announce')
        abstract = check_checkbox(request.POST['form4abstract-enter'], 'form4abstract')
        cv = check_checkbox(request.POST['form4short-cv-enter'], 'form4short-cv')
        image = check_image(announce, 'form4portrait-upload')

        data = models.Content(
            academic_title      = academic_title,
            given_name          = request.POST['form4given-name'],
            family_name         = request.POST['form4family-name'],
            gender              = request.POST['form4gender[]'],
            email               = request.POST['form4email'],
            telephone           = request.POST['form4telephone'],
            academic_status     = check_others(request.POST['form4academic-status[]'], 'form4academic-status-other'),
            country_origin      = check_others(request.POST['form4country-origin[]'], 'form4origin-other'),
            current_location    = check_others(request.POST['form4current-location[]'], 'form4current-location-other'),
            profession          = request.POST.getlist('form4profession[]'),
            university          = request.POST['form4university'],
            type_participation  = request.POST['form4participation-type'],
            presentation_title  = request.POST['form4presentation-title'],
            abstract            = abstract,
            short_cv            = cv,
            presentation_upload = check_file(request.POST['form4presentation-upload-option'], 'form4presentation-upload'),
            portrait            = image
        )
        data.save()

        img = '{"image_intro":"images\/Profil.png","float_intro":"","image_intro_alt":"' + title \
                + '","image_intro_caption":"","image_fulltext":"images\/Profil.png","float_fulltext":"","image_fulltext_alt":"' \
                + title + '","image_fulltext_caption":""}'

        if data.portrait:
            url = f'http://h2976860.stratoserver.net{data.portrait.url}'
            img = '{"image_intro":"' + url + '","float_intro":"","image_intro_alt":"' + title \
                + '","image_intro_caption":"","image_fulltext":"' + url + '","float_fulltext":"","image_fulltext_alt":"' \
                + title + '","image_fulltext_caption":""}'

        access = check_access(abstract, cv, announce)

        core_id = models.ConfContentitemTagMap.objects.latest('core_content_id').core_content_id + 1

        data = models.ConfContent(
            title   = title,
            introtext = abstract,
            fulltext = cv,
            images  = img,
            access  = access
        )
        data.save()

        tags = request.POST.getlist('form4profession[]')

        for tag in request.POST.get('form4other-profession').split('|'):
            low_tag = tag.replace(' ', '-').lower()
            last_rgt = models.ConfTags.objects.latest('rgt').rgt + 1
            new_tag = models.ConfTags(
                lft = last_rgt,
                rgt = last_rgt + 1,
                title = tag,
                path = low_tag,
                alias = low_tag
            )
            new_tag.save()
            tags.append(new_tag.id)

        for tag in tags:
            models.ConfContentitemTagMap(
                core_content_id = core_id,
                content_item_id = data.id,
                tag_id = tag
            ).save()
        
        return render(request, 'thank.html')

    return render(request, 'form.html', 
        {
            'professions': models.ConfTags.objects.all()
        })