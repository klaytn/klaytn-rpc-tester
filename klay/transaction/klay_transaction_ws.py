import unittest
import random
from unittest import result
from utils import Utils
from common import klay as klay_common

# test_data_set is injected by rpc-tester/main.py
global test_data_set


class TestKlayNamespaceTransactionWS(unittest.TestCase):
    config = Utils.get_config()
    _, _, log_path = Utils.get_log_filename_with_path()
    endpoint = config.get("endpoint")
    rpc_port = config.get("rpcPort")
    ws_port = config.get("wsPort")
    ns = "klay"
    waiting_count = 2

    def test_klay_sendTransaction_error_no_param1(self):

        method = f"{self.ns}_sendTransaction"
        params = None
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_klay_sendTransaction_error_no_param2(self):

        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_peb(1.5))

        params = [{"from": txFrom}]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "ContractCreationWithoutData", error)

    def test_klay_sendTransaction_error_no_param3(self):

        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_peb(1.5))

        params = [{"gasPrice": txGasPrice, "value": txValue}]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "ContractCreationWithoutData", error)

    def test_klay_sendTransaction_error_no_param4(self):

        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_peb(1.5))

        params = [{"to": txTo, "gas": txGas, "gasPrice": txGasPrice, "value": txValue}]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "UnknownAccount", error)

    def test_klay_sendTransaction_success_no_param1(self):

        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_peb(1.5))

        params = [{"from": txFrom, "to": txTo}]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_klay_sendTransaction_success_no_param2(self):

        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_peb(1.5))

        params = [{"from": txFrom, "to": txTo, "gas": txGas}]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_klay_sendTransaction_success_no_param3(self):

        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_peb(1.5))

        params = [{"from": txFrom, "to": txTo, "gas": txGas, "gasPrice": txGasPrice}]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_klay_sendTransaction_success_no_param4(self):

        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_peb(1.5))

        params = [{"from": txFrom, "to": txTo, "value": txValue}]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_klay_sendTransaction_success_no_param5(self):

        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_peb(1.5))

        params = [{"from": txFrom, "to": txTo, "gas": txGas, "value": txValue}]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_klay_sendTransaction_error_wrong_type_param1(self):

        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_peb(1.5))

        params = [
            {
                "from": 1234,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
            }
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NonstringToSendTxArgsFromAddress", error)

    def test_klay_sendTransaction_error_wrong_type_param2(self):

        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_peb(1.5))

        params = [
            {
                "from": txFrom,
                "to": 1234,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
            }
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NonstringToSendTxArgsToAddress", error)

    def test_klay_sendTransaction_error_wrong_type_param3(self):

        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_peb(1.5))

        params = [
            {
                "from": txFrom,
                "to": txTo,
                "gas": 1234,
                "gasPrice": txGasPrice,
                "value": txValue,
            }
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NonstringToSendTxArgsGasUint", error)

    def test_klay_sendTransaction_error_wrong_type_param4(self):

        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_peb(1.5))

        params = [
            {
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": 1234,
                "value": txValue,
            }
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NonstringToSendTxArgsGaspriceBig", error)

    def test_klay_sendTransaction_error_wrong_type_param5(self):

        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_peb(1.5))

        params = [
            {
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": 1234,
            }
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NonstringToSendTxArgsValueBig", error)

    def test_klay_sendTransaction_error_wrong_value_param1(self):

        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_peb(1.5))

        params = [
            {
                "from": txFrom + "1",
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
            }
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToSendTxArgsFromAddress", error)

    def test_klay_sendTransaction_error_wrong_value_param2(self):

        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_peb(1.5))

        params = [
            {
                "from": txFrom,
                "to": txTo + "1",
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
            }
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToSendTxArgsToAddress", error)

    def test_klay_sendTransaction_error_wrong_value_param3(self):

        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_peb(1.5))

        params = [
            {
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
            }
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "GasTooLow", error)

    def test_klay_sendTransaction_error_wrong_value_param4(self):

        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = hex(25)
        txValue = hex(Utils.to_peb(1.5))

        params = [
            {
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
            }
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "InvalidGasPrice", error)

    def test_klay_sendTransaction_error_wrong_value_param5(self):

        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_peb(1.5))

        params = [txFrom, "latest"]
        result, error = Utils.call_ws(self.endpoint, "klay_getBalance", params, self.log_path)
        self.assertIsNone(error)

        method = f"{self.ns}_sendTransaction"
        params = [
            {
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": result,
            }
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "InsufficientFunds", error)

    def test_klay_sendTransaction_success(self):

        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_peb(1.5))

        params = [
            {
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
            }
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_klay_signTransaction_error_no_param1(self):

        method = f"{self.ns}_signTransaction"
        params = []
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_klay_signTransaction_error_no_param2(self):

        method = f"{self.ns}_signTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(2441406250)

        params = [
            {
                "from": txFrom,
                "value": txValue,
            }
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "ContractCreationWithoutData", error)

    def test_klay_signTransaction_error_no_param3(self):

        method = f"{self.ns}_signTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(2441406250)

        params = [
            {
                "to": txTo,
                "value": txValue,
            }
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "UnknownAccount", error)

    def test_klay_signTransaction_success_no_param(self):

        method = f"{self.ns}_signTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(2441406250)

        params = [{"from": txFrom, "to": txTo}]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_klay_signTransaction_error_wrong_type_param1(self):

        method = f"{self.ns}_getTransactionCount"
        tag = "latest"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(2441406250)

        params = [txFrom, tag]
        nonce, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        method = f"{self.ns}_signTransaction"
        params = [
            {
                "from": 1234,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
                "nonce": nonce,
            }
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NonstringToSendTxArgsFromAddress", error)

    def test_klay_signTransaction_error_wrong_type_param2(self):

        method = f"{self.ns}_getTransactionCount"
        tag = "latest"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(2441406250)

        params = [txFrom, tag]
        nonce, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        method = f"{self.ns}_signTransaction"
        params = [
            {
                "from": txFrom,
                "to": 1234,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
                "nonce": nonce,
            }
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NonstringToSendTxArgsToAddress", error)

    def test_klay_signTransaction_error_wrong_type_param3(self):

        method = f"{self.ns}_getTransactionCount"
        tag = "latest"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(2441406250)

        params = [txFrom, tag]
        nonce, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        method = f"{self.ns}_signTransaction"
        params = [
            {
                "from": txFrom,
                "to": txTo,
                "gas": "txGas",
                "gasPrice": txGasPrice,
                "value": txValue,
                "nonce": nonce,
            }
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToSendTxArgsGasUint", error)

    def test_klay_signTransaction_error_wrong_type_param4(self):

        method = f"{self.ns}_getTransactionCount"
        tag = "latest"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(2441406250)

        params = [txFrom, tag]
        nonce, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        method = f"{self.ns}_signTransaction"
        params = [
            {
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": "txGasPrice",
                "value": txValue,
                "nonce": nonce,
            }
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToSendTxArgsGaspriceBig", error)

    def test_klay_signTransaction_error_wrong_type_param5(self):

        method = f"{self.ns}_getTransactionCount"
        tag = "latest"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(2441406250)

        params = [txFrom, tag]
        nonce, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        method = f"{self.ns}_signTransaction"
        params = [
            {
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": "txValue",
                "nonce": nonce,
            }
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToSendTxArgsValueBig", error)

    def test_klay_signTransaction_error_wrong_type_param6(self):

        method = f"{self.ns}_getTransactionCount"
        tag = "latest"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(2441406250)

        params = [txFrom, tag]
        nonce, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        method = f"{self.ns}_signTransaction"
        params = [
            {
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
                "nonce": "nonce",
            }
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToSendTxArgsNonceUint", error)

    def test_klay_signTransaction_error_wrong_value_param(self):

        method = f"{self.ns}_getTransactionCount"
        tag = "latest"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(2441406250)

        params = [txFrom, tag]
        nonce, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        method = f"{self.ns}_signTransaction"
        # Tx with Envelop
        params = [
            {
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
                "nonce": nonce,
                "typeInt": 30800,
            }
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "UndefinedTxType", error)

    def test_klay_signTransaction_success(self):

        method = f"{self.ns}_getTransactionCount"
        tag = "latest"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(2441406250)

        params = [txFrom, tag]
        nonce, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        method = f"{self.ns}_signTransaction"
        params = [
            {
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
                "nonce": nonce,
            }
        ]
        result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)
        self.assertEqual(result["tx"]["gasPrice"], txGasPrice)

    def test_klay_sendRawTransaction_error_no_param(self):

        method = f"{self.ns}_sendRawTransaction"
        params = []
        result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_klay_sendRawTransaction_error_wrong_type_param(self):

        method = f"{self.ns}_sendRawTransaction"
        params = ["abcd"]
        result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToBytes", error)

    def test_klay_sendRawTransaction_success(self):

        Utils.waiting_count("Waiting for", 5, "seconds until writing a block.")
        method = f"{self.ns}_getTransactionCount"
        tag = "latest"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(2441406250)

        params = [txFrom, tag]
        nonce, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        method = f"{self.ns}_signTransaction"
        params = [
            {
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
                "nonce": nonce,
            }
        ]
        result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        rawData = result["raw"]
        method = f"{self.ns}_sendRawTransaction"
        params = [rawData]
        result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_klay_sendRawTransaction_AccessList_error_wrong_prefix(self):

        method = f"{self.ns}_getTransactionCount"
        tag = "latest"
        txFrom = test_data_set["account"]["sender"]["address"]

        params = [txFrom, tag]
        nonce, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        method = f"{self.ns}_chainID"
        params = []
        chainId, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(2441)
        storageKeys = [
            "0x0000000000000000000000000000000000000000000000000000000000000003",
            "0x0000000000000000000000000000000000000000000000000000000000000007",
        ]
        accessList = [{"address": txFrom, "storageKeys": storageKeys}]
        transaction = {
            "from": txFrom,
            "to": txTo,
            "gas": txGas,
            "gasPrice": txGasPrice,
            "value": txValue,
            "nonce": nonce,
            "accessList": accessList,
            "chainId": chainId,
            "typeInt": 30721,
        }

        method = f"{self.ns}_signTransaction"
        params = [transaction]
        result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        rawData = result["raw"]
        rawTxWithoutHexPrefix = rawData[6:]

        testSize = 300
        for i in range(0, testSize):
            randomPrefix = hex(random.randint(81, 30720))
            if len(randomPrefix) % 2 == 1:
                randomPrefix = f"0x0{randomPrefix[2:]}"
            rawTx = randomPrefix + rawTxWithoutHexPrefix
            method = f"{self.ns}_sendRawTransaction"
            params = [rawTx]
            result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
            self.assertIsNotNone(error)
            self.assertTrue("undefined tx type" in error["message"] or "rlp:" in error["message"])

    def test_klay_sendRawTransaction_AccessList_success(self):

        Utils.waiting_count("Waiting for", 5, "seconds until writing a block.")
        method = f"{self.ns}_getTransactionCount"
        tag = "latest"
        txFrom = test_data_set["account"]["sender"]["address"]

        params = [txFrom, tag]
        nonce, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        method = f"{self.ns}_chainID"
        params = []
        chainId, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(2441)
        storageKeys = [
            "0x0000000000000000000000000000000000000000000000000000000000000003",
            "0x0000000000000000000000000000000000000000000000000000000000000007",
        ]
        accessList = [{"address": txFrom, "storageKeys": storageKeys}]
        transaction = {
            "from": txFrom,
            "to": txTo,
            "gas": txGas,
            "gasPrice": txGasPrice,
            "value": txValue,
            "nonce": nonce,
            "accessList": accessList,
            "chainId": chainId,
            "typeInt": 30721,
        }

        method = f"{self.ns}_signTransaction"
        params = [transaction]
        result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        method = f"{self.ns}_sendRawTransaction"
        rawData = result["raw"]
        params = [rawData]
        result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_klay_sendRawTransaction_DynamicFee_error_wrong_prefix(self):

        method = f"{self.ns}_getTransactionCount"
        tag = "latest"
        txFrom = test_data_set["account"]["sender"]["address"]

        params = [txFrom, tag]
        nonce, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        method = f"{self.ns}_chainID"
        params = []
        chainId, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(60400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(2441)
        storageKeys = [
            "0x0000000000000000000000000000000000000000000000000000000000000003",
            "0x0000000000000000000000000000000000000000000000000000000000000007",
        ]
        accessList = [{"address": txFrom, "storageKeys": storageKeys}]
        transaction = {
            "from": txFrom,
            "to": txTo,
            "gas": txGas,
            "maxPriorityFeePerGas": txGasPrice,
            "maxFeePerGas": txGasPrice,
            "value": txValue,
            "nonce": nonce,
            "accessList": accessList,
            "chainId": chainId,
            "typeInt": 30722,
        }

        method = f"{self.ns}_signTransaction"
        params = [transaction]
        result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        rawData = result["raw"]
        rawTxWithoutHexPrefix = rawData[6:]

        testSize = 300
        for i in range(0, testSize):
            randomPrefix = hex(random.randint(81, 30720))
            if len(randomPrefix) % 2 == 1:
                randomPrefix = f"0x0{randomPrefix[2:]}"
            rawTx = randomPrefix + rawTxWithoutHexPrefix
            method = f"{self.ns}_sendRawTransaction"
            params = [rawTx]
            result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
            self.assertIsNotNone(error)
            self.assertTrue("undefined tx type" in error["message"] or "rlp:" in error["message"])

    def test_klay_sendRawTransaction_DynamicFee_success(self):

        Utils.waiting_count("Waiting for", 5, "seconds until writing a block.")
        method = f"{self.ns}_getTransactionCount"
        tag = "latest"
        txFrom = test_data_set["account"]["sender"]["address"]

        params = [txFrom, tag]
        nonce, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        method = f"{self.ns}_chainID"
        params = []
        chainId, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(60400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(2441)
        storageKeys = [
            "0x0000000000000000000000000000000000000000000000000000000000000003",
            "0x0000000000000000000000000000000000000000000000000000000000000007",
        ]
        accessList = [{"address": txFrom, "storageKeys": storageKeys}]
        transaction = {
            "from": txFrom,
            "to": txTo,
            "gas": txGas,
            "maxPriorityFeePerGas": txGasPrice,
            "maxFeePerGas": txGasPrice,
            "value": txValue,
            "nonce": nonce,
            "accessList": accessList,
            "chainId": chainId,
            "typeInt": 30722,
        }

        method = f"{self.ns}_signTransaction"
        params = [transaction]
        result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        rawData = result["raw"]
        method = f"{self.ns}_sendRawTransaction"
        params = [rawData]
        txHash, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_klay_getTransactionByBlockHashAndIndex_error_no_param(self):

        method = f"{self.ns}_getTransactionByBlockHashAndIndex"

        params = []
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_klay_getTransactionByBlockHashAndIndex_error_wrong_type_param(self):

        method = f"{self.ns}_getTransactionByBlockHashAndIndex"

        params = ["txhash", "0x0"]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToHash", error)

    def test_klay_getTransactionByBlockHashAndIndex_error_wrong_value_param(self):

        method = f"{self.ns}_getTransactionByBlockHashAndIndex"

        params = [
            "0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
            "0x0",
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "BlockDoesNotExist", error)

    def test_klay_getTransactionByBlockHashAndIndex_success(self):

        method = f"{self.ns}_getTransactionByBlockHashAndIndex"
        txData = test_data_set["txData"]
        for tx in txData:
            params = [tx["result"]["blockHash"], tx["result"]["index"]]
            result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
            self.assertIsNone(error)
            self.assertIsNotNone(result["gasPrice"])

    def test_klay_getTransactionByBlockNumberAndIndex_error_no_param(self):

        method = f"{self.ns}_getTransactionByBlockNumberAndIndex"

        params = []
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_klay_getTransactionByBlockNumberAndIndex_error_wrong_value_param(self):

        method = f"{self.ns}_getTransactionByBlockNumberAndIndex"

        params = ["0xffffffff", "0x0"]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "BlockNotExist", error)

    def test_klay_getTransactionByBlockNumberAndIndex_success(self):

        method = f"{self.ns}_getTransactionByBlockNumberAndIndex"

        txData = test_data_set["txData"]
        for tx in txData:
            params = [tx["result"]["blockNumber"], tx["result"]["index"]]
            result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
            self.assertIsNone(error)
            self.assertIsNotNone(result["gasPrice"])

    def test_klay_getTransactionReceipt_error_no_param(self):

        method = f"{self.ns}_getTransactionReceipt"
        params = []
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_klay_getTransactionReceipt_error_wrong_type_param(self):

        method = f"{self.ns}_getTransactionReceipt"
        params = ["abcd"]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToHash", error)

    def test_klay_getTransactionReceipt_success_wrong_value_param(self):

        method = f"{self.ns}_getTransactionReceipt"
        params = ["0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_klay_getTransactionReceipt_success(self):

        method = f"{self.ns}_getTransactionReceipt"
        txData = test_data_set["txData"]
        for tx in txData:
            params = [tx["result"]["hash"]]
            _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
            self.assertIsNone(error)

    def test_klay_call_error_no_param1(self):

        method = f"{self.ns}_call"
        params = []
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_klay_call_error_no_param2(self):

        method = f"{self.ns}_call"
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        params = [{"to": contract}, "latest"]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "ExecutionReverted", error)

    def test_klay_call_error_no_param3(self):

        method = f"{self.ns}_call"
        methodName = "klay_call"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(0)
        params = [{"data": code}, "latest"]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "VMErrorOccurs", error)

    def test_klay_call_error_wrong_type_param1(self):

        method = f"{self.ns}_call"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(0)
        params = [
            {
                "from": 1234,
                "to": contract,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
                "data": code,
            },
            "latest",
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NonstringToCallArgsFromAddress", error)

    def test_klay_call_error_wrong_type_param2(self):

        method = f"{self.ns}_call"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(0)
        params = [
            {
                "from": address,
                "to": 1234,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
                "data": code,
            },
            "latest",
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NonstringToCallArgsToAddress", error)

    def test_klay_call_error_wrong_type_param3(self):

        method = f"{self.ns}_call"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(0)
        params = [
            {
                "from": address,
                "to": contract,
                "gas": "txGas",
                "gasPrice": txGasPrice,
                "value": txValue,
                "data": code,
            },
            "latest",
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToCallArgsGasUint64", error)

    def test_klay_call_error_wrong_type_param4(self):

        method = f"{self.ns}_call"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(0)
        params = [
            {
                "from": address,
                "to": contract,
                "gas": txGas,
                "gasPrice": "txGasPrice",
                "value": txValue,
                "data": code,
            },
            "latest",
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToCallArgsGaspriceBig", error)

    def test_klay_call_error_wrong_type_param5(self):

        method = f"{self.ns}_call"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(0)
        params = [
            {
                "from": address,
                "to": contract,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": "txValue",
                "data": code,
            },
            "latest",
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToCallArgsValueBig", error)

    def test_klay_call_error_wrong_type_param6(self):

        method = f"{self.ns}_call"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(0)
        params = [
            {
                "from": address,
                "to": contract,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
                "data": 1234,
            },
            "latest",
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NonstringToCallArgsDataBytes", error)

    def test_klay_call_error_wrong_type_param7(self):

        method = f"{self.ns}_call"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(0)
        params = [
            {
                "from": address,
                "to": contract,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
                "data": code,
            },
            "abcd",
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg1HexWithoutPrefix", error)

    def test_klay_call_error_wrong_value_param1(self):

        method = f"{self.ns}_call"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(100000000000000000000000000000000000000000)
        params = [
            {
                "from": address,
                "to": contract,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
                "data": code,
            },
            "latest",
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "ExecutionReverted", error)

    def test_klay_call_error_evm_revert_message(self):

        method = f"{self.ns}_call"
        address = test_data_set["account"]["sender"]["address"]
        ownerContract = test_data_set["contracts"]["unknown"]["address"][0]
        notOwner = "0x15318f21f3dee6b2c64d2a633cb8c1194877c882"
        changeOwnerAbi = "0xa6f9dae10000000000000000000000003e2ac308cd78ac2fe162f9522deb2b56d9da9499"
        params = [
            {"from": notOwner, "to": ownerContract, "data": changeOwnerAbi},
            "latest",
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "ExecutionReverted", error)

    def test_klay_call_error_insufficient_balance_feepayer(self):

        method = f"{self.ns}_call"
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        zeroBalanceAddr = "0x15318f21f3dee6b2c64d2a633cb8c1194877c882"
        code = test_data_set["contracts"]["unknown"]["input"]
        txGasPrice = test_data_set["unitGasPrice"]
        params = [
            {
                "from": zeroBalanceAddr,
                "to": contract,
                "data": code,
                "gas": "0x99999",
                "gasPrice": txGasPrice,
            },
            "latest",
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "InsufficientBalanceFeePayer", error)

    def test_klay_call_error_intrinsic_gas(self):

        method = f"{self.ns}_call"
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        zeroBalanceAddr = "0x15318f21f3dee6b2c64d2a633cb8c1194877c882"
        code = test_data_set["contracts"]["unknown"]["input"]
        txGasPrice = test_data_set["unitGasPrice"]
        params = [
            {
                "from": zeroBalanceAddr,
                "to": contract,
                "data": code,
                "gas": "0x99",
                "gasPrice": txGasPrice,
            },
            "latest",
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "GasTooLow", error)

    def test_klay_call_success1(self):

        method = f"{self.ns}_call"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        params = [{"to": contract, "data": code}, "latest"]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_klay_call_success2(self):

        method = f"{self.ns}_call"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        params = [{"from": address, "to": contract, "data": code}, "latest"]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_klay_call_success3(self):

        method = f"{self.ns}_call"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        params = [
            {
                "from": address,
                "to": contract,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "data": code,
            },
            "latest",
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_klay_call_success4(self):

        method = f"{self.ns}_call"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(0)
        params = [
            {
                "from": address,
                "to": contract,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
                "data": code,
            },
            "latest",
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_klay_call_success_state_override_balance_and_code(self):

        method = f"{self.ns}_call"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(0)
        # 잔고가 부족했지만 stateOverrides에 마치 잔고가 많은 것처럼 덮어씌어 call이 정상 수행될 수 있게끔 처리합니다.
        stateOverrides = {address: {"balance": hex(int(txGas, base=16) * int(txGasPrice, base=16))}}
        params = [
            {
                "from": address,
                "to": contract,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
                "data": code,
            },
            "latest",
            stateOverrides,
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_klay_estimateGas_error_no_param(self):

        method = f"{self.ns}_estimateGas"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(0)
        params = []
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_klay_estimateGas_error_wrong_type_param1(self):

        method = f"{self.ns}_estimateGas"
        address = test_data_set["account"]["sender"]["address"]
        contract = "abcd"
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(0)
        params = [{"from": address, "to": contract, "value": txValue, "data": code}]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToCallArgsToAddress", error)

    def test_klay_estimateGas_error_wrong_type_param2(self):

        method = f"{self.ns}_estimateGas"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = "abcd"
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(0)
        params = [{"from": address, "to": contract, "value": txValue, "data": code}]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0StringToCallArgsDataBytes", error)

    def test_klay_estimateGas_error_exceeds_allowance(self):

        method = f"{self.ns}_estimateGas"
        zeroBalanceAddr = "0x15318f21f3dee6b2c64d2a633cb8c1194877c882"
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(0)
        params = [
            {
                "from": zeroBalanceAddr,
                "to": contract,
                "data": code,
                "gas": "0x999",
                "gasPrice": txGasPrice,
            },
            "latest",
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "GasRequiredExceedsAllowance", error)

    def test_klay_estimateGas_error_evm_revert_message(self):

        method = f"{self.ns}_estimateGas"
        ownerContract = test_data_set["contracts"]["unknown"]["address"][0]
        notOwner = "0x15318f21f3dee6b2c64d2a633cb8c1194877c882"
        changeOwnerAbi = "0xa6f9dae10000000000000000000000003e2ac308cd78ac2fe162f9522deb2b56d9da9499"  # changeOwner("0x3e2ac308cd78ac2fe162f9522deb2b56d9da9499")
        params = [{"from": notOwner, "to": ownerContract, "data": changeOwnerAbi}]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "ExecutionReverted", error)

    def test_klay_estimateGas_error_revert(self):

        method = f"{self.ns}_estimateGas"
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        params = [{"to": contract}]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "ExecutionReverted", error)

    def test_klay_estimateGas_success(self):

        method = f"{self.ns}_estimateGas"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(0)
        params = [{"from": address, "to": contract, "value": txValue, "data": code}]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_klay_estimateComputationCost_success(self):

        method = f"{self.ns}_estimateComputationCost"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(0)
        params = [
            {
                "from": address,
                "to": contract,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
                "data": code,
            },
            "latest",
        ]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_klay_getTransactionByHash_error_no_param(self):

        method = f"{self.ns}_getTransactionByHash"
        params = []
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_klay_getTransactionByHash_error_wrong_type_param(self):

        method = f"{self.ns}_getTransactionByHash"
        params = [1234]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NonstringToHash", error)

    def test_klay_getTransactionByHash_success_wrong_value_param(self):

        method = f"{self.ns}_getTransactionByHash"
        params = ["0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_klay_getTransactionByHash_success(self):

        method = f"{self.ns}_getTransactionByHash"
        txData = test_data_set["txData"]
        for tx in txData:
            params = [tx["result"]["hash"]]
            result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
            self.assertIsNone(error)
            self.assertIsNotNone(result)
            self.assertIsNotNone(result["gasPrice"])
            if result["typeInt"] == 30722: # TxTypeEthereumDynamicFee
                self.assertIsNotNone(result["maxFeePerGas"])
                self.assertIsNotNone(result["maxPriorityFeePerGas"])

    def test_klay_getTransactionBySenderTxHash_error_no_param(self):

        method = f"{self.ns}_getTransactionBySenderTxHash"
        params = []
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_klay_getTransactionBySenderTxHash_error_wrong_type_param(self):

        method = f"{self.ns}_getTransactionBySenderTxHash"
        params = ["abcd"]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToHash", error)

    def test_klay_getTransactionBySenderTxHash_success_wrong_value_param(self):

        method = f"{self.ns}_getTransactionBySenderTxHash"
        params = ["0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_klay_getTransactionBySenderTxHash_success(self):

        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_peb(1.5))
        params = [
            {
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
            }
        ]
        result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)
        txHash = result

        Utils.waiting_count("Waiting for", 5, "seconds until writing a block.")

        method = "klay_getTransactionBySenderTxHash"
        params = [txHash]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_klay_getTransactionReceiptBySenderTxHash_error_no_param(self):

        method = f"{self.ns}_getTransactionReceiptBySenderTxHash"
        params = []
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_klay_getTransactionReceiptBySenderTxHash_error_wrong_type_param(self):

        method = f"{self.ns}_getTransactionReceiptBySenderTxHash"
        params = ["txHash"]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToHash", error)

    def test_klay_getTransactionReceiptBySenderTxHash_success_wrong_value_param(self):

        method = f"{self.ns}_getTransactionReceiptBySenderTxHash"
        params = ["0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_klay_getTransactionReceiptBySenderTxHash_success(self):

        method = "personal_sendTransaction"
        tag = "latest"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_peb(1.5))

        params = [
            {
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
            },
            password,
        ]
        result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)
        txHash = result

        method = f"{self.ns}_getTransactionReceiptBySenderTxHash"
        params = [txHash]
        _, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    @staticmethod
    def suite():
        suite = unittest.TestSuite()
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_sendTransaction_error_no_param1"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_sendTransaction_error_no_param2"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_sendTransaction_error_no_param3"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_sendTransaction_error_no_param4"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_sendTransaction_success_no_param1"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_sendTransaction_success_no_param2"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_sendTransaction_success_no_param3"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_sendTransaction_success_no_param4"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_sendTransaction_success_no_param5"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_sendTransaction_error_wrong_type_param1"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_sendTransaction_error_wrong_type_param2"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_sendTransaction_error_wrong_type_param3"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_sendTransaction_error_wrong_type_param4"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_sendTransaction_error_wrong_type_param5"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_sendTransaction_error_wrong_value_param1"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_sendTransaction_error_wrong_value_param2"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_sendTransaction_error_wrong_value_param3"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_sendTransaction_error_wrong_value_param4"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_sendTransaction_error_wrong_value_param5"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_sendTransaction_success"))

        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_signTransaction_error_no_param1"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_signTransaction_error_no_param2"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_signTransaction_error_no_param3"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_signTransaction_success_no_param"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_signTransaction_error_wrong_type_param1"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_signTransaction_error_wrong_type_param2"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_signTransaction_error_wrong_type_param3"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_signTransaction_error_wrong_type_param4"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_signTransaction_error_wrong_type_param5"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_signTransaction_error_wrong_type_param6"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_signTransaction_error_wrong_value_param"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_signTransaction_success"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_sendRawTransaction_error_no_param"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_sendRawTransaction_error_wrong_type_param"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_sendRawTransaction_success"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_sendRawTransaction_AccessList_error_wrong_prefix"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_sendRawTransaction_AccessList_success"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_sendRawTransaction_DynamicFee_error_wrong_prefix"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_sendRawTransaction_DynamicFee_success"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_getTransactionByBlockHashAndIndex_error_no_param"))
        suite.addTest(
            TestKlayNamespaceTransactionWS("test_klay_getTransactionByBlockHashAndIndex_error_wrong_type_param")
        )
        suite.addTest(
            TestKlayNamespaceTransactionWS("test_klay_getTransactionByBlockHashAndIndex_error_wrong_value_param")
        )
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_getTransactionByBlockHashAndIndex_success"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_getTransactionByBlockNumberAndIndex_error_no_param"))
        suite.addTest(
            TestKlayNamespaceTransactionWS("test_klay_getTransactionByBlockNumberAndIndex_error_wrong_value_param")
        )
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_getTransactionByBlockNumberAndIndex_success"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_getTransactionReceipt_error_no_param"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_getTransactionReceipt_error_wrong_type_param"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_getTransactionReceipt_success_wrong_value_param"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_getTransactionReceipt_success"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_call_error_no_param1"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_call_error_no_param2"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_call_error_no_param3"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_call_error_wrong_type_param1"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_call_error_wrong_type_param2"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_call_error_wrong_type_param3"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_call_error_wrong_type_param4"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_call_error_wrong_type_param5"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_call_error_wrong_type_param6"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_call_error_wrong_type_param7"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_call_error_wrong_value_param1"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_call_error_evm_revert_message"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_call_success1"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_call_success2"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_call_success3"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_call_success4"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_estimateGas_error_no_param"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_estimateGas_error_wrong_type_param1"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_estimateGas_error_wrong_type_param2"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_estimateGas_error_evm_revert_message"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_estimateGas_success"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_estimateComputationCost_success"))

        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_getTransactionByHash_error_no_param"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_getTransactionByHash_error_wrong_type_param"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_getTransactionByHash_success_wrong_value_param"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_getTransactionByHash_success"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_getTransactionBySenderTxHash_error_no_param"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_getTransactionBySenderTxHash_error_wrong_type_param"))
        suite.addTest(
            TestKlayNamespaceTransactionWS("test_klay_getTransactionBySenderTxHash_success_wrong_value_param")
        )
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_getTransactionBySenderTxHash_success"))
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_getTransactionReceiptBySenderTxHash_error_no_param"))
        suite.addTest(
            TestKlayNamespaceTransactionWS("test_klay_getTransactionReceiptBySenderTxHash_error_wrong_type_param")
        )
        suite.addTest(
            TestKlayNamespaceTransactionWS("test_klay_getTransactionReceiptBySenderTxHash_success_wrong_value_param")
        )
        suite.addTest(TestKlayNamespaceTransactionWS("test_klay_getTransactionReceiptBySenderTxHash_success"))
        return suite
