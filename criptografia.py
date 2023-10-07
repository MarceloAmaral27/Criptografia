from hashlib import sha256
from time import sleep
from cryptography_utils import *

while True:
    # Exibe as opções de criptografia
    show_options('Cifra de Cesar', 'Decifrar Cifra de Cesar', 'Sha256', 'Sair')
    option = str(input('Selecione a opção desejada: ')).strip()

    if option == '1':
        # Criptografa usando a cifra de César com deslocamento de 3
        user_input = str(input('Insira uma palavra ou frase que deseja criptografar: '))
        internal_function = displacement(3)
        encrypted = internal_function(user_input)
        print(f'Texto Original: {user_input}')
        print(f'Texto Criptografado: {encrypted}')

    if option == '2':
        # Descriptografa usando a Cifra de César com deslocamento de 3
        decrypt = str(input('Palavra ou frase que deseja descriptografar: '))
        decrypt = decipher_cesar(decrypt, 3)
        print(f'Texto descriptografado: {decrypt}')

    if option == '3':
        # Criptografa usando a criptografia SHA256
        user_text = str(input('Insira uma palavra ou frase que deseja criptografar: '))
        hash_hex = sha256(user_text.encode()).hexdigest()
        print(f'Texto Original: {user_text}')
        print(f'Texto Criptografado: {hash_hex}')

    elif option > '4':
        print('Opção inválida! Por favor, escolha uma opção válida.')
        break

    elif option == '4':
        break

    print('='*40)
    sleep(2)
