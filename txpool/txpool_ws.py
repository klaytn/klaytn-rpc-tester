import unittest
import inspect
import types
from typing import cast
from utils import Utils
from common import personal as personal_common

# test_data_set is injected by rpc-tester/main.py
global test_data_set


class TestTxpoolNamespaceWS(unittest.TestCase):
    config = Utils.get_config()
    _, _, log_path = Utils.get_log_filename_with_path()
    endpoint = config.get("endpoint")
    rpc_port = config.get("rpcPort")
    ws_port = config.get("wsPort")
    ns = "txpool"
    waiting_count = 2

    def send_some_txs(self):
        tx_fields = {
            "from": test_data_set["account"]["sender"]["address"],
            "to": test_data_set["account"]["receiver"]["address"],
            "gas": hex(304000),
            "gasPrice": test_data_set["unitGasPrice"],
            "value": hex(Utils.to_peb(3)),
        }
        password = test_data_set["account"]["sender"]["password"]

        _, error = personal_common.send_transaction(self.endpoint, [tx_fields, password])
        self.assertIsNone(error)

        tx_fields["to"] = test_data_set["contracts"]["unknown"]["address"][0]
        tx_fields["value"] = hex(Utils.to_peb(1.5))

        _, error = personal_common.send_transaction(self.endpoint, [tx_fields, password])
        self.assertIsNone(error)

    def test_txpool_content_success_wrong_value_param(self):

        self.send_some_txs()
        method = f"{self.ns}_content"
        _, error = Utils.call_ws(self.endpoint, method, ["abcd"], self.log_path)
        self.assertIsNone(error)

    def test_txpool_content_success(self):

        self.send_some_txs()
        method = f"{self.ns}_content"
        _, error = Utils.call_ws(self.endpoint, method, [], self.log_path)
        self.assertIsNone(error)

    def test_txpool_inspect_success_wrong_value_param(self):

        method = f"{self.ns}_inspect"
        _, error = Utils.call_ws(self.endpoint, method, ["abcd"], self.log_path)
        self.assertIsNone(error)

    def test_txpool_inspect_success(self):

        method = f"{self.ns}_inspect"
        _, error = Utils.call_ws(self.endpoint, method, [], self.log_path)
        self.assertIsNone(error)

    def test_txpool_status_success_wrong_value(self):

        method = f"{self.ns}_status"
        _, error = Utils.call_ws(self.endpoint, method, ["abcd"], self.log_path)
        self.assertIsNone(error)

    def test_txpool_status_success(self):

        method = f"{self.ns}_status"
        _, error = Utils.call_ws(self.endpoint, method, [], self.log_path)
        self.assertIsNone(error)

    @staticmethod
    def suite():
        suite = unittest.TestSuite()
        suite.addTest(TestTxpoolNamespaceWS("test_txpool_content_success_wrong_value_param"))
        suite.addTest(TestTxpoolNamespaceWS("test_txpool_content_success"))
        suite.addTest(TestTxpoolNamespaceWS("test_txpool_inspect_success_wrong_value_param"))
        suite.addTest(TestTxpoolNamespaceWS("test_txpool_inspect_success"))
        suite.addTest(TestTxpoolNamespaceWS("test_txpool_status_success_wrong_value"))
        suite.addTest(TestTxpoolNamespaceWS("test_txpool_status_success"))

        return suite
