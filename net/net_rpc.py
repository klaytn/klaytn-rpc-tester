import unittest
from binascii import hexlify
from os import urandom
from utils import Utils

# test_data_set is injected by rpc-tester/main.py
global test_data_set


class TestNetNamespaceRPC(unittest.TestCase):
    config = Utils.get_config()
    _, _, log_path = Utils.get_log_filename_with_path()
    endpoint = config.get("endpoint")
    rpc_port = config.get("rpcPort")
    ws_port = config.get("wsPort")
    ns = "net"
    waiting_count = 2

    def test_net_version_success(self):
        method = f"{self.ns}_version"

        _, error = Utils.call_rpc(self.endpoint, method, [], self.log_path)
        self.assertIsNone(error)

    def test_net_networkID_success_wrong_value_param(self):
        method = f"{self.ns}_networkID"
        params = ["abcd"]

        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_net_networkID_success(self):
        method = f"{self.ns}_networkID"
        params = []
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_net_listening_success_wrong_value_param(self):
        method = f"{self.ns}_listening"
        params = ["abcd"]

        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_net_listening_success(self):
        method = f"{self.ns}_listening"
        params = []
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_net_peerCount_success_wrong_value_param(self):
        method = f"{self.ns}_peerCount"
        params = ["abcd"]

        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_net_peerCount_success(self):
        method = f"{self.ns}_peerCount"
        params = []
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_net_peerCountByType_success(self):
        method = f"{self.ns}_peerCountByType"
        params = []
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    @staticmethod
    def suite():
        suite = unittest.TestSuite()
        suite.addTest(TestNetNamespaceRPC("test_net_version_success"))
        suite.addTest(TestNetNamespaceRPC("test_net_networkID_success_wrong_value_param"))
        suite.addTest(TestNetNamespaceRPC("test_net_networkID_success"))
        suite.addTest(TestNetNamespaceRPC("test_net_listening_success_wrong_value_param"))
        suite.addTest(TestNetNamespaceRPC("test_net_listening_success"))
        suite.addTest(TestNetNamespaceRPC("test_net_peerCount_success_wrong_value_param"))
        suite.addTest(TestNetNamespaceRPC("test_net_peerCount_success"))
        suite.addTest(TestNetNamespaceRPC("test_net_peerCountByType_success"))

        return suite
