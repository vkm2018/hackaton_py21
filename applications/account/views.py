from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from applications.account.serializers import RegisterSerializer, LoginSerializer, ChangePasswordSerializer

User = get_user_model()


class RegisterApiView(APIView):
    def post(self, request):
        data = request.data
        serializaers = RegisterSerializer(data=data)

        if serializaers.is_valid(raise_exception=True):
            serializaers.save()
            message = f'На Вашу почту отправлено письмо с активацией'
            return Response(message, status=201)


class ActivationView(APIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response({'Ваш аккаунт успешно активирован'}, status=200)
        except User.DoesNotExist:
            return Response({'Неверный код!'}, status=400)


class LoginAPIView(ObtainAuthToken):
    serializer_class = LoginSerializer


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializers = ChangePasswordSerializer(data=request.data, context={'request': request})

        serializers.is_valid(raise_exception=True)
        serializers.set_new_password()
        return Response('Пароль успешно обновлен!')


class LogOutApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            user = request.user
            Token.objects.filter(user=user).delete()
            return Response('Вы успешно разлогинились')
        except:
            return Response(status=403)
