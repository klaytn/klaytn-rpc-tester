import unittest
from binascii import hexlify
from os import urandom
from utils import Utils

# test_data_set is injected by rpc-tester/main.py
global test_data_set


class TestPersonalNamespaceRPC(unittest.TestCase):
    config = Utils.get_config()
    _, _, log_path = Utils.get_log_filename_with_path()
    endpoint = config.get("endpoint")
    rpc_port = config.get("rpcPort")
    ws_port = config.get("wsPort")
    ns = "personal"
    waiting_count = 2

    def test_personal_importRawKey_error_no_param1(self):
        method = f"{self.ns}_importRawKey"
        _, error = Utils.call_rpc(self.endpoint, method, [], self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_personal_importRawKey_error_no_param2(self):
        method = f"{self.ns}_importRawKey"
        key = hexlify(urandom(32)).decode()
        result, error = Utils.call_rpc(self.endpoint, method, [key], self.log_path)
        Utils.check_error(self, "arg1NoParams", error)

    def test_personal_importRawKey_error_wrong_type_param1(self):
        method = f"{self.ns}_importRawKey"
        _, error = Utils.call_rpc(
            self.endpoint,
            method,
            [1234, test_data_set["account"]["import"]["password"]],
            self.log_path,
        )
        Utils.check_error(self, "arg0NumberToString", error)

    def test_personal_importRawKey_error_wrong_type_param2(self):
        method = f"{self.ns}_importRawKey"
        key = hexlify(urandom(32)).decode()
        _, error = Utils.call_rpc(self.endpoint, method, [key, 1234], self.log_path)
        Utils.check_error(self, "arg1NumberToString", error)

    def test_personal_importRawKey_error_wrong_value_param1(self):
        method = f"{self.ns}_importRawKey"
        _, error = Utils.call_rpc(self.endpoint, method, ["wrongKey", "wrongPasswordValue"], self.log_path)
        Utils.check_error(self, "InvalidHexString", error)

    def test_personal_importRawKey_success(self):
        method = f"{self.ns}_importRawKey"
        key = hexlify(urandom(32)).decode()
        passphrase = test_data_set["account"]["import"]["password"]
        result, error = Utils.call_rpc(self.endpoint, method, [key, passphrase], self.log_path)
        self.assertIsNone(error)
        imported_address = result

        result, error = Utils.call_rpc(self.endpoint, f"{self.ns}_listAccounts", [], self.log_path)
        self.assertIsNone(error)
        self.assertIn(imported_address, result)

    def test_personal_listAccounts_success_wrong_value_param(self):
        method = f"{self.ns}_listAccounts"
        _, error = Utils.call_rpc(self.endpoint, method, ["abcd"], self.log_path)
        self.assertIsNone(error)

    def test_personal_listAccounts_success(self):
        method = f"{self.ns}_listAccounts"
        _, error = Utils.call_rpc(self.endpoint, method, [], self.log_path)
        self.assertIsNone(error)

    def test_personal_lockAccount_error_no_param(self):
        method = f"{self.ns}_lockAccount"
        _, error = Utils.call_rpc(self.endpoint, method, [], self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_personal_lockAccount_error_wrong_type_param1(self):
        method = f"{self.ns}_lockAccount"
        _, error = Utils.call_rpc(self.endpoint, method, [1234], self.log_path)
        Utils.check_error(self, "arg0NonstringToAddress", error)

    def test_personal_lockAccount_error_wrong_type_param2(self):
        method = f"{self.ns}_lockAccount"
        _, error = Utils.call_rpc(self.endpoint, method, ["strangeStrings"], self.log_path)
        Utils.check_error(self, "arg0HexToAddress", error)

    def test_personal_lockAccount_success(self):
        method = f"{self.ns}_lockAccount"
        address = test_data_set["account"]["sender"]["address"]
        _, error = Utils.call_rpc(self.endpoint, method, [address], self.log_path)
        self.assertIsNone(error)

    def test_personal_unlockAccount_error_no_param1(self):
        method = f"{self.ns}_unlockAccount"
        _, error = Utils.call_rpc(self.endpoint, method, [], self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_personal_unlockAccount_error_no_param2(self):
        method = f"{self.ns}_unlockAccount"
        address = test_data_set["account"]["sender"]["address"]
        _, error = Utils.call_rpc(self.endpoint, method, [address], self.log_path)
        Utils.check_error(self, "arg1NoParams", error)

    def test_personal_unlockAccount_error_wrong_type_param1(self):
        method = f"{self.ns}_unlockAccount"
        _, error = Utils.call_rpc(self.endpoint, method, ["address", "passPhrase", "duration"], self.log_path)
        Utils.check_error(self, "arg0HexToAddress", error)

    def test_personal_unlockAccount_error_wrong_type_param2(self):
        method = f"{self.ns}_unlockAccount"
        address = test_data_set["account"]["sender"]["address"]
        passphrase = test_data_set["account"]["sender"]["password"]
        _, error = Utils.call_rpc(self.endpoint, method, [address, passphrase, "duration"], self.log_path)
        Utils.check_error(self, "arg2StringToUint64", error)

    def test_personal_unlockAccount_error_wrong_type_param3(self):
        method = f"{self.ns}_unlockAccount"
        passphrase = test_data_set["account"]["sender"]["password"]
        duration = 100000
        _, error = Utils.call_rpc(self.endpoint, method, ["address", passphrase, duration], self.log_path)
        Utils.check_error(self, "arg0HexToAddress", error)

    def test_personal_unlockAccount_error_wrong_value_param(self):
        method = f"{self.ns}_unlockAccount"
        address = test_data_set["account"]["sender"]["address"]
        duration = 100000
        _, error = Utils.call_rpc(
            self.endpoint,
            method,
            [address, "dontknowPassword", duration],
            self.log_path,
        )
        Utils.check_error(self, "CouldntDecryptKey", error)

    def test_personal_unlockAccount_success_no_duration(self):
        method = f"{self.ns}_unlockAccount"
        address = test_data_set["account"]["sender"]["address"]
        passphrase = test_data_set["account"]["sender"]["password"]
        _, error = Utils.call_rpc(self.endpoint, method, [address, passphrase], self.log_path)
        self.assertIsNone(error)

    def test_personal_unlockAccount_success(self):
        method = f"{self.ns}_unlockAccount"
        address = test_data_set["account"]["sender"]["address"]
        passphrase = test_data_set["account"]["sender"]["password"]
        duration = 1000000
        _, error = Utils.call_rpc(self.endpoint, method, [address, passphrase, duration], self.log_path)
        self.assertIsNone(error)

    def test_personal_newAccount_error_no_param(self):
        method = f"{self.ns}_newAccount"
        _, error = Utils.call_rpc(self.endpoint, method, [], self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_personal_newAccount_error_wrong_type_param(self):
        method = f"{self.ns}_newAccount"
        _, error = Utils.call_rpc(self.endpoint, method, [1234], self.log_path)
        Utils.check_error(self, "arg0NumberToString", error)

    def test_personal_newAccount_success(self):
        method = f"{self.ns}_newAccount"
        passphrase = test_data_set["account"]["sender"]["password"]
        _, error = Utils.call_rpc(self.endpoint, method, [passphrase], self.log_path)
        self.assertIsNone(error)

    def send_transaction(self, tx_fields=None, password=None):
        params = []
        if tx_fields is not None:
            params.append(tx_fields)
        if password is not None:
            params.append(password)
        method = f"{self.ns}_sendTransaction"
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)

        return result, error

    def test_personal_sendTransaction_error_no_param1(self):
        _, error = self.send_transaction()
        Utils.check_error(self, "arg0NoParams", error)

    def test_personal_sendTransaction_error_no_param2(self):
        sender = test_data_set["account"]["sender"]["address"]
        _, error = self.send_transaction({"from": sender})
        Utils.check_error(self, "arg1NoParams", error)

    def test_personal_sendTransaction_error_no_param3(self):
        password = test_data_set["account"]["sender"]["password"]
        _, error = self.send_transaction(None, password)
        Utils.check_error(self, "arg0StringToSendtx", error)

    def test_personal_sendTransaction_error_no_param4(self):
        password = test_data_set["account"]["sender"]["password"]
        gas_price = test_data_set["unitGasPrice"]
        value = hex(Utils.to_peb(1.5))

        _, error = self.send_transaction({"gasPrice": gas_price, "value": value}, password)
        Utils.check_error(self, "ContractCreationWithoutData", error)

    def test_personal_sendTransaction_error_no_param5(self):
        password = test_data_set["account"]["sender"]["password"]
        to = test_data_set["account"]["receiver"]["address"]
        gas = hex(304000)
        gas_price = test_data_set["unitGasPrice"]
        value = hex(Utils.to_peb(1.5))

        _, error = self.send_transaction({"to": to, "gas": gas, "gasPrice": gas_price, "value": value}, password)
        Utils.check_error(self, "UnknownAccount", error)

    def test_personal_sendTransaction_error_no_param6(self):
        sender = test_data_set["account"]["sender"]["address"]
        gas = hex(304000)
        gas_price = test_data_set["unitGasPrice"]
        value = hex(Utils.to_peb(1.5))

        _, error = self.send_transaction({"from": sender, "gas": gas, "gasPrice": gas_price, "value": value}, None)
        Utils.check_error(self, "arg1NoParams", error)

    def test_personal_sendTransaction_success_no_param1(self):
        sender = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        to = test_data_set["account"]["receiver"]["address"]

        _, error = self.send_transaction({"from": sender, "to": to}, password)
        self.assertIsNone(error)

    def test_personal_sendTransaction_success_no_param2(self):
        sender = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        to = test_data_set["account"]["receiver"]["address"]
        gas = hex(304000)

        _, error = self.send_transaction({"from": sender, "to": to, "gas": gas}, password)
        self.assertIsNone(error)

    def test_personal_sendTransaction_success_no_param3(self):
        sender = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        to = test_data_set["account"]["receiver"]["address"]
        gas = hex(304000)
        gas_price = test_data_set["unitGasPrice"]

        _, error = self.send_transaction({"from": sender, "to": to, "gas": gas, "gasPrice": gas_price}, password)
        self.assertIsNone(error)

    def test_personal_sendTransaction_success_no_param4(self):
        sender = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        to = test_data_set["account"]["receiver"]["address"]
        value = hex(Utils.to_peb(1.5))

        _, error = self.send_transaction({"from": sender, "to": to, "value": value}, password)
        self.assertIsNone(error)

    def test_personal_sendTransaction_success_no_param5(self):
        sender = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        to = test_data_set["account"]["receiver"]["address"]
        gas = hex(304000)
        value = hex(Utils.to_peb(1.5))

        _, error = self.send_transaction({"from": sender, "to": to, "gas": gas, "value": value}, password)
        self.assertIsNone(error)

    def test_personal_sendTransaction_error_wrong_type_param1(self):
        password = test_data_set["account"]["sender"]["password"]
        to = test_data_set["account"]["receiver"]["address"]
        gas = hex(304000)
        gas_price = test_data_set["unitGasPrice"]
        value = hex(Utils.to_peb(1.5))

        _, error = self.send_transaction(
            {"from": 1234, "to": to, "gas": gas, "gasPrice": gas_price, "value": value},
            password,
        )
        Utils.check_error(self, "arg0NonstringToSendTxArgsFromAddress", error)

    def test_personal_sendTransaction_error_wrong_type_param2(self):
        sender = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        gas = hex(304000)
        gas_price = test_data_set["unitGasPrice"]
        value = hex(Utils.to_peb(1.5))

        _, error = self.send_transaction(
            {
                "from": sender,
                "to": 1234,
                "gas": gas,
                "gasPrice": gas_price,
                "value": value,
            },
            password,
        )
        Utils.check_error(self, "arg0NonstringToSendTxArgsToAddress", error)

    def test_personal_sendTransaction_error_wrong_type_param3(self):
        sender = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        to = test_data_set["account"]["receiver"]["address"]
        gas_price = test_data_set["unitGasPrice"]
        value = hex(Utils.to_peb(1.5))

        _, error = self.send_transaction(
            {
                "from": sender,
                "to": to,
                "gas": 1234,
                "gasPrice": gas_price,
                "value": value,
            },
            password,
        )
        Utils.check_error(self, "arg0NonstringToSendTxArgsGasUint", error)

    def test_personal_sendTransaction_error_wrong_type_param4(self):
        sender = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        to = test_data_set["account"]["receiver"]["address"]
        gas = hex(304000)
        value = hex(Utils.to_peb(1.5))

        _, error = self.send_transaction(
            {"from": sender, "to": to, "gas": gas, "gasPrice": 1234, "value": value},
            password,
        )
        Utils.check_error(self, "arg0NonstringToSendTxArgsGaspriceBig", error)

    def test_personal_sendTransaction_error_wrong_type_param5(self):
        sender = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        to = test_data_set["account"]["receiver"]["address"]
        gas = hex(304000)
        gas_price = test_data_set["unitGasPrice"]

        _, error = self.send_transaction(
            {
                "from": sender,
                "to": to,
                "gas": gas,
                "gasPrice": gas_price,
                "value": 1234,
            },
            password,
        )
        Utils.check_error(self, "arg0NonstringToSendTxArgsValueBig", error)

    def test_personal_sendTransaction_error_wrong_type_param6(self):
        sender = test_data_set["account"]["sender"]["address"]
        to = test_data_set["account"]["receiver"]["address"]
        gas = hex(304000)
        gas_price = test_data_set["unitGasPrice"]
        value = hex(Utils.to_peb(1.5))

        _, error = self.send_transaction(
            {
                "from": sender,
                "to": to,
                "gas": gas,
                "gasPrice": gas_price,
                "value": value,
            },
            1234,
        )
        Utils.check_error(self, "arg1NumberToString", error)

    def test_personal_sendTransaction_error_wrong_value_param1(self):
        sender = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        to = test_data_set["account"]["receiver"]["address"]
        gas = hex(304000)
        gas_price = test_data_set["unitGasPrice"]
        value = hex(Utils.to_peb(1.5))

        _, error = self.send_transaction(
            {
                "from": sender + "1",
                "to": to,
                "gas": gas,
                "gasPrice": gas_price,
                "value": value,
            },
            password,
        )
        Utils.check_error(self, "arg0HexToSendTxArgsFromAddress", error)

    def test_personal_sendTransaction_error_wrong_value_param2(self):
        sender = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        to = test_data_set["account"]["receiver"]["address"]
        gas = hex(304000)
        gas_price = test_data_set["unitGasPrice"]
        value = hex(Utils.to_peb(1.5))

        _, error = self.send_transaction(
            {
                "from": sender,
                "to": to + "1",
                "gas": gas,
                "gasPrice": gas_price,
                "value": value,
            },
            password,
        )
        Utils.check_error(self, "arg0HexToSendTxArgsToAddress", error)

    def test_personal_sendTransaction_error_wrong_value_param3(self):
        sender = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        to = test_data_set["account"]["receiver"]["address"]
        gas = hex(30)
        gas_price = test_data_set["unitGasPrice"]
        value = hex(Utils.to_peb(1.5))

        _, error = self.send_transaction(
            {
                "from": sender,
                "to": to,
                "gas": gas,
                "gasPrice": gas_price,
                "value": value,
            },
            password,
        )
        Utils.check_error(self, "GasTooLow", error)

    def test_personal_sendTransaction_error_wrong_value_param4(self):
        sender = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        to = test_data_set["account"]["receiver"]["address"]
        gas = hex(304000)
        gas_price = hex(25)
        value = hex(Utils.to_peb(1.5))

        _, error = self.send_transaction(
            {
                "from": sender,
                "to": to,
                "gas": gas,
                "gasPrice": gas_price,
                "value": value,
            },
            password,
        )
        Utils.check_error(self, "InvalidGasPrice", error)

    def test_personal_sendTransaction_error_wrong_value_param5(self):
        to = test_data_set["account"]["receiver"]["address"]
        gas = hex(304000)
        gas_price = test_data_set["unitGasPrice"]
        value = hex(Utils.to_peb(1.5))

        method = f"{self.ns}_newAccount"
        result, error = Utils.call_rpc(self.endpoint, method, [""], self.log_path)
        self.assertIsNone(error)
        new_account_address = result

        _, error = self.send_transaction(
            {
                "from": new_account_address,
                "to": to,
                "gas": gas,
                "gasPrice": gas_price,
                "value": value,
            },
            "",
        )
        Utils.check_error(self, "InsufficientFundsFrom", error)

    def test_personal_sendTransaction_success(self):
        sender = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        to = test_data_set["account"]["receiver"]["address"]
        gas = hex(304000)
        gas_price = test_data_set["unitGasPrice"]
        value = hex(Utils.to_peb(1.5))

        _, error = self.send_transaction(
            {
                "from": sender,
                "to": to,
                "gas": gas,
                "gasPrice": gas_price,
                "value": value,
            },
            password,
        )
        self.assertIsNone(error)

    def sign(self, message=None, signer=None, password=None):
        params = list()
        if message is not None:
            params.append(message)
        if signer is not None:
            params.append(signer)
        if password is not None:
            params.append(password)

        result, error = Utils.call_rpc(self.endpoint, f"{self.ns}_sign", params, self.log_path)
        return result, error

    def test_personal_sign_error_no_param(self):
        _, error = self.sign()
        Utils.check_error(self, "arg0NoParams", error)

    def test_personal_sign_error_wrong_type_param1(self):
        sender = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        _, error = self.sign("message", sender, password)
        Utils.check_error(self, "arg0HexToBytes", error)

    def test_personal_sign_error_wrong_type_param2(self):
        message = Utils.convert_to_hex("Hi Utils!")
        password = test_data_set["account"]["sender"]["password"]
        _, error = self.sign(message, "sender", password)
        Utils.check_error(self, "arg1HexToAddress", error)

    def test_personal_sign_error_wrong_type_param3(self):
        message = Utils.convert_to_hex("Hi Utils!")
        sender = test_data_set["account"]["sender"]["address"]
        _, error = self.sign(message, sender, 1234)
        Utils.check_error(self, "arg2NumberToString", error)

    def test_personal_sign_error_wrong_value_param(self):
        message = Utils.convert_to_hex("Hi Utils!")
        sender = test_data_set["account"]["sender"]["address"]
        _, error = self.sign(message, sender, "abcd")
        Utils.check_error(self, "CouldntDecryptKey", error)

    def test_personal_sign_success(self):
        message = Utils.convert_to_hex("Hi Utils!")
        sender = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        _, error = self.sign(message, sender, password)
        self.assertIsNone(error)

    def test_personal_ecRecover_error_no_param(self):
        method = f"{self.ns}_ecRecover"
        _, error = Utils.call_rpc(self.endpoint, method, [], self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_personal_ecRecover_error_wrong_type_param1(self):
        method = f"{self.ns}_ecRecover"
        message = Utils.convert_to_hex("Hi Utils!")
        _, error = Utils.call_rpc(self.endpoint, method, [message, 1234], self.log_path)
        Utils.check_error(self, "arg1NonstringToBytes", error)

    def test_personal_ecRecover_error_wrong_type_param2(self):
        method = f"{self.ns}_ecRecover"
        message = Utils.convert_to_hex("Hi Utils!")
        _, error = Utils.call_rpc(self.endpoint, method, [message, "abcd"], self.log_path)
        Utils.check_error(self, "arg1HexToBytes", error)

    def test_personal_ecRecover_error_wrong_value_param(self):
        message = Utils.convert_to_hex("Hi Utils!")
        signer = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        signature, error = self.sign(message, signer, password)
        self.assertIsNone(error)
        invalid_signature = signature[:-3] + "fff"

        method = f"{self.ns}_ecRecover"
        _, error = Utils.call_rpc(self.endpoint, method, [message, invalid_signature], self.log_path)
        Utils.check_error(self, "InvalidKlaytnSignature", error)

    def test_personal_ecRecover_success(self):
        message = Utils.convert_to_hex("Hi Utils!")
        signer = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        signature, error = self.sign(message, signer, password)
        self.assertIsNone(error)

        method = f"{self.ns}_ecRecover"
        result, error = Utils.call_rpc(self.endpoint, method, [message, signature], self.log_path)
        self.assertIsNone(error)
        recovered = result
        self.assertEqual(signer.lower(), recovered.lower())

    @staticmethod
    def suite():
        suite = unittest.TestSuite()
        suite.addTest(TestPersonalNamespaceRPC("test_personal_importRawKey_error_no_param1"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_importRawKey_error_no_param2"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_importRawKey_error_wrong_type_param1"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_importRawKey_error_wrong_type_param2"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_importRawKey_error_wrong_value_param1"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_importRawKey_success"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_listAccounts_success_wrong_value_param"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_listAccounts_success"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_lockAccount_error_no_param"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_lockAccount_error_wrong_type_param1"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_lockAccount_error_wrong_type_param2"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_lockAccount_success"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_unlockAccount_error_no_param1"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_unlockAccount_error_no_param2"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_unlockAccount_error_wrong_type_param1"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_unlockAccount_error_wrong_type_param2"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_unlockAccount_error_wrong_type_param3"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_unlockAccount_error_wrong_value_param"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_unlockAccount_success_no_duration"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_unlockAccount_success"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_newAccount_error_no_param"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_newAccount_error_wrong_type_param"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_newAccount_success"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_sendTransaction_error_no_param1"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_sendTransaction_error_no_param2"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_sendTransaction_error_no_param3"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_sendTransaction_error_no_param4"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_sendTransaction_error_no_param5"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_sendTransaction_error_no_param6"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_sendTransaction_success_no_param1"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_sendTransaction_success_no_param2"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_sendTransaction_success_no_param3"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_sendTransaction_success_no_param4"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_sendTransaction_success_no_param5"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_sendTransaction_error_wrong_type_param1"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_sendTransaction_error_wrong_type_param2"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_sendTransaction_error_wrong_type_param3"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_sendTransaction_error_wrong_type_param4"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_sendTransaction_error_wrong_type_param5"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_sendTransaction_error_wrong_type_param6"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_sendTransaction_error_wrong_value_param1"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_sendTransaction_error_wrong_value_param2"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_sendTransaction_error_wrong_value_param3"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_sendTransaction_error_wrong_value_param4"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_sendTransaction_error_wrong_value_param5"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_sendTransaction_success"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_sign_error_no_param"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_sign_error_wrong_type_param1"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_sign_error_wrong_type_param2"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_sign_error_wrong_type_param3"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_sign_error_wrong_value_param"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_sign_success"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_ecRecover_error_no_param"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_ecRecover_error_wrong_type_param1"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_ecRecover_error_wrong_type_param2"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_ecRecover_error_wrong_value_param"))
        suite.addTest(TestPersonalNamespaceRPC("test_personal_ecRecover_success"))

        return suite
