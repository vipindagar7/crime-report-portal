from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.http import request
from django.urls import reverse
from django.conf import settings
# from django.contrib.sites.models import Site
def send_verification_email(email , token):
    url = reverse('verify', kwargs={'auth_token': token})
    name = 'vipin'
    subject = "Your account needs to be verified"
    message = f"click on the link to verify your account http://127.0.0.1:8000{url}"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

    