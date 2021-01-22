from django.urls import path

from .views import *

urlpatterns = [
    path("upload_ml1/", image_upload_view, name="ml1app")
]
