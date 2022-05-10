from utils import Utils

_, _, log_path = Utils.get_log_filename_with_path()


def send_transaction(endpoint, params):
    method = "personal_sendTransaction"
    transaction_hash, error = Utils.call_rpc(endpoint, method, params, log_path)
    return transaction_hash, error


def import_rawkey(endpiont, params):
    method = "personal_importRawKey"
    _, error = Utils.call_rpc(endpiont, method, params, log_path)
    return error


def unlock_account(endpoint, params):
    method = "personal_unlockAccount"
    _, error = Utils.call_rpc(endpoint, method, params, log_path)
    return error
