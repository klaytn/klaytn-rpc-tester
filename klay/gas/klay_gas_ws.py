import unittest
from utils import Utils
from common import klay as klay_common

# test_data_set is injected by rpc-tester/main.py
global test_data_set


class TestKlayNamespaceGasWS(unittest.TestCase):
    config = Utils.get_config()
    _, _, log_path = Utils.get_log_filename_with_path()
    endpoint = config.get("endpoint")
    rpc_port = config.get("rpcPort")
    ws_port = config.get("wsPort")
    ns = "klay"
    waiting_count = 2

    def test_klay_maxPriorityFeePerGas_success(self):

        method = f"{self.ns}_maxPriorityFeePerGas"
        result, error = Utils.call_ws(self.endpoint, method, [], self.log_path)
        self.assertEqual(test_data_set["unitGasPrice"], result)
        self.assertIsNone(error)


    @staticmethod
    def suite():
        suite = unittest.TestSuite()

        suite.addTest(TestKlayNamespaceGasWS("test_klay_maxPriorityFeePerGas_success"))

        return suite
