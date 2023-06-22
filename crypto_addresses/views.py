from rest_framework.viewsets import ModelViewSet
from .serializers import AddressSerializer, WalletSerializer
from .wallet_manager import WalletManager
from .models import Address
from rest_framework.response import Response
from rest_framework import status


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def create(self, request, *args, **kwargs):
        cryptocurrency = request.data.get("cryptocurrency")
        wallet_data = self.generate_wallet_data(cryptocurrency)
        serializer = WalletSerializer(data=wallet_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data["address"]["address"], status=status.HTTP_201_CREATED)


    def generate_wallet_data(self, cryptocurrency):
        wallet_manager = WalletManager(cryptocurrency=cryptocurrency)
        if cryptocurrency == "BTC":
            data = wallet_manager.create_bitcoin_wallet()
        elif cryptocurrency == "ETH":
            data = wallet_manager.create_etherum_wallet()
        else:
            raise ValueError("Unsupported cryptocurrency")
        address_data = { "address": data["addresses"]["p2pkh"]}
        wallet_data = {"cryptocurrency": cryptocurrency,
                       "address": address_data}
        return wallet_data

