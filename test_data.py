import json
from utils import Utils

# Below value are immutable which means Klaytn node always return that values
# when you call RPC with `eth_` namesapce APIs.
ETH_BASEFEE_PER_GAS = "0x0"
ETH_EXTRADATA = "0x"
ETH_SHA3_UNCLES = "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347"
ETH_MIX_HASH = "0x0000000000000000000000000000000000000000000000000000000000000000"
ETH_NONCE = "0x0000000000000000"
ETH_DIFFICULTY = "0x1"  # This value is from Klaytn's blockscore which is always 0x1.
immutable_fields = {
    "baseFeePerGas": ETH_BASEFEE_PER_GAS,
    "extraData": ETH_EXTRADATA,
    "sha3Uncles": ETH_SHA3_UNCLES,
    "mixHash": ETH_MIX_HASH,
    "nonce": ETH_NONCE,
    "difficulty": ETH_DIFFICULTY,
}

ETH_ZERO_HASHRATE = "0x0"
ETH_ZERO_HASHRATE_UINT = 0
ETH_MINING = False
ETH_NO_MINING_WORK = "no mining work available yet"
DUMMY_BLOCK_NONCE = "0x2030090005000100"
DUMMY_HASH = "0x3e39ec3b9f3b9d8786c0dc9f76e24fba63bc840cf57b12f24bdecf242c6a2c29"
ETH_SUBMIT_WORK = False
ETH_HASHRATE = False
DUMMY_HASHRATE = "0x15"
DUMMY_BLOCK_NUMBER = "0x20"
DUMMY_INDEX = "0x1"
ETH_ZERO_UNCLE_COUNT = "0x0"
