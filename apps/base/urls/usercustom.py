# Django Library
from django.urls import path, include,re_path

# Thirty Library
from rest_auth.registration.views import VerifyEmailView
from allauth.account import views

#app_name = "PyUser"

# Localfolder Library

urlpatterns = [
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(), name='account_confirm_email'),
    re_path(r'^account-confirm-email/$', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    path("login/", views.login, name="account_login"),
    path("signup/", views.signup, name="account_signup"),
    path("logout/", views.logout, name="account_logout"),
    path("password/change/",views.password_change,name="account_change_password",),
    path("password/set/", views.password_set, name="account_set_password"),
    path("inactive/", views.account_inactive, name="account_inactive"),
    # E-mail
    path("email/", views.email, name="account_email"),
    path("confirm-email/",views.email_verification_sent,name="account_email_verification_sent",),
    re_path(r"^confirm-email/(?P<key>[-:\w]+)/$",views.confirm_email,name="account_confirm_email",),
    # password reset
    path("password/reset/", views.password_reset, name="account_reset_password"),
    path("password/reset/done/",views.password_reset_done,name="account_reset_password_done",),
    re_path(r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",views.password_reset_from_key,name="account_reset_password_from_key",),
    path("password/reset/key/done/",views.password_reset_from_key_done,name="account_reset_password_from_key_done",),
]
