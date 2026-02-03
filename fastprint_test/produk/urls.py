from django.urls import path
from .views import produk_list, produk_tambah, produk_edit, produk_hapus

urlpatterns = [
    path("", produk_list, name="produk_list"),
    path("produk/tambah/", produk_tambah, name="produk_tambah"),
    path("produk/edit/<int:pk>/", produk_edit, name="produk_edit"),
    path("produk/hapus/<int:pk>/", produk_hapus, name="produk_hapus"),
]
