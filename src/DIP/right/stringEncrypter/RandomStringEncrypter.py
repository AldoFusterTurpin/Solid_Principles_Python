from src.DIP.right.stringEncrypter.IStringEncrypter import IStringEncrypter
import random

class RandomStringEncrypter(IStringEncrypter):
    def encryptString(self, toEncrypt: str) -> str:
        encrypted_list = []
        toEncryptLength = len(toEncrypt)

        for char in toEncrypt:
            random_num = random.randint(0, toEncryptLength)
            encoded_char = char + str(random_num)
            encrypted_list.append(encoded_char)

        return "".join(encrypted_list)