from django.contrib import admin
from django.urls import path,include
from .views import *

app_name = "system"
urlpatterns = [
    path('',loadLogin,name="Index"),
    path('criteria/',loadCriteria,name="criteria"),
    path('login/',login.as_view(),name="Login"),
    path('find_students/',criteria.as_view(),name="FindStudents"),
    path('register_student/', loadSignup, name="Signup"),
    path('register/', reg.as_view(), name="register"),
    path('profile/', profiles.as_view(), name="profile"),
    path('ForgotPassword/', forgotPassword.as_view(), name="forgotpassword"),




]
