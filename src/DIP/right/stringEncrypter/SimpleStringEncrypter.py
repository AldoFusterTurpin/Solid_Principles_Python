from src.DIP.right.stringEncrypter.IStringEncrypter import IStringEncrypter


class SimpleStringEncrypter(IStringEncrypter):
    def encryptString(self, toEncrypt: str) -> str:
        encrypted_list = []
        toEncryptLength = len(toEncrypt)

        for i in toEncrypt:
            encoded_char = i + str(toEncryptLength)
            encrypted_list.append(encoded_char)

        return "".join(encrypted_list)