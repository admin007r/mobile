from django.db import models

# Create your models here.
class Bee(models.Model):
    titel = models.CharField(max_length=28)
    call_p = models.CharField(max_length=28)
    sms = models.CharField(max_length=28)
    mb = models.CharField(max_length=28)
    dec = models.CharField(max_length=28, null=True, blank=True)
    discount = models.CharField(max_length=28)
    realPrice  = models.CharField(max_length=28)


    def __str__(self):
        return self.titel
class Ucell(models.Model):
    titel = models.CharField(max_length=28)
    call_p = models.CharField(max_length=28)
    sms = models.CharField(max_length=28, null=True, blank=True)
    mb = models.CharField(max_length=28)
    dec = models.CharField(max_length=28,null=True, blank=True)
    discount = models.CharField(max_length=28)
    realPrice  = models.CharField(max_length=28)

    def __str__(self):
        return self.titel
class Mobi(models.Model):
    titel = models.CharField(max_length=28)
    call_p = models.CharField(max_length=28)
    sms = models.CharField(max_length=28)
    mb = models.CharField(max_length=28)
    dec = models.CharField(max_length=28,null=True,blank=True)
    discount = models.CharField(max_length=28)
    realPrice  = models.CharField(max_length=28)


    def __str__(self):
        return self.titel