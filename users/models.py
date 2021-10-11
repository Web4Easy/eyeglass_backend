from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import EmailMultiAlternatives
from django.template import RequestContext
from django.template.loader import render_to_string
from django.core.mail import send_mail  
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.utils.translation import ugettext_lazy as _
from django.utils.html import strip_tags
from django.conf import settings



# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=20,null=True,blank=True)






@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    # logo = NottingHillLawLogo.objects.all()[0]
    # logo = settings.BACKEND_DOMAIN + logo.logo.url
    html_content = render_to_string(
        "emails/reset_password.html",
        {
            "verification_link":"{}/{}?token={}".format(settings.FRONT_END_URL,'users/password_reset/', reset_password_token.key),
            # "logo": logo,
        },
    )
    text_context = strip_tags(html_content)
    email = EmailMultiAlternatives(
        f'Password-Reset-Link for CSCART',
        text_context,
        settings.EMAIL_HOST_USER,
        [reset_password_token.user.email]
    )
    email.attach_alternative(html_content, "text/html")
    email.send()