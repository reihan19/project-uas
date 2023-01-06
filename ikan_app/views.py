from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.core import serializers
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def Pagelogin(request):
    if request.user.is_authenticated:
        return redirect ("/peta/")
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            pass1=request.POST.get('pass')
            user=authenticate(request, username=username, password=pass1)
            if user is not None:
                login(request, user)
                return redirect('/peta/')
            
        return render(request, "login.html")

def Pageregis(request):
    if request.user.is_authenticated:
        return redirect ("/peta/")
    else:
        if request.method=='POST':
            uname=request.POST.get('username')
            email=request.POST.get('email')
            pass1=request.POST.get('password1')
            pass2=request.POST.get('password2')
            my_user=User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('/login/')

        return render(request, "regis.html")

def Pagelogout(request):
    logout(request)
    return redirect('/login/')

@login_required(login_url='login')
def peta(request):
      lelang = pelelangan.objects.all()
      marker_json = serializers.serialize('json', lelang)
      data = {
          "Judul"   : "Ujian Akhir Semester",
          'lelang' : lelang,
          'marker_json' : marker_json,
      }
      return render(request, "peta.html", data)

@login_required(login_url='login')
def tambah_peta(request):
      if request.POST:
          form = FormPelelangan(request.POST)
          if form.is_valid():
              form.save()
              form = FormPelelangan()
              lelang = pelelangan.objects.all()
              data = {
                  "Judul"   : "Ujian Akhir Semester",
                 'Title' : "Input Data Baru",
                 'lelang' : lelang,
                 'form'    : form,
                 'pesan'   : "Data berhasil ditambahkan"
              }
              return render(request, "tambah_peta.html", data)
      else:
          form  = FormPelelangan()
          lelang = pelelangan.objects.all()
          data = {
             "Judul"   : "Ujian Akhir Semester",
             'Title'   : "Input Data Baru",
             'lelang' : lelang,
             'form'    : form,
          }
          return render(request, "tambah_peta.html", data)

@login_required(login_url='login')
def ubah_peta(request, id):
      lelang = pelelangan.objects.get(pk=id)
      if request.POST:
          form = FormPelelangan(request.POST, instance=lelang)
          if form.is_valid():
              form.save()
              data = {
                  "Judul"   : "Ujian Akhir Semester",
                  'Title' : "Ubah Data",
                  'lelang' : lelang,
                  'form'  : form,
                  'pesan' : "Data berhasil diubah"
              }
              return render(request, "ubah_peta.html", data)
      else:
          form = FormPelelangan(instance=lelang)
          data = {
          "Judul"   : "Ujian Akhir Semester",
          'Title' : "Ubah Data",
          'lelang' : lelang,
          'form'  : form,
           }
      return render(request, "ubah_peta.html", data)

def hapus_peta(request, id):
    lelang = pelelangan.objects.get(pk=id)
    lelang.delete()
    
    return redirect("/peta/")

@login_required(login_url='login')
def ikan(request):
      jenis = Ikan.objects.all()
      data = {
          "Judul"   : "Ujian Akhir Semester",
          'jenis' : jenis,
      }
      return render(request, "ikan.html", data)

@login_required(login_url='login')
def tambah_ikan(request):
      if request.POST:
          form = FormIkan(request.POST, request.FILES)
          if form.is_valid():
              form.save()
              form = FormIkan()
              jenis = Ikan.objects.all()
              data = {
                  "Judul"   : "Ujian Akhir Semester",
                 'Title' : "Input Data Baru",
                 'jenis' : jenis,
                 'form'    : form,
                 'pesan'   : "Data berhasil ditambahkan"
              }
              return render(request, "tambah_ikan.html", data)
      else:
          form  = FormIkan()
          jenis = Ikan.objects.all()
          data = {
             "Judul"   : "Ujian Akhir Semester",
             'Title'   : "Input Data Baru",
             'jenis' : jenis,
             'form'    : form,
          }
          return render(request, "tambah_ikan.html", data)

@login_required(login_url='login')
def ubah_ikan(request, id):
      jenis = Ikan.objects.get(pk=id)
      if request.POST:
          form = FormIkan(request.POST, request.FILES, instance=jenis)
          if form.is_valid():
              form.save()
              data = {
                  "Judul"   : "Ujian Akhir Semester",
                  'Title' : "Ubah Data",
                  'jenis' : jenis,
                  'form'  : form,
                  'pesan' : "Data berhasil diubah"
              }
              return render(request, "ubah_ikan.html", data)
      else:
          form = FormIkan(instance=jenis)
          data = {
          "Judul"   : "Ujian Akhir Semester",
          'Title' : "Ubah Data",
          'jenis' : jenis,
          'form'  : form,
           }
      return render(request, "ubah_ikan.html", data)

def hapus_ikan(request, id):
    jenis = Ikan.objects.get(pk=id)
    jenis.delete()
    
    return redirect("/ikan/")