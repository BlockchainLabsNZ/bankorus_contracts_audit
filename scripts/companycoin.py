import logging
import json
from web3 import Web3, HTTPProvider

from utils import settings, wallet

logger = logging.getLogger(__name__)


class CompanyCoin:
    def __init__(self, rpcpoint, smart_contract_address, abi, decimals=18, key=None):
        self.endpoint = Web3(HTTPProvider(rpcpoint))
        self.smart_contract = self.endpoint.eth.contract(address=smart_contract_address, abi=abi)
        self.decimals = decimals
        self.key = key
        self.nonce = self.endpoint.eth.getTransactionCount(settings.CONTRACT_HOLDER_ADDRESS, 'pending')
        # todo
        # nonce:This is a very bad way to do it.
        # 0 rpc result is not correct curl -X POST --data '{"jsonrpc":"2.0","method":"eth_getTransactionCount","params":["0x63a2A811B697D0440272a6e13181200327E61521","pending"],"id":1}' https://ropsten.infura.io
        # 1 self.endpoint.eth.getTransactionCount(settings.CONTRACT_HOLDER_ADDRESS, 'pending') result is not correct
        # 2 nonce need a share store,for example redis

    def balance(self, account):
        value = self.smart_contract.call().balanceOf(account)
        return value / self._base_unit()

    # @property
    # def balance_of_base_account(self):
    #     return self.balance(self.endpoint.eth.coinbase)  # if remote endpoint will raise error,so pls use self.balance

    def _base_unit(self):
        return 10 ** self.decimals

    def transfer(self, to_address, value):
        """

        :param to_address:
        :param value:how many tokin
        :param from_address:
        :return:
        """
        if not Web3.isAddress(to_address):
            raise ValueError('%s is not a valid address' % to_address)
        value = int(value * self._base_unit())
        return self._sign_transaction('transfer', (to_address, value))

    # def lock_account(self, is_lock=True):
    #     return self._sign_transaction('changeTag', (is_lock,))

    def _sign_transaction(self, function_name, args=None):
        """

        :param function_name:
        :param args:
        :return:

        replacement transcation:
        replacement transaction underpriced
        have pending transaction now:
        ValueError: {'code': -32000, 'message': 'known transaction:'}
        gas error:
        1.not setting gas: gas required exceeds allowance or always failing transaction'
        2.self.endpoint.eth.getBlock('latest')['gasLimit']:The GAS for this Txn exceeds the Avg GasLimit of 4,711,908 for the last 50 Blocks
        """
        init_params = {
            'from': settings.CONTRACT_HOLDER_ADDRESS,
            'nonce': self.nonce,
            # include pending
            "gas": 4512394,  # self.endpoint.eth.getBlock('latest')['gasLimit'],  # >21000 and <gasLimit

        }
        obj = self.smart_contract.buildTransaction(init_params)
        if args:
            tx = getattr(obj, function_name)(*args)
        else:
            tx = getattr(obj, function_name)()
        signed = self.endpoint.eth.account.signTransaction(tx, self.key)
        txn_hash = self.endpoint.toHex(self.endpoint.eth.sendRawTransaction(signed.rawTransaction))
        self.nonce += 1
        return txn_hash

    def transfer_to_addresses(self, addresss, values):
        assert len(addresss) == len(values)
        assert all(map(Web3.isAddress, addresss))
        values = list(map(lambda value: int(value * self._base_unit()), values))
        return self._sign_transaction('transferToAddresses', (addresss, values))

    def set_transaction_count_limit(self, limit=50):
        return self._sign_transaction('setArrayLimit', (limit,))

    def get_transaction(self, hash_id):
        return self.endpoint.eth.getTransaction(hash_id)

    @classmethod
    def get_client(cls, key=None):
        abi_str = settings.CONTRACT_ABI
        contract = CompanyCoin(settings.CONTRACT_HTTP_SERVICE,
                               smart_contract_address=settings.CONTRACT_ADDRESS,
                               abi=json.loads(abi_str), key=key)
        return contract


if __name__ == "__main__":
    password = 'Micai1234'  # FOR TEST
    wallet_file_path = '../data/keystore-test'  # FOR TEST
    private_key = wallet.get_wallet_key(password, wallet_file_path)
    client = CompanyCoin.get_client(key=private_key)

    # print(client.transfer(to_address='0xD9B8B44Cc2D153A0052Ce7D0A7a450DFe893e066', value=2))
    addresses = ['0xD9B8B44Cc2D153A0052Ce7D0A7a450DFe893e066']
    # addresses_len = 100  # replacement transaction underpriced

    client.set_transaction_count_limit(100)
    addresses_len = 20  # ok
    # hash_id = client.transfer_to_addresses(addresses * addresses_len, [2] * addresses_len)

    for i in range(5):
        hash_id = client.transfer_to_addresses(addresses * addresses_len, [2] * addresses_len)
        print(hash_id)
