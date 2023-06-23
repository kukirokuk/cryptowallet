from rest_framework import serializers
from .models import Address, Wallet


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["address",]

class WalletSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True)

    class Meta:
        model = Wallet
        fields = "__all__"

    def create(self, validated_data):
        address_data = validated_data.pop("addresses")
        wallet = Wallet.objects.create(**validated_data)
        Address.objects.create(wallet=wallet, **address_data[0])
        return wallet
