import unittest
import inspect
import types
from typing import cast
from utils import Utils

# test_data_set is injected by rpc-tester/main.py
global test_data_set


class TestEthNamespaceGasRPC(unittest.TestCase):
    config = Utils.get_config()
    _, _, log_path = Utils.get_log_filename_with_path()
    endpoint = config.get("endpoint")
    rpc_port = config.get("rpcPort")
    ws_port = config.get("wsPort")
    ns = "eth"
    waiting_count = 2

    def test_eth_maxPriorityFeePerGas_success(self):

        method = f"{self.ns}_maxPriorityFeePerGas"
        result, error = Utils.call_rpc(self.endpoint, method, [], self.log_path)
        self.assertEqual(test_data_set["unitGasPrice"], result)
        self.assertIsNone(error)

        Utils.write_log(
            self.log_path,
            "",
            "",
            "",
            "",
            Utils.TestingStatus.FINISHED,
            cast(types.FrameType, inspect.currentframe()).f_code.co_name,
        )
