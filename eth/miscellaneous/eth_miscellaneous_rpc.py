from pickle import FALSE
import unittest

from utils import Utils
from common import eth as eth_common

# test_data_set is injected by rpc-tester/main.py
global test_data_set


class TestEthNamespaceMiscellaneousRPC(unittest.TestCase):
    config = Utils.get_config()
    _, _, log_path = Utils.get_log_filename_with_path()
    endpoint = config.get("endpoint")
    rpc_port = config.get("rpcPort")
    ws_port = config.get("wsPort")
    ns = "eth"
    waiting_count = 2

    def test_eth_hashrate_success(self):

        method = f"{self.ns}_hashrate"
        params = []
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)
        self.assertEqual(result, "0x0")

    def test_eth_mining_success(self):

        method = f"{self.ns}_mining"
        params = []
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)
        self.assertFalse(result)

    def test_eth_getWork_success(self):

        method = f"{self.ns}_getWork"
        params = []
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_eth_submitWork_error_no_param(self):

        method = f"{self.ns}_submitWork"
        params = []
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_eth_submitWork_error_wrong_type_param1(self):

        method = f"{self.ns}_submitWork"
        DUMMY_BLOCK_NONCE = "0x2030090005000100"
        DUMMY_HASH = "0x3e39ec3b9f3b9d8786c0dc9f76e24fba63bc840cf57b12f24bdecf242c6a2c29"
        params = [1234, DUMMY_HASH, DUMMY_HASH]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NumberToBlockNonce", error)

    def test_eth_submitWork_error_wrong_type_param2(self):

        method = f"{self.ns}_submitWork"
        DUMMY_BLOCK_NONCE = "0x2030090005000100"
        DUMMY_HASH = "0x3e39ec3b9f3b9d8786c0dc9f76e24fba63bc840cf57b12f24bdecf242c6a2c29"
        params = [DUMMY_BLOCK_NONCE, 2525, DUMMY_HASH]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg1NonstringToHash", error)

    def test_eth_submitWork_error_wrong_type_param3(self):

        method = f"{self.ns}_submitWork"
        DUMMY_BLOCK_NONCE = "0x2030090005000100"
        DUMMY_HASH = "0x3e39ec3b9f3b9d8786c0dc9f76e24fba63bc840cf57b12f24bdecf242c6a2c29"
        params = [DUMMY_BLOCK_NONCE, DUMMY_HASH, 2525]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg2NonstringToHash", error)

    def test_eth_submitWork_success(self):

        method = f"{self.ns}_submitWork"
        DUMMY_BLOCK_NONCE = "0x2030090005000100"
        DUMMY_HASH = "0x3e39ec3b9f3b9d8786c0dc9f76e24fba63bc840cf57b12f24bdecf242c6a2c29"
        params = [DUMMY_BLOCK_NONCE, DUMMY_HASH, DUMMY_HASH]
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)
        self.assertFalse(result)

    def test_eth_submitHashrate_error_wrong_type_param1(self):

        method = f"{self.ns}_submitHashrate"
        DUMMY_HASH = "0x3e39ec3b9f3b9d8786c0dc9f76e24fba63bc840cf57b12f24bdecf242c6a2c29"
        params = ["abcd", DUMMY_HASH]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0StringToHexutilUint64", error)

    def test_eth_submitHashrate_error_wrong_type_param2(self):

        method = f"{self.ns}_submitHashrate"
        params = ["0x11", 123123]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg1NonstringToHash", error)

    def test_eth_submitHashrate_success(self):

        method = f"{self.ns}_submitHashrate"
        DUMMY_HASHRATE = "0x15"
        DUMMY_HASH = "0x3e39ec3b9f3b9d8786c0dc9f76e24fba63bc840cf57b12f24bdecf242c6a2c29"
        params = [DUMMY_HASHRATE, DUMMY_HASH]
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)
        self.assertFalse(result)

    def test_eth_getHashrate_success(self):

        method = f"{self.ns}_getHashrate"
        params = []
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)
        self.assertEqual(result, 0)

    @staticmethod
    def suite():
        suite = unittest.TestSuite()

        suite.addTest(TestEthNamespaceMiscellaneousRPC("test_eth_hashrate_success"))
        suite.addTest(TestEthNamespaceMiscellaneousRPC("test_eth_mining_success"))
        suite.addTest(TestEthNamespaceMiscellaneousRPC("test_eth_submitWork_error_wrong_type_param1"))
        suite.addTest(TestEthNamespaceMiscellaneousRPC("test_eth_submitWork_error_wrong_type_param2"))
        suite.addTest(TestEthNamespaceMiscellaneousRPC("test_eth_submitWork_error_wrong_type_param3"))
        suite.addTest(TestEthNamespaceMiscellaneousRPC("test_eth_submitHashrate_error_wrong_type_param1"))
        suite.addTest(TestEthNamespaceMiscellaneousRPC("test_eth_submitHashrate_error_wrong_type_param2"))
        suite.addTest(TestEthNamespaceMiscellaneousRPC("test_eth_submitHashrate_success"))
        suite.addTest(TestEthNamespaceMiscellaneousRPC("test_eth_getHashrate_success"))

        return suite
