from rest_framework import serializers
from .models import Address, Wallet


CRYPTO_CHOICES = ["BTC", "ETH"]


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

class WalletSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Wallet
        fields = "__all__"

    def create(self, validated_data):
        address_data = validated_data.pop("address")
        address = Address.objects.create(**address_data)
        wallet = Wallet.objects.create(address=address, **validated_data)
        return wallet
