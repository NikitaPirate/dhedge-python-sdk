from brownie import Contract
from brownie.convert import EthAddress
from dhedge.abi.token import token_abi
import json


class Token:

    def __init__(self, address, signer):
        self.contract = Contract.from_abi('Token', address, token_abi)
        # self.contract = interface.token(address)
        self.address = address
        self.fromSigner = {'from': signer}

    def getAddress(self):
        return self.address

    # Read

    def totalSupply(self):
        return self.contract.totalSupply()

    def balanceOf(self, address):
        address = EthAddress(address)  # Raise error if not valid eth address
        return self.contract.balanceOf(address)

    def allowance(self, owner, spender):
        owner, spender = EthAddress(owner), EthAddress(spender)
        return self.contract.allowance(owner, spender)

    # Write

    def transfer(self, recipient, amount):
        recipient = EthAddress(recipient)
        return self.contract.transfer(recipient, amount, self.fromSigner)

    def approve(self, spender, amount):
        spender = EthAddress(spender)
        return self.contract.approve(spender, amount, self.fromSigner)

    def transferFrom(self, sender, recipient, amount):
        sender, recipient = EthAddress(sender), EthAddress(recipient)
        return self.contract.transferFrom(sender, recipient, amount, self.fromSigner)
