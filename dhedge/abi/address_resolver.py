address_resolver_abi = [
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_owner",
				"type": "address"
			}
		],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "constructor",
		"signature": "constructor"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": False,
				"internalType": "address",
				"name": "oldOwner",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "OwnerChanged",
		"type": "event",
		"signature": "0xb532073b38c83145e3e5135377a08bf9aab55bc0fd7c1179cd4fb995d2a5159c"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": False,
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "OwnerNominated",
		"type": "event",
		"signature": "0x906a1c6bd7e3091ea86693dd029a831c19049ce77f1dce2ce0bab1cacbabce22"
	},
	{
		"constant": False,
		"inputs": [],
		"name": "acceptOwnership",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function",
		"signature": "0x79ba5097"
	},
	{
		"constant": True,
		"inputs": [
			{
				"internalType": "bytes32",
				"name": "name",
				"type": "bytes32"
			}
		],
		"name": "getAddress",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function",
		"signature": "0x21f8a721"
	},
	{
		"constant": True,
		"inputs": [
			{
				"internalType": "bytes32",
				"name": "key",
				"type": "bytes32"
			}
		],
		"name": "getSynth",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function",
		"signature": "0x51456061"
	},
	{
		"constant": False,
		"inputs": [
			{
				"internalType": "bytes32[]",
				"name": "names",
				"type": "bytes32[]"
			},
			{
				"internalType": "address[]",
				"name": "destinations",
				"type": "address[]"
			}
		],
		"name": "importAddresses",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function",
		"signature": "0xab0b8f77"
	},
	{
		"constant": False,
		"inputs": [
			{
				"internalType": "address",
				"name": "_owner",
				"type": "address"
			}
		],
		"name": "nominateNewOwner",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function",
		"signature": "0x1627540c"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "nominatedOwner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function",
		"signature": "0x53a47bb7"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function",
		"signature": "0x8da5cb5b"
	},
	{
		"constant": True,
		"inputs": [
			{
				"internalType": "bytes32",
				"name": "",
				"type": "bytes32"
			}
		],
		"name": "repository",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function",
		"signature": "0x187f7935"
	},
	{
		"constant": True,
		"inputs": [
			{
				"internalType": "bytes32",
				"name": "name",
				"type": "bytes32"
			},
			{
				"internalType": "string",
				"name": "reason",
				"type": "string"
			}
		],
		"name": "requireAndGetAddress",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function",
		"signature": "0xdacb2d01"
	}
]
