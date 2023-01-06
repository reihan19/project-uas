from django.db import models

# Create your models here.

class pelelangan(models.Model):
     nama      = models.CharField(max_length=75)
     lintang = models.FloatField(null=True)
     bujur = models.FloatField(null=True)

     def __str__(self):
         return self.nama

class Ikan(models.Model):
     nama_Ikan  = models.CharField(max_length=75)
     harga     = models.CharField(max_length=50)
     gambar   = models.ImageField(null=True, blank=True, upload_to="images/")
     
     def __str__(self):
         return self.nama_Ikan