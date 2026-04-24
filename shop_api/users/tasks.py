from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def add(x, y):
    print(f"args: {x} + {y}")
    from time import sleep

    sleep(40)
    return x + y


@shared_task
def send_otp_mail(email, code):
    send_mail(
        "Your OTP-CODE",
        f"Ваш одноразовый код {code}",
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
    return "OK"


@shared_task
def send_report_mail():
    send_mail(
        "Daily Report",
        "что то оченб важное",
        settings.EMAIL_HOST_USER,
        ["riszav.01@gmail.com"],
        fail_silently=False,
    )
    return "OK"\

@shared_task
def create_reminder(title):
    print(" 🔔 Напоминание" , title)

@shared_task
def send_reminder_email(email, title):
    send_mail(
        subject="Напоминание",
        message=f"🔔 {title}",
        from_email="arturkuchanbai@email.com",
        recipient_list=[email],
        fail_silently=False,
    )

    