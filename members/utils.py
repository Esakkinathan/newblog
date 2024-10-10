# your_app/utils.py

import random
from django.core.mail import send_mail
from .models import OTP

def generate_otp(email):
    OTP.objects.filter(email=email).delete()
    otp = ''.join(random.choices('0123456789', k=6))
    OTP.objects.create(email=email, otp=otp)
    send_otp_email(email, otp)

def send_otp_email(email, otp):
    subject = 'Your OTP Code'
    message = f'Thank You for using heyblog.\nYour OTP code is {otp}.\n It is valid for 10 minutes.'
    email_from = 'passw6443@gmail.com'
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
