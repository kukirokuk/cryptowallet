import copy

from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from crypto_addresses.models import Address, Wallet
from crypto_addresses.serializers import AddressSerializer, WalletSerializer
from bitcoinlib.keys import deserialize_address


class AddressAPITestCase(APITestCase):
    def setUp(self):
        self.address_data = {"address": "address_string"}
        self.wallet_data = {
            "cryptocurrency": "BTC",
            "xprivate_key": "encrypted_xprivate_key",
            "xpublic_key": "encrypted_xpublic_key",
            "private_key": "encrypted_private_key",
            "public_key": "encrypted_public_key",
            "wif": "encrypted_wif",
            "finger_print": "encrypted_fingerprint",
            "semantic": "encrypted_semantic",
            "path": "encrypted_path",
            "hash_data": "encrypted_hash_data",
        }

    def validate_bitcoin_address(self, address):
        try:
            deserialize_address(address)
            return True
        except:
            return False

    def test_create_address(self):
        url = reverse("address-list")
        response = self.client.post(url, data={"cryptocurrency": self.wallet_data["cryptocurrency"]}, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue("address" in response.data)

        address = response.data["address"]

        address_obj = Address.objects.first()
        self.assertEqual(address_obj.address, address)

        wallet = Wallet.objects.first()
        self.assertEqual(wallet.addresses.count(), 1)
        self.assertEqual(wallet.addresses.first(), address_obj)

        result = self.validate_bitcoin_address(address)
        self.assertTrue(result)

    def test_create_address_invalid_cryptocurrency(self):
        url = reverse("address-list")
        response = self.client.post(url, data={"cryptocurrency": "INVALID"}, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_addresses(self):
        wallet = Wallet.objects.create(**self.wallet_data)
        Address.objects.create(wallet=wallet, **self.address_data)
        url = reverse("address-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        serializer = AddressSerializer(self.address_data)
        self.assertIn(serializer.data, response.data)

    def test_wallet_serializer(self):
        wallet_data = copy.deepcopy(self.wallet_data)
        wallet_data["addresses"] = [self.address_data]
        serializer = WalletSerializer(data=wallet_data)
        self.assertTrue(serializer.is_valid(raise_exception=True))
        wallet = serializer.save()

        self.assertEqual(Wallet.objects.count(), 1)
        self.assertEqual(wallet.cryptocurrency, self.wallet_data["cryptocurrency"])
        self.assertEqual(wallet.xprivate_key, self.wallet_data["xprivate_key"])
        self.assertEqual(wallet.xpublic_key, self.wallet_data["xpublic_key"])


