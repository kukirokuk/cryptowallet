from django.db import models

    
class Address(models.Model):
    address = models.CharField(max_length=80)

    def __str__(self):
        return self.address


class Wallet(models.Model):
    cryptocurrency = models.CharField(max_length=3)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="addreses")

    def __str__(self):
        return self.address