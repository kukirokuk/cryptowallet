#!/usr/bin/env python3
from hdwallet import HDWallet
from hdwallet.utils import generate_entropy
from typing import Optional
from hdwallet import HDWallet

class WalletManager:
    
    def __init__(self, cryptocurrency):
      self.cryptocurrency = cryptocurrency
    
    def create_wallet(self):

        # Choose strength 128, 160, 192, 224, or 256
        STRENGTH: int = 160  # Default is 128

        # Choose language: english, french, italian, spanish, chinese_simplified, chinese_traditional, japanese, or korean
        LANGUAGE: str = "english"

        # Generate new entropy hex string
        ENTROPY: str = generate_entropy(strength=STRENGTH)

        # Secret passphrase for mnemonic
        PASSPHRASE: Optional[str] = "None"

        # Initialize Bitcoin mainnet HDWallet
        hdwallet: HDWallet = HDWallet(symbol=self.cryptocurrency, use_default_path=False)

        # Get Bitcoin HDWallet from entropy
        hdwallet.from_entropy(entropy=ENTROPY, language=LANGUAGE, passphrase=PASSPHRASE)

        # Derivation from path
        # hdwallet.from_path("m/44'/0'/0'/0/0")

        # Or derivation from index
        hdwallet.from_index(44, hardened=True)
        hdwallet.from_index(0, hardened=True)
        hdwallet.from_index(0, hardened=True)
        hdwallet.from_index(0)
        hdwallet.from_index(0)

        wallet_data = hdwallet.dumps()
        return wallet_data
