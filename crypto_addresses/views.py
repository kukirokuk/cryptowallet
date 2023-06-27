from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .serializers import AddressSerializer, WalletSerializer
from .wallet_manager import WalletManager
from .models import Address

CRYPTO_CHOICES = ["BTC", "ETH"]


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def create(self, request, *args, **kwargs):
        cryptocurrency = request.data.get("cryptocurrency")
        wallet_data = self.generate_wallet_data(cryptocurrency)
        serializer = WalletSerializer(data=wallet_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data["addresses"][0], status=status.HTTP_201_CREATED)


    def generate_wallet_data(self, cryptocurrency):
        if cryptocurrency in CRYPTO_CHOICES:
            wallet_manager = WalletManager(cryptocurrency=cryptocurrency)
            data = wallet_manager.create_wallet()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        wallet_data = self.parse_data(cryptocurrency, data)
        return wallet_data

    def parse_data(self, cryptocurrency, data):
        address_data = [{"address": data["addresses"]["p2pkh"]}]
        wallet_data = {"cryptocurrency": cryptocurrency,
                       "xprivate_key": data["xprivate_key"],
                       "xpublic_key": data["xprivate_key"],
                       "private_key": data["private_key"],
                       "public_key": data["public_key"],
                       "xprivate_key": data["xprivate_key"],
                       "wif": data["wif"],
                       "finger_print": data["finger_print"],
                       "semantic": data["semantic"],
                       "path": data["path"],
                       "hash_data": data["hash"],
                       "addresses": address_data}
                       
        return wallet_data

