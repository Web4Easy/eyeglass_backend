from django.shortcuts import render
from rest_framework.decorators import action, permission_classes,api_view  # other imports elided
from oauth2_provider.models import AccessToken,RefreshToken,Application
from oauth2_provider.scopes import oauth2_settings
from datetime import datetime,timedelta
from oauthlib import common
from .tokens import account_activation_token
from .utils import email_verification
from rest_framework import generics

from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

# Create your views here.
# @api_view(['POST'])
# def register_user(request):

#     data = request.data
#     try:
#         user = User.objects.create(
#             first_name=data['first_name'],
#             last_name=data['last_name'],
#             username=data['email'],
#             email=data['email'],
#             is_active=False,
#             password=make_password(data['password'])
#         )
#         email_verification("hello","message",user,"localhost")
#         serializer = UserSerializer(user, many=False)
#         return Response(serializer.data)
#     except:
#         message = {'detail': 'User with this email already exists'}
#         return Response(message, status=400)    



# @api_view(['GET'])
# def activate_account(request,uidb64,token):

#     """
#     http://localhost/users/activate/MTc/atdqa8-1b0db16ddca2b9ea6285deba408a8c51/
#     """
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None

#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()

#         """
#         for getting access token from djangooauthtoolkit
#         """
#         expire_seconds =360000
#         expires =  datetime.now() + timedelta(seconds=expire_seconds)
#         scopes = "read write"
#         application = Application.objects.all()[0]
#         access_token = AccessToken.objects.create(
#                 user=user,
#                 application=application,
#                 token=common.generate_token(),
#                 expires=expires,
#                 scope=scopes)

#         refresh_token = RefreshToken.objects.create(
#                 user=user,
#                 application=application,
#                 token=common.generate_token(),
#                 access_token=access_token,
#                 )
        
#         return Response(access_token.token)
#     else:
#         return Response({'detail':"The confirmation link was invalid, possibly because it has already been used"})


# @api_view(['PUT'])
# @permission_classes([IsAuthenticated])
# def update_user(request,pk):

#     """
#     Function for register user 
#     with one validation if user exist
#     """


#     data = request.data
#     user = request.user
#     try:
#         if user:
#             user.first_name = data.get('first_name')
#             user.last_name = data.get('last_name')
#             user.phone = data.get('phone')
#             if data.get('password')!="":
#                 match_check = check_password(data['last_password'],user.password)
#                 if match_check:
#                     user.password = make_password(data['password'])
#                 else:
#                     return Response({'detail':"Your password is not match"},status=400)
#             user.save()
#         serializer = UserSerializer(user,many=False)
#         return Response(serializer.data)
#     except Exception as e:
#         return Response({'detail':'Object not found'},status=400)


# class GetUser(generics.RetrieveAPIView):
#     """
#     User detail for admin and single user
    
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]
#     def get(self,request,*args,**kwargs):
#         """
#         user based
#         """
#         try:
#             serializer = self.get_serializer(request.user,many=False)
#             return Response(serializer.data)
#         except:
#             return Response({"detail":"Wrong api Endpoints"},status=400)