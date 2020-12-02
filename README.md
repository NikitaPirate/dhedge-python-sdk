# dhedge-python-sdk


## Installation
install [eth-brownie](https://github.com/eth-brownie/brownie)
```bash
$ git clone https://github.com/NikitaPirate/dhedge-python-sdk.git
$ cd dhedge-python-sdk
$ python3 setup.py install
```
or
```bash
$ pip install dhedge-python-sdk
```


## Network

```bash
$ brownie networks modify <id> host=<your host>
```
or just add Infura ID to environment
```bash
$ export WEB3_INFURA_PROJECT_ID=YourProjectID
```

## Account
Adding account in script:
```python
from brownie import accounts
account = accounts.add(<private key>)
```
or
```python
account = accounts.from_mnemonic(<mnemonic>)
```

or add account in brownie:
use to explore all options:
```bash
$ brownie accounts -help
```
after adding account:
```python
from brownie import accounts
account = accounts.load(<account_id>)
```

## Usage

```bash
$ brownie run script --network <network id>
```