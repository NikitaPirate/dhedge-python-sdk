from brownie import Contract
from dhedge.pool import Pool
from dhedge.exchange_rates import ExchangeRates
from dhedge.utills import strTo32HexString
from dhedge.abi.factory import factory_abi
from dhedge.abi.address_resolver import address_resolver_abi


class Factory:

    def __init__(self, signer_private_key, factoryAddress):

        self.signer = signer_private_key
        self.fromSigner = {'from': self.signer}

        self.factory = Contract.from_abi('Factory', factoryAddress, factory_abi)
        self.address = factoryAddress

    def getAddressResolver(self):
        return self.factory.addressResolver()

    def getExchangeRates(self):
        resolverAddress = self.getAddressResolver()

        resolver = Contract.from_abi('Address resolver', resolverAddress, address_resolver_abi)
        exchangeRatesAddress = resolver.getAddress(strTo32HexString('ExchangeRates'))
        return ExchangeRates(self.signer, exchangeRatesAddress)

    # Read

    def getAddress(self):
        return self.address

    def loadPool(self, address):
        pool = Pool(self.signer, address)
        return pool

    def isPool(self, address):
        return self.factory.isPool(address)

    def validatePool(self, address):
        isPool = self.factory.isPool(address)
        if not isPool:
            raise Exception('Given address not a pool')

    def getPoolCount(self):
        return self.factory.deployedFundsLength()

    def getDaoAddress(self):
        return self.factory.getDaoAddress()

    def getManagerFee(self, address):
        self.validatePool(address)
        result = self.factory.getPoolManagerFee(address)
        return result[0] / result[1]

    def getMaximumManagerFee(self):
        result = self.factory.getMaximumManagerFee()
        return result[0] / result[1]

    def getExitFee(self):
        result = self.factory.getExitFee()
        return result[0] / result[1]

    def getDaoFee(self):
        result = self.factory.getDaoFee()
        return result[0] / result[1]

    def getExitFeeCooldown(self):
        return self.factory.getExitFeeCooldown()

    def getMaximumAssetCount(self):
        return self.factory.getMaximumSupportedAssetCount()

    # Write

    def createPool(self,
                   privatePool,
                   managerName,
                   poolName,
                   assets=["sETH"],
                   managerFeeNumerator=100,
                   ):

        for i in range(len(assets)):
            assets[i] = strTo32HexString(assets[i])

        createPoolTx = self.factory.createFund(
            privatePool,
            self.signer,
            managerName,
            poolName,
            managerFeeNumerator,
            assets,
            self.fromSigner)

        creationEvent = createPoolTx.events['FundCreated']

        if not creationEvent:
            raise Exception('Fund not created')

        poolAddress = creationEvent['fundAddress']

        pool = Pool(self.signer, poolAddress)
        return pool




