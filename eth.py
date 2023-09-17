import blocksmith
from web3 import Web3, HTTPProvider
from eth_keys import keys
from eth_utils import decode_hex
from colorama import Fore, Back, init
from time import sleep
# Все импорты
init()

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
    try:
        provider = HTTPProvider(f'https://mainnet.infura.io/v3/{url}')
        if (provider.is_connected()):
            web3 = Web3(provider)
            address = Web3.to_checksum_address(address)
            balance_wei = web3.eth.get_balance(address)
            balance_eth = web3.from_wei(balance_wei, 'ether')
            if balance_eth> 0.000000000001:
                with open("goods.txt", "w+") as my_file:
                    my_file.write(f"Address: {address};"
                                  f" Public Key: {generate_public_key(key)};"
                                  f" Private Key: {key};"
                                  f" ETH:{balance_eth}")
                print(f"{Back.YELLOW}{Fore.WHITE}Address: {Fore.CYAN}{address} {Fore.GREEN}| {Fore.RED}ETH: {balance_eth}")  # Если есть eth то делает текст подствеченным
            else:
                print(f"{Fore.WHITE}Address: {Fore.CYAN}{address} {Fore.GREEN} | {Fore.RED}ETH: {balance_eth}")  # а если нету то такой какой есть цвет
        else:
            sleep(80)
            start(0)
    except Exception as e:
        print(e)


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

def start(i):
    global url
    url = input("Введите свой mainnet.infura.io код: ")
    #eec9b42b403f4a3aad1099940d4abe36
    while True: #Вечный цикл
        print(f"[{i}]", generate_private_key()) #Выводин на экран и делает выше функцию
        i += 1  # прибавляет к i + 1

start(0)