from django.urls import path
from .views import UserCreateView , OtpVerificationView, LoginApiView
urlpatterns = [
    path('api/usercreate/', UserCreateView.as_view()),
    path('api/otpverification/', OtpVerificationView.as_view()),
    path('api/login/', LoginApiView.as_view())
]