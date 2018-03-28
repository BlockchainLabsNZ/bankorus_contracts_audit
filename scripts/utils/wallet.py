import logging
from web3 import Web3
from eth_keyfile import extract_key_from_keyfile

logger = logging.getLogger(__name__)


def get_wallet_key(password, wallet_file_path):
    """
    use password get private key
    :param password:
    :param wallet_file_path:
    :return:
    """
    try:
        key = Web3.toHex(
            extract_key_from_keyfile(wallet_file_path, Web3.toBytes(text=password)))[2:]
    except Exception as e:
        logging.error('password mistake %s', password)
        key = None
    return key
