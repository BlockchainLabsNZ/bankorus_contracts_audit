import logging
import json
from web3 import Web3, HTTPProvider
from django.conf import settings

logger = logging.getLogger(__name__)
"""
实现转账(Real time transfer)、
历史交易查询(Transaction history search)
"""


class CompanyCoin:
    NAME = 'BKT'

    def __init__(self, rpcpoint, smart_contract_address, abi, decimals=18, key=None):
        self.endpoint = Web3(HTTPProvider(rpcpoint))
        self.smart_contract = self.endpoint.eth.contract(address=smart_contract_address, abi=abi)
        self.decimals = decimals
        self.key = key

    def balance(self, account):
        value = self.smart_contract.call().balanceOf(account)
        return value / self._base_unit()

    @property
    def balance_of_base_account(self):
        return self.balance(self.endpoint.eth.coinbase)  # if remote endpoint will raise error,so pls use self.balance

    def _base_unit(self):
        return 10 ** self.decimals

    def transfer(self, to_address, value):
        """

        :param to_address:
        :param value:
        :param from_address:
        :return:
        """
        value = int(value * self._base_unit())
        return self._sign_transaction('transfer', (to_address, value))

    def lock_account(self, is_lock=True):
        return self._sign_transaction('changeTag', (is_lock,))

    def _sign_transaction(self, function_name, args=None):
        obj = self.smart_contract.buildTransaction({'from': settings.CONTRACT_HOLDER_ADDRESS,
                                                    'nonce': self.endpoint.eth.getTransactionCount(
                                                        settings.CONTRACT_HOLDER_ADDRESS)})
        if args:
            tx = getattr(obj, function_name)(*args)
        else:
            tx = getattr(obj, function_name)()
        signed = self.endpoint.eth.account.signTransaction(tx, self.key)
        txn_hash = self.endpoint.toHex(self.endpoint.eth.sendRawTransaction(signed.rawTransaction))
        return txn_hash

    @classmethod
    def get_client(cls, key=None):
        abi_str = settings.CONTRACT_ABI
        contract = CompanyCoin(settings.CONTRACT_HTTP_SERVICE,
                           smart_contract_address=settings.CONTRACT_ADDRESS,
                           abi=json.loads(abi_str), key=key)
        return contract


if __name__ == "__main__":
    client = CompanyCoin.get_client()
    print(client.balance_of_base_account)
    # print(coin.balance("0x320547f3f4a66936428602aeB5f76B616DF4a078"))
    # # print(coin.transfer(to_address='0xD9B8B44Cc2D153A0052Ce7D0A7a450DFe893e066',value=999999861))
    # print(coin.balance_of_base_account)
    # print(coin.endpoint.eth.coinbase)

    pass


