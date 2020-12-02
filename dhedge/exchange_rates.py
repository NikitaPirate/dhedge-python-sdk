from brownie import Contract
from dhedge.utills import strTo32HexString
from dhedge.abi.exchange_rates import exchange_rates_abi


class ExchangeRates:

    def __init__(self, signer, exchangeRatesAddress):
        self.signer = signer

        self.contract = Contract.from_abi('Exchange rates', exchangeRatesAddress, exchange_rates_abi)
        self.address = exchangeRatesAddress

    def rateForCurrency(self, key):
        key = strTo32HexString(key)
        return self.contract.rateForCurrency(key)

    def getEffectiveValue(self, source, amount, destination):
        source = strTo32HexString(source)
        destination = strTo32HexString(destination)
        return self.contract.effectiveValue(source, amount, destination)