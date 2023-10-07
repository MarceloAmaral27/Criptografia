def show_options(*args):
    """ Exibe as opções de criptografia.
    Args:
        args (tuple): Uma tupla de textos a serem exibidas como opções de criptografia.
    """
    print('Escolha uma das opções de criptografia abaixo:')
    for i, option in enumerate(args, start=1):
        print(f'[{i}] {option}')

def displacement(displacement):
    """
    Configura a cifra de César com o valor de deslocamento fornecido.

    Args:
        displacement (int): O valor de deslocamento a ser usado na cifra de César.

    Returns:
        function (caesar_cipher): Uma função que recebe uma string de entrada do usuário e retorna o texto criptografado usando a cifra de César.
    """
    def caesar_cipher(user_input):
        """
        Criptografa uma string fornecida usando a técnica da cifra de César com o deslocamento especificado.

        Args:
            user_input (str): A string de entrada a ser criptografada.

        Returns:
            str: A string criptografada.
        """
        encrypted = ''
        for letter in user_input:
            if letter.isalpha():
                shifting = ord(letter) + displacement
                encrypted += chr(shifting)

        return encrypted

    return caesar_cipher


def decipher_cesar(ciphertext, displacement):
    """Descriptografa um texto cifrado usando a Cifra de César com um valor de deslocamento específico.

    Args:
        ciphertext (str): O texto cifrado a ser descriptografado.
        displacement (_type_): O valor de deslocamento usado na Cifra de César durante a criptografia.

    Returns:
        str: O texto original descriptografado.
    """
    encrypted = ""
    for letter in ciphertext:
        if letter.isalpha():
            shifting = ord(letter) - displacement
            encrypted += chr(shifting)

    return encrypted
