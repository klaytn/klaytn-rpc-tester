import unittest
from utils import Utils
from common import klay as klay_common

# test_data_set is injected by rpc-tester/main.py
global test_data_set


class TestKlayNamespaceGasRPC(unittest.TestCase):
    config = Utils.get_config()
    _, _, log_path = Utils.get_log_filename_with_path()
    endpoint = config.get("endpoint")
    rpc_port = config.get("rpcPort")
    ws_port = config.get("wsPort")
    ns = "klay"
    waiting_count = 2

    def test_klay_maxPriorityFeePerGas_success(self):

        method = f"{self.ns}_maxPriorityFeePerGas"
        result, error = Utils.call_rpc(self.endpoint, method, [], self.log_path)
        self.assertIsNone(error)
        self.assertEqual(test_data_set["unitGasPrice"], result)

    def test_klay_feeHistory_success(self):

        method = f"{self.ns}_feeHistory"
        blockCount = 3
        lastBlock = "latest"
        rewardPercentiles = [20, 30, 50]
        params = [blockCount, lastBlock, rewardPercentiles]
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)
        length = len(result["reward"])
        self.assertLessEqual(length, blockCount)
        self.assertEqual(length, len(result["gasUsedRatio"]))
        self.assertEqual(length + 1, len(result["baseFeePerGas"]))

    @staticmethod
    def suite():
        suite = unittest.TestSuite()

        suite.addTest(TestKlayNamespaceGasRPC("test_klay_maxPriorityFeePerGas_success"))
        suite.addTest(TestKlayNamespaceGasRPC("test_klay_feeHistory_success"))

        return suite
