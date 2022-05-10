from utils import Utils

_, _, log_path = Utils.get_log_filename_with_path()


def send_transaction(endpoint, params):
    transaction_hash, error = Utils.call_rpc(endpoint, "klay_sendTransaction", params, log_path)
    return transaction_hash, error


def get_transaction(endpoint, params):
    transaction, error = Utils.call_rpc(endpoint, "klay_getTransactionByHash", params, log_path)
    return transaction, error


def get_transaction_receipt(endpoint, params):
    receipt, error = Utils.call_rpc(endpoint, "klay_getTransactionReceipt", params, log_path)
    return receipt, error


def get_latest_block_by_number(endpoint):
    method = "klay_getBlockByNumber"
    latest_block, _ = Utils.call_rpc(endpoint, method, ["latest", True], log_path)
    return latest_block


def get_block_number(endpoint):
    method = "klay_blockNumber"
    block_number, _ = Utils.call_rpc(endpoint, method, ["latest", True], log_path)
    return block_number
