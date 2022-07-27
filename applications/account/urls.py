from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from applications.account.views import *

urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    path('active/<uuid:activation_code>/', ActivationView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    #TODO
    path('forgot_password/', ForgotPasswordView.as_view()),
    path('password_recovery/', ForgotPasswordComplete.as_view()),
    path('change_password/', ChangePasswordView.as_view()),
    path('logout/', LogOutApiView.as_view()),
]