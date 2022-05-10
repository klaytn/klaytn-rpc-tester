from utils import Utils

_, _, log_path = Utils.get_log_filename_with_path()


def net_peerCount(endpoint):
    result, _ = Utils.call_rpc(endpoint, "net_peerCount", [], log_path)
    return result
