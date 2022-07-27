from django.core.mail import send_mail

our_email = 'csqvsr25@gmail.com'

def send_confirmation(code, email):
    link = f'Спасибо за регистрацию! \nДля активации аккаунта перейдите по ссылке: ' \
           f'http://localhost:8000/api/v1/account/active/{code}'
    send_mail('Активация аккаунта', link, our_email, [email])

def send_code_recovery(code, email):
    send_mail('Восстановление пароля', f'Ваш код подтверждения: {code}', our_email, [email])