import unittest
from utils import Utils
from common import klay as klay_common

# test_data_set is injected by rpc-tester/main.py
global test_data_set


class TestKlayNamespaceMiscellaneousWS(unittest.TestCase):
    config = Utils.get_config()
    _, _, log_path = Utils.get_log_filename_with_path()
    endpoint = config.get("endpoint")
    rpc_port = config.get("rpcPort")
    ws_port = config.get("wsPort")
    ns = "klay"
    waiting_count = 2

    def test_klay_sha3_error_no_param(self):
        method = f"{self.ns}_sha3"
        data = Utils.convert_to_hex("Hi Utils!")
        params = None
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_klay_sha3_error_wrong_type_param(self):
        method = f"{self.ns}_sha3"
        data = Utils.convert_to_hex("Hi Utils!")
        params = ["data"]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToBytes", error)

    def test_klay_sha3_success(self):
        method = f"{self.ns}_sha3"
        data = Utils.convert_to_hex("Hi Utils!")
        params = [data]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    @staticmethod
    def suite():
        suite = unittest.TestSuite()

        suite.addTest(TestKlayNamespaceMiscellaneousWS("test_klay_sha3_error_no_param"))
        suite.addTest(TestKlayNamespaceMiscellaneousWS("test_klay_sha3_error_wrong_type_param"))
        suite.addTest(TestKlayNamespaceMiscellaneousWS("test_klay_sha3_success"))

        return suite
