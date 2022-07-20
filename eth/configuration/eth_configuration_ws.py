import unittest
from utils import Utils

# test_data_set is injected by rpc-tester/main.py
global test_data_set


class TestEthNamespaceConfigurationWS(unittest.TestCase):
    config = Utils.get_config()
    _, _, log_path = Utils.get_log_filename_with_path()
    endpoint = config.get("endpoint")
    rpc_port = config.get("rpcPort")
    ws_port = config.get("wsPort")
    ns = "eth"
    waiting_count = 2

    def test_eth_coinbase_success(self):

        method = f"{self.ns}_coinbase"
        _, error = Utils.call_ws(self.endpoint, method, [], self.log_path)
        self.assertIsNone(error)

    def test_eth_etherbase_success(self):

        method = f"{self.ns}_etherbase"
        _, error = Utils.call_ws(self.endpoint, method, [], self.log_path)
        self.assertIsNone(error)

    def test_eth_gasPrice_success_wrong_value_param(self):

        method = f"{self.ns}_gasPrice"
        _, error = Utils.call_ws(self.endpoint, method, ["abcd"], self.log_path)
        self.assertIsNone(error)

    def test_eth_gasPrice_success(self):

        method = f"{self.ns}_gasPrice"
        _, error = Utils.call_ws(self.endpoint, method, [], self.log_path)
        self.assertIsNone(error)

    def test_eth_chainId_success(self):

        method = f"{self.ns}_chainId"
        params = None
        _, error = Utils.call_ws(self.endpoint, method, [], self.log_path)
        self.assertIsNone(error)

    def test_eth_chainId_success_wrong_value_param(self):

        method = f"{self.ns}_chainId"
        params = ["abcd"]
        _, error = Utils.call_ws(self.endpoint, method, [], self.log_path)
        self.assertIsNone(error)

    @staticmethod
    def suite():
        suite = unittest.TestSuite()

        suite.addTest(TestEthNamespaceConfigurationWS("test_eth_coinbase_success"))
        suite.addTest(TestEthNamespaceConfigurationWS("test_eth_etherbase_success"))
        suite.addTest(TestEthNamespaceConfigurationWS("test_eth_gasPrice_success_wrong_value_param"))
        suite.addTest(TestEthNamespaceConfigurationWS("test_eth_gasPrice_success"))
        suite.addTest(TestEthNamespaceConfigurationWS("test_eth_chainId_success"))
        suite.addTest(TestEthNamespaceConfigurationWS("test_eth_chainId_success_wrong_value_param"))

        return suite
