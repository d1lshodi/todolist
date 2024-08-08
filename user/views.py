from rest_framework import generics
from .models import UserModel
from .serializers import UserModelSerializer , UserLoginSerializer
from rest_framework.response import Response
from rest_framework import status
from .utils import generate_otp
from django.core.mail import send_mail


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserModelSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        username = request.data.get('username')

        otp = generate_otp()

        if UserModel.objects.filter(email=email).exists():
            return Response("Email already registrated", status=status.HTTP_400_BAD_REQUEST)
        elif UserModel.objects.filter(username=username).exists():
            return Response({"This username already taken"}, status=status.HTTP_400_BAD_REQUEST)
    
        data = request.data.copy()
        data['otp'] = otp

        send_mail(
            "Verification Code",
            f"Your verification code is: {otp} ",
            'Todolist <settings.EMAIL_HOST_USER>',
            [email],
            fail_silently=False,
        )

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response("Registrated successfully", status=status.HTTP_200_OK)

    
class OtpVerificationView(generics.GenericAPIView):
    serializer_class = UserModelSerializer

    def post(self, request, *args , **kwargs):
        email = request.data.get('email')
        otp = request.data.get('otp')

    
        if otp == UserModel.objects.get(email=email).otp:
            user = UserModel.objects.get(email=email)
            user.is_active=True
            user.otp = ""
            user.save()
            return Response("Registrated successfully", status=status.HTTP_200_OK)
        else:
            return Response("Otp is wrong", status=status.HTTP_400_BAD_REQUEST)

class LoginApiView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args , **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user  = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return Response("Email didn't registrated", status=status.HTTP_404_NOT_FOUND)
        
        if user.password == password:
            return Response("Login succesfully", status=status.HTTP_200_OK)
        else:
            return Response("Password is wrong", status=status.HTTP_400_BAD_REQUEST)
            