import binascii
import bip32utils
import secrets
from mnemonic import Mnemonic
from colorama import Fore, Back, init
import os
import blockcypher
from moneywagon import AddressBalance

# Все импорты
init()


# Если что я никого не принуждаю это делать я это сделал чисто для того что бы проверить себя, и дать ознакомится
# другим, что бы понимали как это работает


# ....................Создатель......................#

# ███╗░░░███╗░█████╗░██████╗░░█████╗░██╗░░░██╗░██████╗
# ████╗░████║██╔══██╗██╔══██╗██╔══██╗██║░░░██║██╔════╝
# ██╔████╔██║███████║██████╔╝██║░░╚═╝██║░░░██║╚█████╗░
# ██║╚██╔╝██║██╔══██║██╔══██╗██║░░██╗██║░░░██║░╚═══██╗
# ██║░╚═╝░██║██║░░██║██║░░██║╚█████╔╝╚██████╔╝██████╔╝
# ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═════╝░


def check_balance(address):
    try:
        total = blockcypher.get_total_balance(address)
        return float(total)
    except:
        total = AddressBalance().action('btc', address)
        return float(total)


def bip39(mnemonic_words):
    ##########################
    seed = Mnemonic("english").to_seed(mnemonic_words)
    bip32_root_key_obj = bip32utils.BIP32Key.fromEntropy(seed)
    bip32_child_key_obj = bip32_root_key_obj.ChildKey(44 + bip32utils.BIP32_HARDEN) \
        .ChildKey(0 + bip32utils.BIP32_HARDEN).ChildKey(0 + bip32utils.BIP32_HARDEN) \
        .ChildKey(0).ChildKey(0)
    ##########################
    # Генерирует мнемоническую фразу и делает из нее приват ключ

    #############################ПЕРЕМЕННЫЕ#################################
    ######################################################################
    address = bip32_child_key_obj.Address()  # Из мнемонической фразы генерирует адрес
    balance = check_balance(address)
    public_Key = binascii.hexlify(bip32_child_key_obj.PublicKey()).decode()  # Переменная где хранится public key
    private_Key = bip32_child_key_obj.WalletImportFormat()  # Переменная где хранится private key
    ######################################################################

    if balance is isinstance(balance,
                             float) and balance > 0.000000000001:  # проверянет если balance флоат и если баланс >0.00...1
        with open("goods.txt", "w+") as my_file:  # И если да то записывает в файл goods.txt
            my_file.write(f"Address: {address};"
                          f" Seed: {mnemonic_words};"
                          f" Public Key: {public_Key};"
                          f" Private Key: {private_Key};"
                          f" BTC:{balance}")
        return f"{Back.YELLOW}{Fore.WHITE}Address: {Fore.CYAN}{address} {Fore.GREEN}| {Fore.RED}BTC: {balance}"  # Если есть битки то делает текст подствеченным
    else:
        return f"{Fore.WHITE}Address: {Fore.CYAN}{address} {Fore.GREEN} | {Fore.RED}BTC: {balance}"  # а если нету то такой какой есть цвет


def start():
    i = 0  # Подсчет колво проверок
    while True:  # Вечный цикл
        seed_phrase24 = Mnemonic("english").to_mnemonic(
            secrets.token_bytes(24))  # Создает сид фразу тут можете настраивать сколько будет слов подбиратся
        print(f"[{i}]", bip39(seed_phrase24))  # Выводин на экран и делает выше функцию
        i += 1  # прибавляет к i + 1


######################Я думаю тут объяснять не надо


print("\t\t\t░█▀▄▀█ ─█▀▀█ ░█▀▀█ ░█▀▀█ ░█─░█ ░█▀▀▀█")
print("\t\t\t░█░█░█ ░█▄▄█ ░█▄▄▀ ░█─── ░█─░█ ─▀▀▀▄▄")
print("\t\t\t░█──░█ ░█─░█ ░█─░█ ░█▄▄█ ─▀▄▄▀ ░█▄▄▄█\n")

print(
    Fore.GREEN + f"\t\t\t\tПриветствую!{Fore.RESET}\n"
                 f"\t\tДанная программа была написана программистом {Fore.RED}MARCUS{Fore.RESET}\n")

a = input("Что вы хотите майнить?(BTC, ETH): ")
if (a.lower() == "btc"):
    start()
elif (a.lower() == "eth"):
    os.system('python eth.py')
