from ..System.crypto import encryptData, decryptData
from ...Core.modules import json

def saveData(path:str, data, key:str):
    json_str = json.dumps(data)
    encrypted = encryptData(json_str.encode(), key)
    with open(path, "wb+") as f:
        f.write(encrypted)

def loadData(path:str, key:str):
    with open(path, "rb") as f:
        data = f.read()
    decrypted = decryptData(data, key)
    return json.loads(decrypted)
