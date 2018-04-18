import logging
import json
from web3 import Web3, HTTPProvider

from utils import settings, wallet

logger = logging.getLogger(__name__)


class CompanyCoin:
    def __init__(self, rpcpoint, smart_contract_address, abi, passphrase, decimals=18, ):
        self.endpoint = Web3(HTTPProvider(rpcpoint))
        self.smart_contract = self.endpoint.eth.contract(address=Web3.toChecksumAddress(smart_contract_address),
                                                         abi=abi)
        self.passphrase = passphrase
        unlock = self.endpoint.personal.unlockAccount(settings.CONTRACT_HOLDER_ADDRESS, passphrase)
        if not unlock:
            raise "can't unlock account for {account}".format(account=settings.CONTRACT_HOLDER_ADDRESS)
        self.decimals = decimals

    def balance(self, account):
        value = self.smart_contract.call().balanceOf(Web3.toChecksumAddress(account))
        return value / self._base_unit()

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
        to_address = Web3.toChecksumAddress(to_address)
        value = int(value * self._base_unit())
        return Web3.toHex(
            self.smart_contract.transact({'from': settings.CONTRACT_HOLDER_ADDRESS}).transfer(to_address, value))

    def transfer_to_addresses(self, addresss, values):
        """
        GETH NODE NEED STORE keystore FILE
        :param addresss:
        :param values:
        :return:
        """
        assert len(addresss) == len(values)
        assert all(map(Web3.isAddress, addresss))
        addresss = list(map(Web3.toChecksumAddress, addresss))
        values = list(map(lambda value: int(value * self._base_unit()), values))
        tx = Web3.toHex(
            self.smart_contract.transact({'from': settings.CONTRACT_HOLDER_ADDRESS}).transferToAddresses(addresss,
                                                                                                         values))
        return tx

    def set_transaction_count_limit(self, limit=50):
        return Web3.toHex(self.smart_contract.transact({'from': settings.CONTRACT_HOLDER_ADDRESS}).setArrayLimit(limit))

    def get_transaction_count_limit(self):
        return self.smart_contract.call().arrayLimit()

    def get_transaction(self, hash_id):
        return self.endpoint.eth.getTransaction(hash_id)

    @classmethod
    def get_client(cls, passphrase=None):
        abi_str = settings.CONTRACT_ABI
        contract = CompanyCoin(settings.CONTRACT_HTTP_SERVICE,
                               smart_contract_address=settings.CONTRACT_ADDRESS,
                               abi=json.loads(abi_str), passphrase=passphrase)
        return contract


if __name__ == "__main__":
    password = 'the-passphrase'  # FOR TEST
    client = CompanyCoin.get_client(passphrase=password)

    # count limit
    # print('count limit:%s' % client.get_transaction_count_limit())
    # client.set_transaction_count_limit_no_sign(500)
    # time.sleep(60)
    #
    address_list = list(map(Web3.toChecksumAddress, [i.strip() for i in open('../data/airdrop.csv').readlines()]))

    # print(client.transfer('0xf194ab72d9f9348c3b2e5632284783efe41ce892', 2))
    address = ['0x08206B0eb10751AC289aAE62F250DbDC0314cC18', '0x24Ce57eaC6254d8813E53C2ad15b3a2e780b18Cc',
               '0x2f0F805E35b47Fd0aBE5032E68f552f3bCB7c6BC', '0xFC072b0A3790B33265FC8A15a1A2ba115c024a24',
               '0xE770cebC2050d520C1B4709323aED311F0F32FFA', '0x69A31026616bfE7de8e3dF49E1686CAd65289274',
               '0xe90A1800035603f12D5137DFDEC7E237F5E5898A', '0x67638ec0E75aEc679F0CE55048E48eBa720a9Fff',
               '0x325d24746D9046394Ef1F45FBd52bA9235f1b327', '0x2247eD908DcbBAA24D7795aEe919fA80f4e7a493',
               '0xF7372cB895a54cCBed4d386f035e01569465f7cc', '0xb22d4d63853b396E345c7e72F5bb95707D3Ec502',
               '0x80be00Ed1F1BcE361cD6973e079C1292848386EC', '0xd315f0cE090236a5dD46b6829382cC958a5ED582',
               '0x98814f3B6F646dEB2445D057bcbe0C48F55F0a71', '0xD9343be85CEeebe39eb7fd49320E11A2918661bc',
               '0x7cfEa31E1BA8447b7Df7555Bb680eD09e4Dee56d', '0x29f84b8B458e0001809E49871f73400a27d700c2',
               '0x8FEdFF8e75b56511486d660a8A2C12127ce3359B', '0x5C6C69FFEb3f72f3C7Ba54d8F8fB99f216F8C0cB']
    values = [35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35]
    print(client.transfer_to_addresses(address, values))
    # case 3
    # for i in [100, 150, 200]:
    #     # case per 100
    #     step = i  # client.get_transaction_count_limit()
    #     # gas 100:36149,90:,80:,70:,60:,50:21237,40:21354,30:21563,20:21961,10:23168,5:25556,1:44715:
    #     assert client.get_transaction_count_limit() > step
    #     balance = client.balance(settings.CONTRACT_HOLDER_ADDRESS)
    #     print('from balance: %s' % balance)
    #     if balance > 2 * len(address_list):
    #         for i in range(0, len(address_list), step):
    #             adds = address_list[i:i + step]
    #             hash_id = client.transfer_to_addresses(adds, [2] * len(adds))
    #             print(hash_id)
