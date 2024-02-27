from django.template.loader import render_to_string
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import SubEmail
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render


@api_view(['POST'])
def sub_or_unsub(request):
    r_email = request.query_params.get('email')
    r_name = request.query_params.get('name')
    r_frequency = request.query_params.get('frequency')
    r_sub = request.query_params.get('state')
    r_id = request.query_params.get('id')

    if r_sub == 'True' and r_id is not None:
        try:
            email = SubEmail.objects.get(id=int(r_id))
            if email.sub_state == False and email.frequency == r_frequency:
                email.sub_state = True
                email.save()
                return Response({'You Resubscribed to our NewLetter Successfuly :)'})
            elif email.sub_state != False and email.frequency != r_frequency:
                old_frequency = email.frequency
                email.frequency = r_frequency
                email.save()
                return Response({f"You change your newletter from {old_frequency} to {email.frequency} Successfuly :)"})
            else:
                return Response({'You are already Subscribed to our NewLetter :p'})
        except:
            return Response({'your id dose not exist'})
    elif r_sub == 'True' and r_id is None and r_frequency is not None:
        email = SubEmail.objects.create(
            email=r_email, name=r_name, sub_state=True, frequency=r_frequency)
        print(
            f"{email.name} with email: {email.email} was with [sub] for {email.frequency} added to db")
        template = render_to_string(
            'api/subemail.html', {'subed': True, 'myname': settings.EMAIL_NAME})
        try:
            send_mail(
                "Sub to our newsletter",
                template,
                settings.EMAIL_HOST_USER,
                [email.email],
                fail_silently=False,
            )
            return Response({'Your Subscribed to our NewLetter Successfuly :)'})
        except:
            return Response({'Your Subscribed to our NewLetter Successfuly :) but no email was sent because email system was not setup properly'})
    elif r_sub == 'False' and r_id is not None:
        try:
            email = SubEmail.objects.get(id=int(r_id))
            if email.sub_state != False:
                email.sub_state = False
                email.save()
                return Response({'Your have Unsubscribed from our NewLetter Successfuly :('})
            else:
                return Response({'You are already Unsubscribed to our NewLetter :('})
        except:
            return Response({'your id dose not exist'})


def chackmail(request):
    send_mail(
        'testing mail',
        'body of content',
        settings.EMAIL_HOST_USER,
        ['mukithasan58@gmail.com'],
        fail_silently=False,
    )
    return render(request, 'api/subemail.html', {'subed': True})
