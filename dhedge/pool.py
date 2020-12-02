from brownie import Contract
from dhedge.utills import strTo32HexString, parseBytes32String, toEther
from dhedge.token import Token
from dhedge.abi.pool import pool_abi
from dhedge.abi.token import token_abi


class Pool:

    def __init__(self, signer, poolAddress):
        self.signer = signer
        self.fromSigner = {'from': self.signer}

        self.contract = Contract.from_abi('Pool', poolAddress, pool_abi)

        self.token = Contract.from_abi('Token', poolAddress, token_abi)

        self.address = poolAddress

    def getToken(self):
        return Token(self.address, self.signer)

    def getAddress(self):
        return self.address

    # Read - Managed

    def getManager(self):
        return self.contract.manager()

    def getManagerName(self):
        return self.contract.managerName()

    def isMember(self, address):
        return self.contract.isMemberAllowed(address)

    def getMembers(self):
        return self.contract.getMembers()

    def getMemberCount(self):
        return self.contract.numberOfMembers()

    # Write - Managed

    def changeManager(self, address, name):
        receipt = self.contract.changeManager(address, name, self.fromSigner)
        receipt = receipt.wait(1)
        changeEvent = receipt.events['ManagerUpdated']
        if not changeEvent:
            raise Exception('FManager not updated')

    def addMembers(self, members):
        return self.contract.addMembers(members, self.fromSigner)

    def removeMembers(self, members):
        return self.contract.removeMembers(members, self.fromSigner)

    def addMember(self, member):
        self.addMembers([member])

    def removeMember(self, member):
        self.removeMembers([member])

    # Read - Pool

    def isPrivate(self):
        return self.contract.privatePool()

    def getCreator(self):
        return self.contract.creator()

    def getCreationTime(self):
        return self.contract.creationTime()

    def getFactory(self):
        return self.contract.factory()

    def getAssets(self):
        return [parseBytes32String(item) for item in self.contract.getSupportedAssets()]

    def getTokenPriceAtLastFeeMint(self):
        return self.contract.tokenPriceAtLastFeeMint()

    def getLastDepositByAddress(self, address):
        return self.contract.lastDeposit(address)

    def getManagerFee(self):
        result = self.contract.getManagerFee()
        return result[0] / result[1]

    def getExitFee(self):
        result = self.contract.getExitFee()
        return result[0] / result[1]

    def getAssetCount(self):
        return self.contract.numberOfSupportedAssets()

    def isAssetSupported(self, key, convert=False):
        if convert:
            key = strTo32HexString(key)
        return self.contract.isAssetSupported(key)

    def getAsset(self, key):
        key = strTo32HexString(key)
        proxy = self.contract.getAssetProxy(key)
        token = Token(proxy, self.signer)
        return token

    def getPoolValue(self):
        return self.contract.totalFundValue()

    def assetValue(self, key):
        key = strTo32HexString(key)
        if not self.isAssetSupported(key):
            raise Exception('Asset not supported')
        return self.contract.assetValue(key)

    def getSummary(self):
        summary = self.contract.getFundSummary()
        return {
            'name': summary[0],
            'totalSupply': summary[1],
            'totalPoolValue': summary[2],
            'managerAddress': summary[3],
            'managerName': summary[4],
            'creationTime': summary[5],
            'private': summary[6],
            'managerFee': summary[7] / summary[8],
            'exitFee': summary[9] / summary[10],
        }

    def getComposition(self):
        result = self.contract.getFundComposition()
        composition = {}
        for i in range(len(result[0])):
            assetName = parseBytes32String(result[0][i])
            assetBalance = toEther(result[1][i])
            assetRate = toEther(result[2][i])
            composition[assetName] = {'balance': assetBalance, 'rate': assetRate}
        return composition

    def getWaitingPeriods(self):
        result = self.contract.getWaitingPeriods()
        periods = {}
        for i in range(len(result[0])):
            periods[parseBytes32String(result[0][i])] = result[1][i]
        return periods

    def getSuspendedAssets(self):
        result = self.contract.getSuspendedAssets()
        assets = {}
        for i in range(len(result[0])):
            assets[parseBytes32String(result[0][i])] = result[1][i]
        return assets

    # Pool - Write

    def addAsset(self, key):
        key = strTo32HexString(key)
        if self.isAssetSupported(key):
            raise Exception('Asset already supported')
        return self.contract.addToSupportedAssets(key, self.fromSigner)

    def removeAsset(self, key):
        key = strTo32HexString(key)
        if not self.isAssetSupported(key):
            raise Exception('Asset not supported')
        return self.contract.removeFromSupportedAssets(key, self.fromSigner)

    def deposit(self, amount):
        return self.contract.deposit(amount, self.fromSigner)

    def withdraw(self, amount, forfeit=False):
        if forfeit:
            tx = self.contract.forfeitSuspendedSynthsAndWithdraw(amount, self.fromSigner)
        else:
            tx = self.contract.withdraw(amount, self.fromSigner)
        return tx

    def exchange(self, sourceKey, sourceAmount, destinationKey):
        sourceKey = strTo32HexString(sourceKey)
        destinationKey = strTo32HexString(destinationKey)

        if not self.isAssetSupported(sourceKey):
            raise Exception('Source asset not supported')

        if not self.isAssetSupported(destinationKey):
            raise Exception('Destination asset not supported')

        return self.contract.exchange(sourceKey, sourceAmount, destinationKey, self.fromSigner)
