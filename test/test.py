from dhedge import Factory
from brownie import accounts, network, Wei


def main():
    privateKey = 'private key'
    factoryAddr = '0x44226Fc17074A4F019FAA6412E85eff3e01b8368'  # factory addr on kovan
    poolAddr = 'pool addr'
    acc = accounts.add(privateKey)
    network.gas_limit(10000000)         # Not work without it on kovan
    network.gas_price(Wei('1 gwei'))    # Not work without it on kovan

    factory = Factory(acc, factoryAddr)
    pool = factory.loadPool(poolAddr)

    print('Pool Address', pool.getAddress())
    print('isPool', pool.getAddress(), factory.isPool(pool.getAddress()))
    print('isPool', '0xb12DC0644f505028388Da4A919eD72d422175dA8',
          factory.isPool('0xb12DC0644f505028388Da4A919eD72d422175dA8'))
    print('Pool manager fee', factory.getManagerFee(pool.getAddress()))
    print('Dao fee', factory.getDaoFee())
    print('Dao address', factory.getDaoAddress())
    print('Exit fee', factory.getExitFee())
    print('Maximum manager fee', factory.getMaximumManagerFee())
    print('Exit fee cooldown', factory.getExitFeeCooldown())
    print('Max assets', factory.getMaximumAssetCount())
    print('Total pools', factory.getPoolCount())

    # Pool test
    print('Is pool private', pool.isPrivate())
    print('Creator', pool.getCreator())
    print('Creation time', pool.getCreationTime())
    print('Factory address', pool.getFactory())
    print('Assets', pool.getAssets())
    print('Token price at last fee mint', pool.getTokenPriceAtLastFeeMint())
    print('Manager', pool.getManager())
    print('Manager name', pool.getManagerName())
    print('Pool members', pool.getMembers())
    print('Pool member count', pool.getMemberCount())

    sUSD = pool.getAsset('sUSD')
    balance = sUSD.balanceOf(factory.signer)
    print('sUSD balance', balance)

    sUSD.contract.approve(pool.getAddress(), '1000000000000000000', {'from': acc})
    pool.deposit('1000000000000000000')
    print('Pool Value', pool.getPoolValue())

    pool.exchange('sUSD', '500000000000000000', 'sETH')

    print('Pool Value', pool.getPoolValue())
    print('sUSD value', pool.assetValue('sUSD'))
    print('sETH value', pool.assetValue('sETH'))

    print('Summary', pool.getSummary())
    print('Composition', pool.getComposition())
    print('Waiting periods', pool.getWaitingPeriods())
    print('Suspended assets', pool.getSuspendedAssets())