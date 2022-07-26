from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from applications.account.send_mail import send_confirmation_email

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(min_length=8, write_only=True, required=True)


    class Meta:
        model = User
        fields = ['email', 'password', 'password2']

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.pop('password2')

        if password != password2:
            raise serializers.ValidationError('Password did not match')

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        code = user.activation_code
        send_confirmation_email(code, user.email)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate_emal(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь не зарегестрирован!')
        return email

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(username=email, password=password)

            if not user:
                raise serializers.ValidationError('Неверный email или пароль!')

            attrs['user'] = user
            return attrs


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    password = serializers.CharField(required=True, min_length=6)
    password2 = serializers.CharField(required=True, min_length=6)

    def validate_old_password(self, p):
        user = self.context.get('request').user
        if not user.check_password(p):
            raise serializers.ValidationError('Неверный пароль')
        return p

    def validate(self, attrs):
        pass1 = attrs.get('password')
        pass2 = attrs.get('password2')
        if pass1 != pass2:
            raise serializers.ValidationError('Пароли не совпадают')

        return attrs

    def set_new_password(self):
        user = self.context.get('request').user
        print(dir(self.validated_data))
        password = self.validated_data.get('password')
        user.set_password(password)
        user.save()