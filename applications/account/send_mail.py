from django.core.mail import send_mail


def send_confirmation_email(code, email):
    link = f'Спасибо за регистрацию! \nДля активации аккаунта перейдите по ссылке: ' \
           f'http://localhost:8000/api/v1/account/active/{code}'
    our_email = 'csqvsr25@gmail.com'

    send_mail('Активация аккаунта', link, our_email, [email])