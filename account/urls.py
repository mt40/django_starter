from django.urls import path

from . import views

app_name = "account"  # pylint: disable=invalid-name

urlpatterns = [
    # post views
    path("login/", views.user_login, name="login"),
]
