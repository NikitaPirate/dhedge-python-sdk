from dhedge import Factory
from brownie import accounts, network, Wei
from click import secho


def main():
    privateKey = 'private key'
    factoryAddr = '0x44226Fc17074A4F019FAA6412E85eff3e01b8368'  # factory addr on kovan

    acc = accounts.add(privateKey)

    factory = Factory(acc, factoryAddr)

    network.gas_limit(10000000)         # Not work without it on kovan
    network.gas_price(Wei('1 gwei'))    # Not work without it on kovan

    privatePool = False
    managerName = 'Test'
    poolName = 'Test'
    assets = ['sETH', 'sBTC']

    managerFeeNumerator = 100
    secho('create pool...', fg="green")

    pool = factory.createPool(
        privatePool,
        managerName,
        poolName,
        assets,
        managerFeeNumerator
    )
    secho(f'pool {pool.address} created', fg="green")

    comp = pool.getComposition()
    secho(f'composition: {comp}', fg="yellow")

    sUSD = pool.getAsset('sUSD')
    secho('approve sUSD...', fg="green")
    tx = sUSD.contract.approve(pool.address, Wei('100000000000000 ether'), {'from': acc})
    tx.wait(1)

    secho('deposit sUSD...', fg="green")
    tx = pool.deposit(Wei('5 ether'))
    tx.wait(1)

    secho('exchange synths...', fg="green")
    tx = pool.exchange('sUSD', Wei('5 ether'), 'sETH')
    tx.wait(1)

    comp = pool.getComposition()
    secho(f'composition: {comp}', fg="yellow")
