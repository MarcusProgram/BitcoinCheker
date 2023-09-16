import blocksmith
from eth_keys import keys
from eth_utils import decode_hex
import pyetherbalance
from colorama import Fore, Back

# Все импорты


#Если что я никого не принуждаю это делать я это сделал чисто для того что бы проверить себя, и дать ознакомится
#другим, что бы понимали как это работает


#....................Создатель......................#

#███╗░░░███╗░█████╗░██████╗░░█████╗░██╗░░░██╗░██████╗
#████╗░████║██╔══██╗██╔══██╗██╔══██╗██║░░░██║██╔════╝
#██╔████╔██║███████║██████╔╝██║░░╚═╝██║░░░██║╚█████╗░
#██║╚██╔╝██║██╔══██║██╔══██╗██║░░██╗██║░░░██║░╚═══██╗
#██║░╚═╝░██║██║░░██║██║░░██║╚█████╔╝╚██████╔╝██████╔╝
#╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═════╝░

def generate_public_key(private_key):
    priv_key_bytes = decode_hex(private_key)
    priv_key = keys.PrivateKey(priv_key_bytes)
    pub_key = priv_key.public_key
    return pub_key
def check_balance_print(address,key):
    infura_url = 'https://mainnet.infura.io/v3/eec9b42b403f4a3aad1099940d4abe36'
    ethbalance = pyetherbalance.PyEtherBalance(infura_url)
    balance_eth = ethbalance.get_eth_balance(address)
    if balance_eth['balance'] > 0.000000000001:
        with open("goods.txt", "w+") as my_file:
            my_file.write(f"Address: {address};"
                          f" Public Key: {generate_public_key(key)};"
                          f" Private Key: {key};"
                          f" ETH:{balance_eth['balance']}")
        print(f"{Back.YELLOW}{Fore.WHITE}Address: {Fore.CYAN}{address} {Fore.GREEN}| {Fore.RED}ETH: {balance_eth['balance']}")  # Если есть eth то делает текст подствеченным
    else:
        print(f"{Fore.WHITE}Address: {Fore.CYAN}{address} {Fore.GREEN} | {Fore.RED}ETH: {balance_eth['balance']}")  # а если нету то такой какой есть цвет


def generate_address(key):
    address = blocksmith.EthereumWallet.generate_address(key)
    check_balance_print(address,key)
    return address

def generate_private_key():
    private_key= blocksmith.KeyGenerator()
    private_key.seed_input('kdktrkkfee')
    key = private_key.generate_key()
    generate_address(key)
    generate_public_key(key)
    return key

def start():
    i = 0 # Подсчет колво проверок
    while True: #Вечный цикл
        print(f"[{i}]", generate_private_key()) #Выводин на экран и делает выше функцию
        i += 1  # прибавляет к i + 1
start()