from django.db import models
from django_cryptography.fields import encrypt

    
class Wallet(models.Model):
    cryptocurrency = models.CharField(max_length=3)
    xprivate_key = encrypt(models.CharField(max_length=200, default=None))
    xpublic_key = encrypt(models.CharField(max_length=200, default=None))
    private_key = encrypt(models.CharField(max_length=200, default=None))
    public_key = encrypt(models.CharField(max_length=200, default=None))
    wif = encrypt(models.CharField(max_length=200, default=None))
    finger_print = encrypt(models.CharField(max_length=200, default=None))
    semantic = encrypt(models.CharField(max_length=200, default=None))
    path = encrypt(models.CharField(max_length=200, default=None))
    hash_data = encrypt(models.CharField(max_length=200, default=None))

    
class Address(models.Model):
    address = models.CharField(max_length=80)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name="addresses")
    