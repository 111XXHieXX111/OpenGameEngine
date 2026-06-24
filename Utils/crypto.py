from ..Core.modules import Fernet

def encryptData(data, key:str):
    fernet = Fernet(key.encode() if isinstance(key, str) else key)
    if isinstance(data, str):
        data = data.encode()
    return fernet.encrypt(data)

def decryptData(encrypted:bytes, key:str):
    fernet = Fernet(key.encode() if isinstance(key, str) else key)
    decrypted = fernet.decrypt(encrypted)
    return decrypted.decode()

def genKey():
    return Fernet.generate_key().decode()
