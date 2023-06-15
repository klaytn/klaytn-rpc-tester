import unittest
from utils import Utils
from common import klay as klay_common

# test_data_set is injected by rpc-tester/main.py
global test_data_set


class TestKlayNamespaceConfigurationRPC(unittest.TestCase):
    config = Utils.get_config()
    _, _, log_path = Utils.get_log_filename_with_path()
    endpoint = config.get("endpoint")
    rpc_port = config.get("rpcPort")
    ws_port = config.get("wsPort")
    ns = "klay"
    waiting_count = 2

    def test_klay_protocolVersion_success_wrong_value_param(self):

        method = f"{self.ns}_protocolVersion"
        _, error = Utils.call_rpc(self.endpoint, method, ["abcd"], self.log_path)
        self.assertIsNone(error)

    def test_klay_protocolVersion_success(self):

        method = f"{self.ns}_protocolVersion"
        _, error = Utils.call_rpc(self.endpoint, method, [], self.log_path)
        self.assertIsNone(error)

    def test_klay_gasPrice_success_wrong_value_param(self):

        method = f"{self.ns}_gasPrice"
        _, error = Utils.call_rpc(self.endpoint, method, ["abcd"], self.log_path)
        self.assertIsNone(error)

    def test_klay_gasPrice_success(self):

        method = f"{self.ns}_gasPrice"
        _, error = Utils.call_rpc(self.endpoint, method, [], self.log_path)
        self.assertIsNone(error)

    def test_klay_isParallelDBWrite_success_wrong_value_param(self):

        method = f"{self.ns}_isParallelDBWrite"
        _, error = Utils.call_rpc(self.endpoint, method, ["abcd"], self.log_path)
        self.assertIsNone(error)

    def test_klay_isParallelDBWrite_success(self):

        method = f"{self.ns}_isParallelDBWrite"
        _, error = Utils.call_rpc(self.endpoint, method, [], self.log_path)
        self.assertIsNone(error)

    def test_klay_isSenderTxHashIndexingEnabled_success_wrong_value_param(self):

        method = f"{self.ns}_isSenderTxHashIndexingEnabled"
        _, error = Utils.call_rpc(self.endpoint, method, ["abcd"], self.log_path)
        self.assertIsNone(error)

    def test_klay_isSenderTxHashIndexingEnabled_success(self):

        method = f"{self.ns}_isSenderTxHashIndexingEnabled"
        _, error = Utils.call_rpc(self.endpoint, method, [], self.log_path)
        self.assertIsNone(error)

    def test_klay_rewardbase_success_wrong_value_param(self):

        method = f"{self.ns}_rewardbase"
        _, error = Utils.call_rpc(self.endpoint, method, ["abcd"], self.log_path)
        self.assertIsNone(error)

    def test_klay_rewardbase_success(self):

        method = f"{self.ns}_rewardbase"
        _, error = Utils.call_rpc(self.endpoint, method, [], self.log_path)
        self.assertIsNone(error)

    def test_klay_chainId_success(self):

        method = f"{self.ns}_chainId"
        params = None
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_klay_chainId_success_wrong_value_param(self):

        method = f"{self.ns}_chainId"
        params = ["abcd"]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_klay_clientVersion_success_wrong_value_param(self):

        method = f"{self.ns}_clientVersion"
        params = ["abcd"]
        _, error = Utils.call_rpc(self.endpoint, method, [], self.log_path)
        self.assertIsNone(error)

    def test_klay_clientVersion_success(self):

        method = f"{self.ns}_clientVersion"
        params = []
        _, error = Utils.call_rpc(self.endpoint, method, [], self.log_path)
        self.assertIsNone(error)

    @staticmethod
    def suite():
        suite = unittest.TestSuite()

        suite.addTest(TestKlayNamespaceConfigurationRPC("test_klay_protocolVersion_success_wrong_value_param"))
        suite.addTest(TestKlayNamespaceConfigurationRPC("test_klay_protocolVersion_success"))
        suite.addTest(TestKlayNamespaceConfigurationRPC("test_klay_gasPrice_success_wrong_value_param"))
        suite.addTest(TestKlayNamespaceConfigurationRPC("test_klay_gasPrice_success"))

        suite.addTest(TestKlayNamespaceConfigurationRPC("test_klay_isParallelDBWrite_success_wrong_value_param"))
        suite.addTest(TestKlayNamespaceConfigurationRPC("test_klay_isParallelDBWrite_success"))
        suite.addTest(
            TestKlayNamespaceConfigurationRPC("test_klay_isSenderTxHashIndexingEnabled_success_wrong_value_param")
        )
        suite.addTest(TestKlayNamespaceConfigurationRPC("test_klay_isSenderTxHashIndexingEnabled_success"))
        suite.addTest(TestKlayNamespaceConfigurationRPC("test_klay_rewardbase_success_wrong_value_param"))
        suite.addTest(TestKlayNamespaceConfigurationRPC("test_klay_rewardbase_success"))
        suite.addTest(TestKlayNamespaceConfigurationRPC("test_klay_chainId_success"))
        suite.addTest(TestKlayNamespaceConfigurationRPC("test_klay_chainId_success_wrong_value_param"))
        suite.addTest(TestKlayNamespaceConfigurationRPC("test_klay_clientVersion_success_wrong_value_param"))
        suite.addTest(TestKlayNamespaceConfigurationRPC("test_klay_clientVersion_success"))

        return suite
