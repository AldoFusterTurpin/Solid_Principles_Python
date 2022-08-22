class StringEncrypter:
    def encryptString(self, toEncrypt: str) -> str:
        encrypted_list = []
        toEncryptLength = len(toEncrypt)

        for char in toEncrypt:
            encoded_char = char + str(toEncryptLength)
            encrypted_list.append(encoded_char)

        return "".join(encrypted_list)
