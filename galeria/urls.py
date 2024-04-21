from django.urls import path, include

from galeria.views import index, imagem, buscar

urlpatterns = [
    path("", index, name="index"),
    path("imagem/<int:foto_id>", imagem, name="imagem"),
    path("buscar", buscar, name="buscar"),
    path("accounts/", include("django.contrib.auth.urls")),
]
