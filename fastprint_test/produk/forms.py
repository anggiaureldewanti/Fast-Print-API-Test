from django import forms
from .models import Produk

class ProdukForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = ["id_produk", "nama_produk", "harga", "kategori", "status"]
        widgets = {
            "id_produk": forms.NumberInput(
                attrs={
                    "class": "w-full border border-gray-300 rounded-md px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500",
                }
            ),
            "nama_produk": forms.TextInput(
                attrs={
                    "class": "w-full border border-gray-300 rounded-md px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500",
                }
            ),
            "harga": forms.NumberInput(
                attrs={
                    "class": "w-full border border-gray-300 rounded-md px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500",
                }
            ),
            "kategori": forms.Select(
                attrs={
                    "class": "w-full border border-gray-300 rounded-md px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500",
                }
            ),
            "status": forms.Select(
                attrs={
                    "class": "w-full border border-gray-300 rounded-md px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500",
                }
            ),
        }

    def clean_nama_produk(self):
        nama = self.cleaned_data.get("nama_produk")
        if not nama:
            raise forms.ValidationError("Nama produk wajib diisi")
        return nama

    def clean_harga(self):
        harga = self.cleaned_data.get("harga")
        if harga <= 0:
            raise forms.ValidationError("Harga harus berupa angka lebih dari 0")
        return harga
