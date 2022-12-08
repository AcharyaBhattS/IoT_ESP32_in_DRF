from django.db import models

# Create your models here.
class sbdb(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=50)
    address = models.TextField(max_length=255)    
    class Meta:
        db_table = "SB_Table"


class esp32_db(models.Model):
    led1 = models.IntegerField(max_length=50)
    temp1 = models.TextField(max_length=100)    
    class Meta:
        db_table = "Table_ESP32"


class Upld_sbdb(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    fileName = models.CharField(max_length=550)
    class Meta:
        db_table = "Upload_Table"