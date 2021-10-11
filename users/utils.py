from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token


def email_verification(subject,message,user,domain):
    subject = "Activate Your Cscart Account"
    message = render_to_string(
        "emails/account_activation_email.html",
        {
            "user": user,
            "domain": domain,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": account_activation_token.make_token(user),
        },
    )
    user.email_user(subject,message)
