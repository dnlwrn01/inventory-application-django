
from django.conf.urls import url, include
from django.urls.conf import path
from .views import home, register, list_users, view_user, edit_user, del_user
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", home, name="home"),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^register/", register, name="register"),
    path("inventory/", include("products.urls")),
    path("users/", list_users, name="list_users"),
    path("users/<int:pk>/", view_user, name="view_user"),
    path("users/<int:pk>/edit", edit_user, name="edit_user"),
    path("users/<int:pk>/delete", del_user, name="del_user"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
