[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)

# NO LONGER MAINTAINED

Since the launch of Kaia Blockchain this repository has been parked in favour of the new open-source projects in [Kaia's Github](https://github.com/kaiachain). Contributors have now moved there continuing with massive open-source contributions to our blockchain ecosystem. A big thank you to everyone who has contributed to this repository. For more information about Klaytn's chain merge with Finschia blockchain please refer to the launching of Kaia blockchain - [kaia.io](http://kaia.io/).


# RPC-tester

The tester checks basic operations of Klaytn RPC/WebSocket APIs.

# How to run
## Python Virtualenv
> You can setup the project Environment as separate env from your globally installed python dev environemnt by using virtualenv.

Please check below instructions after installing virtualenv :)
- Create virtualenv for this project by using `$ virtualenv -p python3.6 venv`
- Activate virtualenv by using `source ./venv/bin/activate`
- Install project dependency by using `$ pip install -r requirements.txt`
- Install this repository as module to use relative path `$pip install -e .`

All done :)

## Required
- [1] Faucet Account: An account which has enough amount KLAY for the test.
### For EN (to be tested)
- Options 
  1. --rpc --rpcapi admin,debug,klay,eth,miner,net,personal,rpc,txpool,web3 --rpcport 8551 --rpcaddr 0.0.0.0
  2. --ws --wsapi admin,debug,klay,eth,miner,net,personal,rpc,txpool,web3 --wsport 8552 --wsaddr 0.0.0.0
  3. --sendertxhashindexing
  4. --vmdebug
  5. --txpool.allow-local-anchortx

```shell
--rpc --rpcapi admin,debug,klay,eth,miner,net,personal,rpc,txpool,web3 --rpcport 8551 --rpcaddr 0.0.0.0 --ws --wsapi admin,debug,klay,miner,net,personal,rpc,txpool,web3 --wsport 8552 --wsaddr 0.0.0.0 --sendertxhashindexing --vmdebug
```

- File 
  1. `block.rlp` should be placed at the EN excution path. The content of `block.rlp` is needed to be updated with the return value of `
  debug_getblockrlp` API.
  2. `script/set_CNOnly.sh` - Script to set a private network with 1 CN easily.   

## Usage
### 0. Set config.json and run generate_ws_from_rpc.sh
`config.json` - The information of EN and the faucet account and fee payer account (both account should have enough KLAY).
```json
{
    "endpoint": "localhost",
    "rpcPort": "8551",
    "wsPort": "8552",
    "chainId": "2019",
    "faucetPrivateKey": "752a08fd165dcc7f37f3e444cf485c5b2020e4096a2cfd02f823a8b8280baaab",
    "faucetAddress": "0xf77e71cf745e14129a344bcfb7e28240a5351beb",
    "faucetPassword": "2524",
    "feePayerPrivateKey": "752a08fd165dcc7f37f3e444cf485c5b2020e4096a2cfd02f823a8b8280baaab",
    "feePayerAddress": "0xf77e71cf745e14129a344bcfb7e28240a5351beb",
    "feePayerPassword": "2524",
    "namespaces": "admin,debug,personal,txpool,eth,klay"
}
```

`generate-ws_from_rpc.sh` - The script to change protocol `rpc` to `websocket` used by test script. You need to run this script if you have any updates on `{namespace}/*_rpc.py`
 

### 1. Run all tests
```shell
rpc-tester$ source ./venv/bin/activate
(venv) rpc-tester$ python main.py 
```

### 2. Run specific namespace
Change namespaces field of `config.json` file. If you want to run tests about debug and net namespaces, change the value to `debug,net`.

Others are same with "1. Run all tests".

### 3. Run tests for rpc or websocket
If you want to run tests for specific protocol, you can do like below.
```shell
# Run tests only by rpc
(venv) rpc-tester$ python main.py --protocol rpc
# Run tests only by websocket
(venv) rpc-tester$ python main.py --protocol ws
```

# Project structure overview

```shell
.
├── README.md
├── admin
│   ├── admin_rpc.py
│   └── admin_ws.py
├── block.rlp
├── common # This contains common functions which will be used by many test scripts commonly.
│   ├── klay.py # functions can be used by multiple tests cases with klay namespace
│   ├── net.py # functions can be used by multiple tests cases with net namespace
│   └── personal.py # functions can be used by multiple tests cases with personal namespace
├── config.json # config file used during tests.
├── config_template.json
├── debug # This contains test scripts about `debug` namespace.
│   ├── block.rlp
│   ├── debug_rpc.py
│   └── debug_ws.py
├── errors.py # This contains expected errors occurred during tests. This is shared resource regardless of namespace.
├── eth # This contains test scripts about `eth` namespace.
│   ├── account
│   │   ├── eth_account_rpc.py
│   │   └── eth_account_ws.py
│   ├── block
│   │   ├── eth_block_rpc.py
│   │   └── eth_block_ws.py
│   ├── configuration
│   │   ├── eth_configuration_rpc.py
│   │   └── eth_configuration_ws.py
│   ├── filter
│   │   ├── eth_filter_rpc.py
│   │   └── eth_filter_ws.py
│   ├── gas
│   │   └── eth_gas_rpc.py
│   ├── miscellaneous
│   │   ├── eth_miscellaneous_rpc.py
│   │   └── eth_miscellaneous_ws.py
│   └── transaction
│   │   ├── eth_transaction_rpc.py
│   │   └── eth_transaction_ws.py
├── generate_ws_from_rpc.sh
├── klay # This contains test scripts about `klay` namespace.
│   ├── account
│   │   ├── klay_account_rpc.py
│   │   └── klay_account_ws.py
│   ├── block
│   │   ├── klay_block_rpc.py
│   │   └── klay_block_ws.py
│   ├── configuration
│   │   ├── klay_configuration_rpc.py
│   │   └── klay_configuration_ws.py
│   ├── filter
│   │   ├── klay_filter_rpc.py
│   │   └── klay_filter_ws.py
│   ├── miscellaneous
│   │   ├── klay_miscellaneous_rpc.py
│   │   └── klay_miscellaneous_ws.py
│   └── transaction
│   │   ├── klay_transaction_rpc.py
│   │   └── klay_transaction_ws.py
├── main.py # Run tests by executing main.py
├── net # This contains test scripts about `net` namespace.
│   ├── net_rpc.py
│   └── net_ws.py
├── personal # This contains test scripts about `personal` namespace.
│   ├── personal_rpc.py
│   └── personal_ws.py
├── reports # Contains logs created during each run
├── requirements.txt
├── rpc_tester.egg-info # This is created by executing `pip install -e .`
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   ├── dependency_links.txt
│   └── top_level.txt
├── setup.py 
├── testReport # Contains HTML test reports
├── test_data.py # Contains some constants. This values doesn't need to be initialized.
├── txpool # This contains test scripts about `net` namespace.
│   ├── txpool_rpc.py
│   └── txpool_ws.py
├── utils.py # The Utils class which will be used by many test cases.
├── pre-commit # Place this script to .git/hooks/pre-commit when you maintain this project.
└── venv # Virtual env
```

## Caution

It doesn't test full functionality of APIs, but basic operations.
To maintain this project, please place pre-commit on .git/hooks/pre-commit
