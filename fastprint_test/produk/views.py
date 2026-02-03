from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Produk
from .forms import ProdukForm

def produk_list(request):
    produk = Produk.objects.select_related(
        'kategori', 'status'
    ).filter(status__nama_status='bisa dijual')

    form = ProdukForm()

    context = {
        'produk': produk,
        'form': form
    }
    return render(request, 'produk/list.html', context)

def produk_tambah(request):
    produk = Produk.objects.select_related(
        'kategori', 'status'
    ).filter(status__nama_status='bisa dijual')
    
    if request.method == 'POST':
        form = ProdukForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produk berhasil ditambahkan')
            return redirect('produk_list')
        else:
            messages.error(request, 'Gagal menambahkan produk')
    else:
        form = ProdukForm()

    context = {
        'produk': produk,
        'form': form,
        'openTambah': True
    }
    return render(request, 'produk/list.html', context)

def produk_edit(request, pk):
    produk = get_object_or_404(Produk, id=pk)

    if request.method == 'POST':
        form = ProdukForm(request.POST, instance=produk)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produk berhasil diperbarui')
        else:
            messages.error(request, 'Gagal memperbarui produk')

    return redirect('produk_list')

def produk_hapus(request, pk):
    produk = get_object_or_404(Produk, id=pk)
    produk.delete()
    messages.success(request, 'Produk berhasil dihapus')
    return redirect('produk_list')
