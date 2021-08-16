
from django.conf.urls import url, include
from django.urls.conf import path
from .views import list_items, view_item, edit_item, del_item
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", list_items, name="list_items"),
    path("<int:pk>/", view_item, name="view_item"),
    path("<int:pk>/edit", edit_item, name="edit_item"),
    path("<int:pk>/delete", del_item, name="del_item"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
