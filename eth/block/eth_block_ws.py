import unittest
from utils import Utils
from common import eth as eth_common

# test_data_set is injected by rpc-tester/main.py
global test_data_set


class TestEthNamespaceBlockWS(unittest.TestCase):
    config = Utils.get_config()
    _, _, log_path = Utils.get_log_filename_with_path()
    endpoint = config.get("endpoint")
    rpc_port = config.get("rpcPort")
    ws_port = config.get("wsPort")
    ns = "eth"
    waiting_count = 2

    def test_eth_syncing_success_wrong_value_param(self):
        method = f"{self.ns}_syncing"
        _, error = Utils.call_ws(self.endpoint, method, ["abcd"], self.log_path)
        self.assertIsNone(error)

    def test_eth_syncing_success(self):
        method = f"{self.ns}_syncing"
        _, error = Utils.call_ws(self.endpoint, method, [], self.log_path)
        self.assertIsNone(error)

    def test_eth_mining_success(self):
        method = f"{self.ns}_mining"
        _, error = Utils.call_ws(self.endpoint, method, [], self.log_path)
        self.assertIsNone(error)

    def test_eth_blockNumber_success(self):
        method = f"{self.ns}_blockNumber"
        params = []
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_eth_blockNumber_success_wrong_value_param(self):
        method = f"{self.ns}_blockNumber"
        params = ["abcd"]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_eth_getStorageAt_error_no_param(self):
        method = f"{self.ns}_getStorageAt"
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        position = "0x0"
        tag = "latest"
        params = []
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_eth_getStorageAt_error_wrong_type_param1(self):
        method = f"{self.ns}_getStorageAt"
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        position = "0x0"
        tag = "latest"
        params = ["contract", position, tag]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToAddress", error)

    def test_eth_getStorageAt_error_wrong_type_param2(self):
        method = f"{self.ns}_getStorageAt"
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        position = "0x0"
        tag = "latest"
        params = [contract, position, "0xffffffff"]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "HeaderNotExist", error)

    def test_eth_getStorageAt_success_wrong_value_param(self):
        method = f"{self.ns}_getStorageAt"
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        position = "0x0"
        tag = "latest"
        params = [contract, "position", tag]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_eth_getStorageAt_success(self):
        method = f"{self.ns}_getStorageAt"
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        position = "0x0"
        tag = "latest"
        params = [contract, position, tag]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_eth_getBlockTransactionCountByHash_error_no_param(self):
        txFrom = test_data_set["account"]["sender"]["address"]
        txTo = test_data_set["account"]["receiver"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(500000000000)
        params = [
            {
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
            }
        ]
        transaction_hash, error = eth_common.send_transaction(self.endpoint, params)
        self.assertIsNone(error)

        Utils.waiting_count("Waiting for", 5, "seconds to connect with a peer.")

        result, error = eth_common.get_transaction(self.endpoint, [transaction_hash])
        self.assertIsNone(error)
        hashOfBlock = result["blockHash"]
        blockNumber = result["blockNumber"]

        method = f"{self.ns}_getBlockTransactionCountByHash"
        params = []
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_eth_getBlockTransactionCountByHash_error_wrong_type_param(self):
        txFrom = test_data_set["account"]["sender"]["address"]
        txTo = test_data_set["account"]["receiver"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(500000000000)
        params = [
            {
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
            }
        ]
        transaction_hash, error = eth_common.send_transaction(self.endpoint, params)
        self.assertIsNone(error)

        Utils.waiting_count("Waiting for", 5, "seconds to connect with a peer.")

        result, error = eth_common.get_transaction(self.endpoint, [transaction_hash])
        self.assertIsNone(error)
        hashOfBlock = result["blockHash"]
        blockNumber = result["blockNumber"]

        method = f"{self.ns}_getBlockTransactionCountByHash"
        params = [1234]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NonstringToHash", error)

    def test_eth_getBlockTransactionCountByHash_error_wrong_value_param(self):
        txFrom = test_data_set["account"]["sender"]["address"]
        txTo = test_data_set["account"]["receiver"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(500000000000)
        params = [
            {
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
            }
        ]
        transaction_hash, error = eth_common.send_transaction(self.endpoint, params)
        self.assertIsNone(error)

        Utils.waiting_count("Waiting for", 5, "seconds to connect with a peer.")

        result, error = eth_common.get_transaction(self.endpoint, [transaction_hash])
        self.assertIsNone(error)
        hashOfBlock = result["blockHash"]
        blockNumber = result["blockNumber"]

        method = f"{self.ns}_getBlockTransactionCountByHash"
        params = ["0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"]
        result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(result)

    def test_eth_getBlockTransactionCountByHash_success(self):
        txFrom = test_data_set["account"]["sender"]["address"]
        txTo = test_data_set["account"]["receiver"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(500000000000)
        params = [
            {
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
            }
        ]
        transaction_hash, error = eth_common.send_transaction(self.endpoint, params)
        self.assertIsNone(error)

        Utils.waiting_count("Waiting for", 5, "seconds to connect with a peer.")

        result, error = eth_common.get_transaction(self.endpoint, [transaction_hash])
        self.assertIsNone(error)
        hashOfBlock = result["blockHash"]
        blockNumber = result["blockNumber"]

        method = f"{self.ns}_getBlockTransactionCountByHash"
        params = [hashOfBlock]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_eth_getBlockTransactionCountByNumber_error_no_param(self):
        method = f"{self.ns}_getBlockTransactionCountByNumber"
        params = []
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_eth_getBlockTransactionCountByNumber_error_wrong_type_param(self):
        method = f"{self.ns}_getBlockTransactionCountByNumber"
        params = ["blocknumber"]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexWithoutPrefix", error)

    def test_eth_getBlockTransactionCountByNumber_error_wrong_value_param(self):
        method = f"{self.ns}_getBlockTransactionCountByNumber"
        params = ["0xffffffff"]
        result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(result)

    def test_eth_getBlockTransactionCountByNumber_success(self):
        blockNumber = eth_common.get_block_number(self.endpoint)
        method = f"{self.ns}_getBlockTransactionCountByNumber"
        params = [blockNumber]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_eth_getBlockByHash_error_no_param(self):
        method = f"{self.ns}_getBlockByHash"
        params = []
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_eth_getBlockByHash_error_wrong_type_param1(self):
        method = f"{self.ns}_getBlockByHash"
        params = [True, True]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NonstringToHash", error)

    def test_eth_getBlockByHash_error_wrong_type_param2(self):
        method = f"{self.ns}_getBlockByNumber"
        num = "latest"
        params = [num, True]
        result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNotNone(result)
        blockHash = result["hash"]

        method = f"{self.ns}_getBlockByHash"
        params = [blockHash, "True"]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg1StringToBool", error)

    def test_eth_getBlockByHash_error_wrong_value_param(self):
        method = f"{self.ns}_getBlockByHash"
        params = [
            "0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
            True,
        ]
        result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        # Utils.check_error(self, "BlockDoesNotExist", error)
        self.assertIsNone(result)
        self.assertIsNone(error)

    def test_eth_getBlockByHash_success(self):
        method = f"{self.ns}_getBlockByNumber"
        num = "latest"
        params = [num, True]
        result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)
        eth_common.checkBaseFeePerGasFieldAndValue(self, result)
        blockHash = result["hash"]

        method = f"{self.ns}_getBlockByHash"
        params = [blockHash, True]
        result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)
        eth_common.checkBaseFeePerGasFieldAndValue(self, result)
        eth_common.checkEthereumBlockOrHeaderFormat(self, result)

    def test_eth_getBlockByNumber_error_no_param(self):
        method = f"{self.ns}_getBlockByNumber"
        num = "latest"
        params = []
        _, error = eth_common.send_transaction(self.endpoint, params)
        Utils.check_error(self, "arg0NoParams", error)

    def test_eth_getBlockByNumber_error_wrong_type_param1(self):
        method = f"{self.ns}_getBlockByNumber"
        num = "latest"
        params = [True, True]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexWithoutPrefix", error)

    def test_eth_getBlockByNumber_error_wrong_type_param2(self):
        method = f"{self.ns}_getBlockByNumber"
        num = "latest"
        params = [num, "True"]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg1StringToBool", error)

    def test_eth_getBlockByNumber_error_wrong_value_param1(self):
        method = f"{self.ns}_getBlockByNumber"
        num = "latest"
        params = ["num", True]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexWithoutPrefix", error)

    def test_eth_getBlockByNumber_error_wrong_value_param2(self):
        method = f"{self.ns}_getBlockByNumber"
        num = "latest"
        params = ["0xffffffff", True]
        result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        # Utils.check_error(self, "BlockNotExist", error)
        self.assertIsNone(result)
        self.assertIsNone(error)

    def test_eth_getBlockByNumber_success(self):
        method = f"{self.ns}_getBlockByNumber"
        num = "latest"
        params = [num, True]
        result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)
        eth_common.checkEthereumBlockOrHeaderFormat(self, result)

    def test_eth_getBlockReceipts_error_no_param(self):
        method = f"{self.ns}_getBlockReceipts"
        params = []
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_eth_getBlockReceipts_error_wrong_type_param(self):
        method = f"{self.ns}_getBlockReceipts"
        params = ["abcd"]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexWithoutPrefix", error)

    def test_eth_getBlockReceipts_fail_wrong_value_param(self):
        method = f"{self.ns}_getBlockReceipts"
        params = ["0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "BlockDoesNotExist", error)

    def test_eth_getBlockReceipts_success(self):
        method = f"{self.ns}_getBlockReceipts"
        params = [10]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_eth_getHeaderByHash_error_no_param(self):
        method = f"{self.ns}_getHeaderByNumber"
        num = "latest"
        params = [num]
        result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNotNone(result)
        blockHash = result["hash"]

        method = f"{self.ns}_getHeaderByHash"
        params = []
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_eth_getHeaderByHash_error_wrong_type_param1(self):
        method = f"{self.ns}_getHeaderByNumber"
        num = "latest"
        params = [num]
        result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNotNone(result)
        blockHash = result["hash"]

        method = f"{self.ns}_getHeaderByHash"
        params = [True, True]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NonstringToHash", error)

    def test_eth_getHeaderByHash_error_wrong_value_param(self):
        method = f"{self.ns}_getHeaderByHash"
        params = ["0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"]
        result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        # Utils.check_error(self, "HeaderDoesNotExist", error)
        self.assertIsNone(result)
        self.assertIsNone(error)

    def test_eth_getHeaderByHash_success(self):
        method = f"{self.ns}_getHeaderByNumber"
        num = "latest"
        params = [num]
        result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNotNone(result)
        blockHash = result["hash"]

        method = f"{self.ns}_getHeaderByHash"
        params = [blockHash]
        result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)
        eth_common.checkEthereumBlockOrHeaderFormat(self, result)

    def test_eth_getHeaderByNumber_error_no_param(self):
        method = f"{self.ns}_getHeaderByNumber"
        num = "latest"
        params = []
        _, error = eth_common.send_transaction(self.endpoint, params)
        Utils.check_error(self, "arg0NoParams", error)

    def test_eth_getHeaderByNumber_error_wrong_type_param1(self):
        method = f"{self.ns}_getHeaderByNumber"
        num = "latest"
        params = [True]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexWithoutPrefix", error)

    def test_eth_getHeaderByNumber_error_wrong_value_param1(self):
        method = f"{self.ns}_getHeaderByNumber"
        num = "latest"
        params = ["num"]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexWithoutPrefix", error)

    def test_eth_getHeaderByNumber_error_wrong_value_param2(self):
        method = f"{self.ns}_getHeaderByNumber"
        num = "latest"
        params = ["0xffffffff"]
        result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        # Utils.check_error(self, "HeaderDoesNotExist", error)
        self.assertIsNone(result)
        self.assertIsNone(error)

    def test_eth_getHeaderByNumber_success(self):
        method = f"{self.ns}_getHeaderByNumber"
        num = "latest"
        params = [num]
        result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)
        eth_common.checkEthereumBlockOrHeaderFormat(self, result)

    def test_eth_getUncleByBlockNumberAndIndex_error_no_param(self):
        method = f"{self.ns}_getUncleByBlockNumberAndIndex"
        params = []
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_eth_getUncleByBlockNumberAndIndex_success(self):
        method = f"{self.ns}_getUncleByBlockNumberAndIndex"
        DUMMY_BLOCK_NUMBER = "0x20"
        DUMMY_INDEX = "0x1"
        params = [DUMMY_BLOCK_NUMBER, DUMMY_INDEX]
        result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)
        self.assertIsNone(result)

    def test_eth_getUncleByBlockHashAndIndex_error_no_param(self):
        method = f"{self.ns}_getUncleByBlockHashAndIndex"
        params = []
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_eth_getUncleByBlockHashAndIndex_success(self):
        method = f"{self.ns}_getUncleByBlockHashAndIndex"
        DUMMY_HASH = "0x3e39ec3b9f3b9d8786c0dc9f76e24fba63bc840cf57b12f24bdecf242c6a2c29"
        DUMMY_INDEX = "0x1"
        params = [DUMMY_HASH, DUMMY_INDEX]
        result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)
        self.assertIsNone(result)

    def test_eth_getUncleCountByBlockNumber_error_no_param(self):
        method = f"{self.ns}_getUncleCountByBlockNumber"
        params = []
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_eth_getUncleCountByBlockNumber_success(self):
        method = f"{self.ns}_getUncleCountByBlockNumber"
        DUMMY_BLOCK_NUMBER = "0x20"
        params = [DUMMY_BLOCK_NUMBER]
        result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)
        self.assertEqual(result, "0x0")

    def test_eth_getUncleCountByBlockHash_error_no_param(self):
        method = f"{self.ns}_getUncleCountByBlockHash"
        params = []
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_eth_getUncleCountByBlockHash_success(self):
        method = f"{self.ns}_getUncleCountByBlockHash"
        DUMMY_HASH = "0x3e39ec3b9f3b9d8786c0dc9f76e24fba63bc840cf57b12f24bdecf242c6a2c29"
        params = [DUMMY_HASH]
        result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)
        self.assertIsNone(result)

    @staticmethod
    def suite():
        suite = unittest.TestSuite()

        suite.addTest(TestEthNamespaceBlockWS("test_eth_syncing_success_wrong_value_param"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_syncing_success"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_mining_success"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_blockNumber_success"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_blockNumber_success_wrong_value_param"))

        suite.addTest(TestEthNamespaceBlockWS("test_eth_getStorageAt_error_no_param"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_getStorageAt_error_wrong_type_param1"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_getStorageAt_error_wrong_type_param2"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_getStorageAt_success_wrong_value_param"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_getStorageAt_success"))

        suite.addTest(TestEthNamespaceBlockWS("test_eth_getBlockTransactionCountByHash_error_no_param"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_getBlockTransactionCountByHash_error_wrong_type_param"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_getBlockTransactionCountByHash_error_wrong_value_param"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_getBlockTransactionCountByHash_success"))

        suite.addTest(TestEthNamespaceBlockWS("test_eth_getBlockTransactionCountByNumber_error_no_param"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_getBlockTransactionCountByNumber_error_no_param"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_getBlockTransactionCountByNumber_error_wrong_type_param"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_getBlockTransactionCountByNumber_error_wrong_value_param"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_getBlockTransactionCountByNumber_success"))

        suite.addTest(TestEthNamespaceBlockWS("test_eth_getBlockByHash_error_no_param"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_getBlockByHash_error_wrong_type_param1"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_getBlockByHash_error_wrong_type_param2"))

        suite.addTest(TestEthNamespaceBlockWS("test_eth_getBlockByHash_error_wrong_value_param"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_getBlockByHash_success"))

        suite.addTest(TestEthNamespaceBlockWS("test_eth_getBlockByNumber_error_no_param"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_getBlockByNumber_error_wrong_type_param1"))

        suite.addTest(TestEthNamespaceBlockWS("test_eth_getBlockByNumber_error_wrong_type_param2"))

        suite.addTest(TestEthNamespaceBlockWS("test_eth_getBlockByNumber_error_wrong_value_param1"))

        suite.addTest(TestEthNamespaceBlockWS("test_eth_getBlockByNumber_error_wrong_value_param2"))

        suite.addTest(TestEthNamespaceBlockWS("test_eth_getBlockByNumber_success"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_getBlockReceipts_error_no_param"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_getBlockReceipts_error_wrong_type_param"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_getBlockReceipts_fail_wrong_value_param"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_getBlockReceipts_success"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_getHeaderByHash_error_no_param"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_getHeaderByHash_error_wrong_type_param1"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_getHeaderByHash_error_wrong_value_param"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_getHeaderByHash_success"))

        suite.addTest(TestEthNamespaceBlockWS("test_eth_getHeaderByNumber_error_no_param"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_getHeaderByNumber_error_wrong_type_param1"))

        suite.addTest(TestEthNamespaceBlockWS("test_eth_getHeaderByNumber_error_wrong_value_param1"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_getHeaderByNumber_error_wrong_value_param2"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_getHeaderByNumber_success"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_getUncleByBlockNumberAndIndex_error_no_param"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_getUncleByBlockNumberAndIndex_success"))

        suite.addTest(TestEthNamespaceBlockWS("test_eth_getUncleByBlockHashAndIndex_error_no_param"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_getUncleByBlockHashAndIndex_success"))

        suite.addTest(TestEthNamespaceBlockWS("test_eth_getUncleCountByBlockNumber_error_no_param"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_getUncleCountByBlockNumber_success"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_getUncleCountByBlockHash_error_no_param"))
        suite.addTest(TestEthNamespaceBlockWS("test_eth_getUncleCountByBlockHash_success"))

        return suite
