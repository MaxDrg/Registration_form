from django.utils.datastructures import MultiValueDict
from django.http.request import QueryDict
from django.http import HttpRequest
from django.shortcuts import render
from . import models, emails

def form(request: HttpRequest):
    if request.method == "POST":
        post: QueryDict = request.POST
        files: MultiValueDict = request.FILES

        check_title     = lambda title: title if not title == 'Choose a value' else ''
        check_others    = lambda current, other: post[other] if current == 'other' else current
        check_checkbox  = lambda check, file: post[file] if not check == 'none' else None
        check_file      = lambda check, data_name: files[data_name] if not check == 'none' and file_exist(files, data_name) else None
        check_image     = lambda check, data_name: files[data_name] if check == '1' and file_exist(files, data_name) else None

        academic_title  = check_title(post['form4title[]'])
        tags            = post.getlist('form4profession[]')
        university      = post['form4university']
        email           = post['form4email']
        family_name     = post['form4family-name']
        phone           = post['form4telephone']

        particip            = post['form4participation-type']
        sess_lead           = None
        presentation_title  = None
        announce            = None
        abstract            = None
        cv                  = None
        image               = None
        presentation_upload = None
        social_med          = None

        title = f"{post['form4given-name']} {post['form4family-name']}"
        if academic_title:
            title = f"{academic_title} {post['form4given-name']} {post['form4family-name']}"
        
        if particip == 'listen':
            sess_lead           = post.get('form4session-lead')
        else:
            announce            = post.get('form4announce')
            presentation_title  = post['form4presentation-title']
            abstract            = check_checkbox(post['form4abstract-enter'], 'form4abstract')
            cv                  = check_checkbox(post['form4short-cv-enter'], 'form4short-cv')
            presentation_upload = check_file(post['form4presentation-upload-option'], 'form4presentation-upload')
            image               = check_image(announce, 'form4portrait-upload')
            social_med          = post.get('form4social-media')

        # Adding data in the storage
        data = models.Content(
            academic_title      = academic_title,
            given_name          = post['form4given-name'],
            family_name         = family_name,
            gender              = post['form4gender[]'],
            email               = email,
            telephone           = phone,
            academic_status     = check_others(post['form4academic-status[]'], 'form4academic-status-other'),
            country_origin      = check_others(post['form4country-origin[]'], 'form4origin-other'),
            current_location    = check_others(post['form4current-location[]'], 'form4current-location-other'),
            profession          = tags,
            profession_other    = (lambda professions: professions if professions else None)(post.get('form4profession-other')),
            university          = university,
            type_participation  = particip,
            presentation_title  = presentation_title,
            abstract            = abstract,
            short_cv            = cv,
            presentation_upload = presentation_upload,
            portrait            = image,
            session_lead        = sess_lead,
            social_media        = social_med,
        )
        data.save()

        img: str = '{"image_intro":"images\/Profil.png","float_intro":"","image_intro_alt":"' + title \
                + '","image_intro_caption":"","image_fulltext":"images\/Profil.png","float_fulltext":"","image_fulltext_alt":"' \
                + title + '","image_fulltext_caption":""}'

        if data.portrait:
            url = f'https://registration.chance-for-science.eu{data.portrait.url}'
            img = '{"image_intro":"' + url + '","float_intro":"","image_intro_alt":"' + title \
                + '","image_intro_caption":"","image_fulltext":"' + url + '","float_fulltext":"","image_fulltext_alt":"' \
                + title + '","image_fulltext_caption":""}'

        access: int = (lambda abstract, cv, check: 1 if abstract and cv and check == '1' else 0)(abstract, cv, announce)

        core_id = models.ConfsepContentitemTagMap.objects.latest('core_content_id').core_content_id + 1

        introtext = ''
        if cv and abstract:
            introtext = f"<p><strong>{title}</strong></p>" \
                    f"<p>{university[0]}</p>" \
                    f"<p><strong>CV:</strong> {cv}</p>" \
                    f"<p><strong>Presentation title:</strong> {presentation_title}</p>" \
                    f"<p><strong>Abstract:</strong> {abstract}</p>"

        # Adding data on the website
        data = models.ConfsepContent(
            title       = title,
            alias       = family_name.lower(),
            introtext   = introtext,
            images      = img,
            access      = access
        )
        data.save()

        # Adding tags
        for tag in tags:
            if tag == 'other': continue
            new_tag = models.ConfsepTags.objects.filter(title=tag)
            if not new_tag.exists():
                low_tag  = tag.replace(' ', '-').lower()
                last_rgt = models.ConfsepTags.objects.latest('rgt').rgt + 1

                new_tag  = [models.ConfsepTags(
                    lft     = last_rgt,
                    rgt     = last_rgt + 1,
                    title   = tag,
                    path    = low_tag,
                    alias   = low_tag
                )]
                new_tag[0].save()
            models.ConfsepContentitemTagMap(
                core_content_id = core_id,
                content_item_id = data.id,
                tag_id          = new_tag[0].id
            ).save()

        # Sending emails
        email_sender = emails.Email(email)
        email_sender.send_email(registr_message(title, access, cv, abstract))
        email_sender.send_email(email_notification(
            part_type   = particip, 
            title       = title,
            email       = email, 
            phone       = phone, 
            university  = university, 
            presen      = presentation_title, 
            cv          = cv,
            abstract    = abstract
        ))

        # Error message
        alert = ''
        if not particip == 'listen' and announce:
            if not abstract or not cv:
                alert = 'But you need to add abstract and short CV to display you on the website.'
        
        return render(request, 'thank.html', {
            'title': title,
            'additional': alert
        })

    return render(request, 'form1.html')

def file_exist(files: MultiValueDict, key: str):
    for current_key in files.keys():
        if current_key == key:
            return True
    return False

def registr_message(title: str, access: int, cv, abstract):
    
    notification = ''
    
    if access == '0':
        option = 'CV and Abstract'
        if abstract:
            option = 'CV'
        elif cv:
            option = 'Abstract'
        notification = f"""
            You did not input your {option} while registration. If you want us to update your Online 
            profile, please send us these information to conference@chance-for-science.de

            You will receive further information on how to join the online conference later.

        """

    message = f"""
        Dear {title}

        Thank you for your registration for the Chance for Science Conference 2022 on September, 8-9 2022.

        {notification}
        Please do not hesitate to contact us for any questions (just reply to this mail).

        Sincerely,

        The Chance for Science Team
    """
    return message

def email_notification(part_type: str, title: str, email: str, phone: str, 
                    university: str, presen: str, cv: str, abstract: str):
    message = f"""
        New registration:

        Participation-Type: {part_type}

        Form Data:

        Name: {title}
        Email: {email}
        Phone: {phone}
        University: {university}
        Presentation title: {presen}

        CV: {cv}

        Abstract: {abstract}

        --Automatische Mail--
    """

    return message