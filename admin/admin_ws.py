import unittest
import pathlib
from datetime import datetime
from time import time
from utils import Utils

# test_data_set is injected by rpc-tester/main.py
global test_data_set


class TestAdminNamespaceWS(unittest.TestCase):
    config = Utils.get_config()
    _, _, log_path = Utils.get_log_filename_with_path()
    endpoint = config.get("endpoint")
    rpc_port = config.get("rpcPort")
    ws_port = config.get("wsPort")
    ns = "admin"
    waiting_count = 2
    current_dt = None

    def test_admin_addPeer_error_no_param(self):
        method = f"{self.ns}_addPeer"
        _, error = Utils.call_ws(self.endpoint, method, [], self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_admin_addPeer_error_wrong_type_param(self):
        method = f"{self.ns}_addPeer"
        params = [1234]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NumberToString", error)

    def test_admin_addPeer_error_wrong_value_param(self):
        method = f"{self.ns}_addPeer"
        params = ["1234"]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "invalidNodeId", error)

    def test_admin_addPeer_success(self):
        method = f"{self.ns}_addPeer"
        kni = test_data_set["test"]["knis"][0]
        params = [kni]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def fetch_peer_count_and_peers(self):
        method_net_peerCount = f"net_peerCount"
        peer_count, error = Utils.call_rpc(self.endpoint, method_net_peerCount, [], self.log_path)
        self.assertIsNone(error)

        method_admin_peers = f"{self.ns}_peers"
        peers, error = Utils.call_rpc(self.endpoint, method_admin_peers, [], self.log_path)
        self.assertIsNone(error)

        return peer_count, peers

    def test_admin_addPeer_stopped_node_success(self):
        peer_count, peers = self.fetch_peer_count_and_peers()

        # Try to add stopped or non-operating node
        params = [test_data_set["test"]["knis"][1]]
        method = f"{self.ns}_addPeer"
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        # Stopped node should not be added as peer.
        new_peer_count, new_peers = self.fetch_peer_count_and_peers()
        self.assertEqual(peer_count, new_peer_count)
        self.assertEqual(peers, new_peers)

    def test_admin_addPeer_invalid_node_success(self):
        peer_count, peers = self.fetch_peer_count_and_peers()
        # Try to add invalid kni
        params = [test_data_set["test"]["knis"][2]]
        method = f"{self.ns}_addPeer"
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        # Stopped node should not be added as peer.
        new_peer_count, new_peers = self.fetch_peer_count_and_peers()
        self.assertEqual(peer_count, new_peer_count)
        self.assertEqual(peers, new_peers)

    def test_admin_removePeer_success(self):
        method = f"{self.ns}_removePeer"
        params = [
            "kni://a979fb575495b8d6db44f750317d0f4622bf4c2aa3365d6af7c284339968eef29b69ad0dce72a4d8db5ebb4968de0e3bec910127f134779fbcb0cb6d3331163c@10.0.0.1:32323"
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_admin_removePeer_error_no_param(self):
        method = f"{self.ns}_removePeer"
        _, error = Utils.call_ws(self.endpoint, method, [], self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_admin_removePeer_error_wrong_type_param(self):
        method = f"{self.ns}_removePeer"
        params = [1234]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NumberToString", error)

    def test_admin_removePeer_error_wrong_value_param(self):
        method = f"{self.ns}_removePeer"
        params = ["abcd"]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "invalidNodeId", error)

    def test_admin_peers_success(self):
        method = f"{self.ns}_peers"
        _, error = Utils.call_ws(self.endpoint, method, [], self.log_path)
        self.assertIsNone(error)

    def test_admin_peers_success_wrong_value_param(self):
        method = f"{self.ns}_peers"
        params = ["abcd"]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_admin_datadir_success(self):
        method = f"{self.ns}_datadir"
        _, error = Utils.call_ws(self.endpoint, method, [], self.log_path)
        self.assertIsNone(error)

    def test_admin_datadir_success_wrong_value_param(self):
        method = f"{self.ns}_datadir"
        params = ["abcd"]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_admin_nodeInfo_success_wrong_value_param(self):
        method = f"{self.ns}_nodeInfo"
        params = ["abcd"]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_admin_nodeInfo_success(self):
        method = f"{self.ns}_nodeInfo"
        _, error = Utils.call_ws(self.endpoint, method, [], self.log_path)
        self.assertIsNone(error)

    def test_admin_stopRPC_success_using_ws(self):
        method = f"{self.ns}_stopRPC"
        ws_result, error = Utils.call_ws(self.endpoint, method, None, self.log_path)  # Using RPC is intended.
        self.assertTrue(ws_result)
        self.assertIsNone(error)

        Utils.waiting_count("Waiting for", self.waiting_count, "seconds until stacking some klay logs.")

    def test_admin_stopRPC_error_http_rpc_not_running_using_ws(self):
        method = f"{self.ns}_stopRPC"
        _, error = Utils.call_ws(self.endpoint, method, None, self.log_path)  # Using RPC is intended.
        Utils.check_error(self, "HTTPRPCNotRunning", error)

        Utils.waiting_count("Waiting for", self.waiting_count, "seconds until stacking some klay logs.")

    def test_admin_startRPC_success_using_ws(self):
        # During running above tests, http endpoint is closed so we must request using RPC.
        method = f"{self.ns}_startRPC"
        ws_result, error = Utils.call_ws(self.endpoint, method, self.create_params_for_starting_rpc(), self.log_path)
        self.assertTrue(ws_result)
        self.assertIsNone(error)

    def test_admin_stopRPC_success_wrong_value_param_using_ws(self):
        method = f"{self.ns}_stopRPC"
        params = ["abcd"]
        ws_result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertTrue(ws_result)
        self.assertIsNone(error)

        Utils.waiting_count("Waiting for", self.waiting_count, "seconds until stacking some klay logs.")

    def test_admin_startRPC_success_no_param_using_ws(self):
        method = f"{self.ns}_startRPC"
        ws_result, error = Utils.call_ws(self.endpoint, method, None, self.log_path)  # Using RPC is intended.
        self.assertTrue(ws_result)
        self.assertIsNone(error)

    def create_params_for_starting_rpc(self):
        host = "0.0.0.0"
        port = int(self.rpc_port)
        cors = "*"
        apis = "admin,eth,klay,net,personal,debug,web3,txpool"
        return [host, port, cors, apis]

    def create_params_for_starting_ws(self):
        host = "0.0.0.0"
        port = int(self.ws_port)
        cors = "*"
        apis = "admin,eth,klay,net,personal,debug,web3,txpool"
        return [host, port, cors, apis]

    def test_admin_startRPC_error_wrong_type_param1_using_ws(self):
        method = f"{self.ns}_startRPC"
        params = self.create_params_for_starting_rpc()
        params[0] = 1234  # Invalid host
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)  # Using RPC is intended.
        Utils.check_error(self, "arg0NumberToString", error)

    def test_admin_startRPC_error_wrong_type_param2_using_ws(self):
        method = f"{self.ns}_startRPC"
        params = self.create_params_for_starting_rpc()
        params[1] = "portString"  # Invalid port
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)  # Using RPC is intended.
        Utils.check_error(self, "arg1StringToInt", error)

    def test_admin_startRPC_error_wrong_type_param3_using_ws(self):
        method = f"{self.ns}_startRPC"
        params = self.create_params_for_starting_rpc()
        params[2] = 1234  # Invalid cors
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)  # Using RPC is intended.
        Utils.check_error(self, "arg2NumberToString", error)

    def test_admin_startRPC_error_wrong_type_param4_using_ws(self):
        method = f"{self.ns}_startRPC"
        params = self.create_params_for_starting_rpc()
        params[3] = 1234  # Invalid apis
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)  # Using RPC is intended.
        Utils.check_error(self, "arg3NumberToString", error)

    def test_admin_startRPC_error_wrong_value_param1_using_ws(self):
        # Before testing this TC, stop rpc first.
        # If not, HTTP RPC already running on 0.0.0.0:8551 will be returned as error.
        method = f"{self.ns}_stopRPC"
        _, error = Utils.call_ws(self.endpoint, method, None, self.log_path)  # Using RPC is intended.
        self.assertIsNone(error)

        method = f"{self.ns}_startRPC"
        params = self.create_params_for_starting_rpc()
        params[0] = "abcd"  # Invalid host
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)  # Using RPC is intended.
        Utils.check_error(self, "NameResolutionFailure", error)

    def test_admin_startRPC_error_already_running_using_ws(self):
        method = f"{self.ns}_startRPC"
        params = self.create_params_for_starting_rpc()
        Utils.call_ws(self.endpoint, method, params, self.log_path)  # Using RPC is intended.

        # Call two times to get expected error
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)  # Using RPC is intended.
        Utils.check_error(self, "HTTPAlreadyRunning", error)

    def test_admin_stopWS_success_using_rpc(self):
        method = f"{self.ns}_stopWS"
        result_from_rpc, error = Utils.call_rpc(self.endpoint, method, None, self.log_path)
        self.assertTrue(result_from_rpc)
        self.assertIsNone(error)

        Utils.waiting_count("Waiting for", self.waiting_count, "seconds until stacking some klay logs.")

    def test_admin_startWS_success_using_rpc(self):
        method = f"{self.ns}_startWS"
        params = self.create_params_for_starting_ws()
        result_from_rpc, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertTrue(result_from_rpc)
        self.assertIsNone(error)

    def test_admin_stopWS_success_wrong_value_param_using_rpc(self):
        method = f"{self.ns}_stopWS"
        params = ["abcd"]
        result_from_rpc, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertTrue(result_from_rpc)
        self.assertIsNone(error)

        Utils.waiting_count("Waiting for", self.waiting_count, "seconds until stacking some klay logs.")

    def test_admin_stopWS_error_ws_not_running_using_rpc(self):
        method = f"{self.ns}_stopWS"
        result_from_rpc, error = Utils.call_rpc(self.endpoint, method, None, self.log_path)
        self.assertIsNone(result_from_rpc)
        Utils.check_error(self, "WSRPCNotRunning", error)

    def test_admin_startWS_error_wrong_type_param1_using_rpc(self):
        method = f"{self.ns}_startWS"
        params = self.create_params_for_starting_ws()
        params[0] = "abcd"  # Invalid host
        result_from_rpc, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(result_from_rpc)
        Utils.check_error(self, "NameResolutionFailure", error)

    def test_admin_startWS_error_wrong_type_param2_using_rpc(self):
        method = f"{self.ns}_startWS"
        params = self.create_params_for_starting_ws()
        params[1] = "wsPort"  # Invalid port
        result_from_rpc, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(result_from_rpc)
        Utils.check_error(self, "arg1StringToInt", error)

    def test_admin_startWS_error_wrong_type_param3_using_rpc(self):
        method = f"{self.ns}_startWS"
        params = self.create_params_for_starting_ws()
        params[2] = 1234  # Invalid cors
        result_from_rpc, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(result_from_rpc)
        Utils.check_error(self, "arg2NumberToString", error)

    def test_admin_startWS_error_wrong_type_param4_using_rpc(self):
        method = f"{self.ns}_startWS"
        params = self.create_params_for_starting_ws()
        params[3] = 1234  # Invalid apis
        result_from_rpc, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(result_from_rpc)
        Utils.check_error(self, "arg3NumberToString", error)

    def test_admin_startWS_error_wrong_value_param1_using_rpc(self):
        method = f"{self.ns}_startWS"
        params = self.create_params_for_starting_ws()
        params[0] = "abcd"  # Invalid host
        result_from_rpc, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(result_from_rpc)
        Utils.check_error(self, "NameResolutionFailure", error)

    def test_admin_startWS_success_no_param_using_rpc(self):
        method = f"{self.ns}_startWS"
        params = self.create_params_for_starting_ws()
        result_from_rpc, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertTrue(result_from_rpc)
        self.assertIsNone(error)

    def test_admin_startWS_error_already_running_using_rpc(self):
        method = f"{self.ns}_startWS"
        params = self.create_params_for_starting_ws()
        result_from_rpc, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(result_from_rpc)
        Utils.check_error(self, "WSAlreadyRunning", error)

    def test_admin_exportChain_success(self):
        method = f"{self.ns}_exportChain"
        TestAdminNamespaceWS.current_dt = datetime.fromtimestamp(time()).strftime("%Y%m%d%H%M%S")
        file_path = f"/tmp/chain_{TestAdminNamespaceWS.current_dt}_created_by_ws.txt"
        _, error = Utils.call_ws(self.endpoint, method, [file_path], self.log_path)
        self.assertIsNone(error)

        Utils.waiting_count("Waiting for", self.waiting_count, "seconds until stacking some klay logs.")

        self.assertTrue(pathlib.Path.exists(pathlib.Path(file_path)))

    def test_admin_exportChain_error_already_exist(self):
        method = f"{self.ns}_exportChain"
        file_path = f"/tmp/chain_{TestAdminNamespaceWS.current_dt}_created_by_ws.txt"
        _, error = Utils.call_ws(self.endpoint, method, [file_path], self.log_path)
        Utils.check_error(self, "ExistingFile", error)

        Utils.waiting_count("Waiting for", self.waiting_count, "seconds until stacking some klay logs.")

    def test_admin_exportChain_error_no_param(self):
        method = f"{self.ns}_exportChain"
        _, error = Utils.call_ws(self.endpoint, method, [""], self.log_path)
        Utils.check_error(self, "NoSuchFile", error)

    def test_admin_importChain_success(self):
        method = f"{self.ns}_importChain"
        file_path = f"/tmp/chain_{self.current_dt}_created_by_ws.txt"
        _, error = Utils.call_ws(self.endpoint, method, [file_path], self.log_path)
        self.assertIsNone(error)

        Utils.waiting_count("Waiting for", self.waiting_count, "seconds until stacking some klay logs.")

    def test_admin_importChain_error_no_param(self):
        method = f"{self.ns}_importChain"
        _, error = Utils.call_ws(self.endpoint, method, [""], self.log_path)
        Utils.check_error(self, "NoSuchFile", error)

    def test_admin_importChain_error_wrong_type_param(self):
        method = f"{self.ns}_importChain"
        _, error = Utils.call_ws(self.endpoint, method, [1234], self.log_path)
        Utils.check_error(self, "arg0NumberToString", error)

    def test_admin_importChain_error_wrong_value_param(self):
        method = f"{self.ns}_importChain"
        _, error = Utils.call_ws(self.endpoint, method, ["/tmp/noexists.txt"], self.log_path)
        Utils.check_error(self, "NoSuchFile", error)

    def test_admin_nodeConfig_success(self):
        method = f"{self.ns}_nodeConfig"
        _, error = Utils.call_ws(self.endpoint, method, [], self.log_path)
        self.assertIsNone(error)

        Utils.waiting_count("Waiting for", self.waiting_count, "seconds until stacking some klay logs.")

    @staticmethod
    def suite():
        suite = unittest.TestSuite()
        suite.addTest(TestAdminNamespaceWS("test_admin_addPeer_error_no_param"))
        suite.addTest(TestAdminNamespaceWS("test_admin_addPeer_error_wrong_type_param"))
        suite.addTest(TestAdminNamespaceWS("test_admin_addPeer_error_wrong_value_param"))
        suite.addTest(TestAdminNamespaceWS("test_admin_addPeer_success"))
        suite.addTest(TestAdminNamespaceWS("test_admin_addPeer_stopped_node_success"))
        suite.addTest(TestAdminNamespaceWS("test_admin_addPeer_invalid_node_success"))
        suite.addTest(TestAdminNamespaceWS("test_admin_removePeer_success"))
        suite.addTest(TestAdminNamespaceWS("test_admin_removePeer_error_no_param"))
        suite.addTest(TestAdminNamespaceWS("test_admin_removePeer_error_wrong_type_param"))
        suite.addTest(TestAdminNamespaceWS("test_admin_removePeer_error_wrong_value_param"))
        suite.addTest(TestAdminNamespaceWS("test_admin_peers_success"))
        suite.addTest(TestAdminNamespaceWS("test_admin_peers_success_wrong_value_param"))
        suite.addTest(TestAdminNamespaceWS("test_admin_datadir_success"))
        suite.addTest(TestAdminNamespaceWS("test_admin_datadir_success_wrong_value_param"))
        suite.addTest(TestAdminNamespaceWS("test_admin_nodeInfo_success_wrong_value_param"))
        suite.addTest(TestAdminNamespaceWS("test_admin_nodeInfo_success"))
        suite.addTest(TestAdminNamespaceWS("test_admin_stopRPC_success_using_ws"))
        suite.addTest(TestAdminNamespaceWS("test_admin_stopRPC_error_http_rpc_not_running_using_ws"))
        suite.addTest(TestAdminNamespaceWS("test_admin_startRPC_success_using_ws"))
        suite.addTest(TestAdminNamespaceWS("test_admin_stopRPC_success_wrong_value_param_using_ws"))
        suite.addTest(TestAdminNamespaceWS("test_admin_startRPC_success_no_param_using_ws"))
        suite.addTest(TestAdminNamespaceWS("test_admin_startRPC_error_wrong_type_param1_using_ws"))
        suite.addTest(TestAdminNamespaceWS("test_admin_startRPC_error_wrong_type_param2_using_ws"))
        suite.addTest(TestAdminNamespaceWS("test_admin_startRPC_error_wrong_type_param3_using_ws"))
        suite.addTest(TestAdminNamespaceWS("test_admin_startRPC_error_wrong_type_param4_using_ws"))
        suite.addTest(TestAdminNamespaceWS("test_admin_startRPC_error_wrong_value_param1_using_ws"))
        suite.addTest(TestAdminNamespaceWS("test_admin_startRPC_error_already_running_using_ws"))
        suite.addTest(TestAdminNamespaceWS("test_admin_stopWS_success_using_rpc"))
        suite.addTest(TestAdminNamespaceWS("test_admin_startWS_success_using_rpc"))
        suite.addTest(TestAdminNamespaceWS("test_admin_stopWS_success_wrong_value_param_using_rpc"))
        suite.addTest(TestAdminNamespaceWS("test_admin_stopWS_error_ws_not_running_using_rpc"))
        suite.addTest(TestAdminNamespaceWS("test_admin_startWS_error_wrong_type_param1_using_rpc"))
        suite.addTest(TestAdminNamespaceWS("test_admin_startWS_error_wrong_type_param2_using_rpc"))
        suite.addTest(TestAdminNamespaceWS("test_admin_startWS_error_wrong_type_param3_using_rpc"))
        suite.addTest(TestAdminNamespaceWS("test_admin_startWS_error_wrong_type_param4_using_rpc"))
        suite.addTest(TestAdminNamespaceWS("test_admin_startWS_error_wrong_value_param1_using_rpc"))
        suite.addTest(TestAdminNamespaceWS("test_admin_startWS_success_no_param_using_rpc"))
        suite.addTest(TestAdminNamespaceWS("test_admin_startWS_error_already_running_using_rpc"))
        suite.addTest(TestAdminNamespaceWS("test_admin_exportChain_success"))
        suite.addTest(TestAdminNamespaceWS("test_admin_exportChain_error_already_exist"))
        suite.addTest(TestAdminNamespaceWS("test_admin_exportChain_error_no_param"))
        suite.addTest(TestAdminNamespaceWS("test_admin_importChain_success"))
        suite.addTest(TestAdminNamespaceWS("test_admin_importChain_error_no_param"))
        suite.addTest(TestAdminNamespaceWS("test_admin_importChain_error_wrong_type_param"))
        suite.addTest(TestAdminNamespaceWS("test_admin_importChain_error_wrong_value_param"))
        suite.addTest(TestAdminNamespaceWS("test_admin_nodeConfig_success"))

        return suite
