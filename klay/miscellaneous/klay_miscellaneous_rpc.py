import unittest
from utils import Utils
from common import klay as klay_common

# test_data_set is injected by rpc-tester/main.py
global test_data_set


class TestKlayNamespaceMiscellaneousRPC(unittest.TestCase):
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
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_klay_sha3_error_wrong_type_param(self):
        method = f"{self.ns}_sha3"
        data = Utils.convert_to_hex("Hi Utils!")
        params = ["data"]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToBytes", error)

    def test_klay_sha3_success(self):
        method = f"{self.ns}_sha3"
        data = Utils.convert_to_hex("Hi Utils!")
        params = [data]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_klay_forkStatus_success_no_param(self):
        method = f"{self.ns}_forkStatus"
        params = None
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_klay_forkStatus_error_wrong_value_param(self):
        method = f"{self.ns}_forkStatus"
        params = ["num"]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexWithoutPrefix", error)

    def test_klay_forkStatus_error_wrong_value_param2(self):
        method = f"{self.ns}_forkStatus"
        num = "latest"
        params = ["0xffffffff"]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "BlockNotExist", error)

    def test_klay_forkStatus_success(self):
        method = f"{self.ns}_forkStatus"
        params = ["latest"]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_klay_recoverFromTransaction_error_no_param(self):
        method = f"{self.ns}_recoverFromTransaction"
        params = None
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_klay_recoverFromTransaction_error_wrong_type_param1(self):
        method = f"{self.ns}_recoverFromTransaction"
        params = [123, "latest"]
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NonstringToBytes", error)

    def test_klay_recoverFromTransaction_error_wrong_type_param2(self):
        method = f"{self.ns}_recoverFromTransaction"
        params = ["num", "latest"]
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToBytes", error)

    def test_klay_recoverFromTransaction_error_wrong_value_param1(self):
        method = f"{self.ns}_recoverFromTransaction"
        txRawData = "0xffff"
        params = [txRawData, "latest"]
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "RlpExceed", error)

    def test_klay_recoverFromTransaction_error_wrong_value_param2(self):
        method = f"{self.ns}_recoverFromTransaction"
        txRawData = "0xec0c850ba43b74008261a8949957dfd92e4b70f91131c573293343bc5f21f2158829a2241af62c000080018080"
        params = [txRawData, "latest"]
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "InvalidTransaction", error)

    def test_klay_recoverFromTransaction_success(self):
        method = f"{self.ns}_recoverFromTransaction"
        txRawData = "0x08f88302850ba43b74008366926694000000000000000000000000000000000000dead843b9aca0094a2a8854b1802d8cd5de631e690817c253d6a9153f847f845820feaa07bbc8b9f248a4ad18e7059833f8e79b468f6323853880551b0867956d26a32e4a017784ff7c75de110316f44c8b60315b9d1b45e8954703c29f3a667e50a01f0f9"
        params = [txRawData, "latest"]
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_klay_recoverFromMessage_error_no_param(self):
        method = f"{self.ns}_recoverFromMessage"
        params = None
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_klay_recoverFromMessage_error_wrong_type_param1(self):
        method = f"{self.ns}_recoverFromMessage"
        address = "0xA2a8854b1802D8Cd5De631E690817c253d6a9153"
        message = "0xdeadbeef"
        sig = 123
        params = [address, message, sig, "latest"]
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg2NonstringToBytes", error)

    def test_klay_recoverFromMessage_error_wrong_type_param2(self):
        method = f"{self.ns}_recoverFromMessage"
        address = "0xA2a8854b1802D8Cd5De631E690817c253d6a9153"
        message = "0xdeadbeef"
        sig = "num"
        params = [address, message, sig, "latest"]
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg2HexToBytes", error)

    def test_klay_recoverFromMessage_error_wrong_value_param1(self):
        method = f"{self.ns}_recoverFromMessage"
        address = "0xA2a8854b1802D8Cd5De631E690817c253d6a9153"
        message = "0xdeadbeef"
        sig = "0xff"
        params = [address, message, sig, "latest"]
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "InvalidSignatureSize", error)

    def test_klay_recoverFromMessage_error_wrong_value_param2(self):
        method = f"{self.ns}_recoverFromMessage"
        address = "0xA2a8854b1802D8Cd5De631E690817c253d6a9153"
        message = "0xdeadbeef"
        sig = "0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
        params = [address, message, sig, "latest"]
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "InvalidKlaytnSignature", error)

    def test_klay_recoverFromMessage_success(self):
        method = f"{self.ns}_recoverFromMessage"
        address = "0xA2a8854b1802D8Cd5De631E690817c253d6a9153"
        message = "0xdeadbeef"
        sig = "0x1e6338d6e4a8d688a25de78cf2a92efec9a92e52eb8425acaaee8c3957e68cdb3f91bdc483f0ed05a0da26eca3be4c566d087d90dc2ca293be23b2a9de0bcafc1c"
        params = [address, message, sig, "latest"]
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    @staticmethod
    def suite():
        suite = unittest.TestSuite()

        suite.addTest(TestKlayNamespaceMiscellaneousRPC("test_klay_sha3_error_no_param"))
        suite.addTest(TestKlayNamespaceMiscellaneousRPC("test_klay_sha3_error_wrong_type_param"))
        suite.addTest(TestKlayNamespaceMiscellaneousRPC("test_klay_sha3_success"))
        suite.addTest(TestKlayNamespaceMiscellaneousRPC("test_klay_forkStatus_error_no_param"))
        suite.addTest(TestKlayNamespaceMiscellaneousRPC("test_klay_forkStatus_error_wrong_value_param"))
        suite.addTest(TestKlayNamespaceMiscellaneousRPC("test_klay_forkStatus_error_wrong_value_param2"))
        suite.addTest(TestKlayNamespaceMiscellaneousRPC("test_klay_forkStatus_success"))
        suite.addTest(TestKlayNamespaceMiscellaneousRPC("test_klay_recoverFromTransaction_error_no_param"))
        suite.addTest(TestKlayNamespaceMiscellaneousRPC("test_klay_recoverFromTransaction_error_wrong_type_param1"))
        suite.addTest(TestKlayNamespaceMiscellaneousRPC("test_klay_recoverFromTransaction_error_wrong_type_param2"))
        suite.addTest(TestKlayNamespaceMiscellaneousRPC("test_klay_recoverFromTransaction_error_wrong_value_param1"))
        suite.addTest(TestKlayNamespaceMiscellaneousRPC("test_klay_recoverFromTransaction_error_wrong_value_param2"))
        suite.addTest(TestKlayNamespaceMiscellaneousRPC("test_klay_recoverFromTransaction_success"))
        suite.addTest(TestKlayNamespaceMiscellaneousRPC("test_klay_recoverFromMessage_error_no_param"))
        suite.addTest(TestKlayNamespaceMiscellaneousRPC("test_klay_recoverFromMessage_error_wrong_type_param1"))
        suite.addTest(TestKlayNamespaceMiscellaneousRPC("test_klay_recoverFromMessage_error_wrong_type_param2"))
        suite.addTest(TestKlayNamespaceMiscellaneousRPC("test_klay_recoverFromMessage_error_wrong_value_param1"))
        suite.addTest(TestKlayNamespaceMiscellaneousRPC("test_klay_recoverFromMessage_error_wrong_value_param2"))
        suite.addTest(TestKlayNamespaceMiscellaneousRPC("test_klay_recoverFromMessage_success"))

        return suite
