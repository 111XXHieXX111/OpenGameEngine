from .crypto import encryptData, decryptData
from ..Kernel.modules import json
from ..Kernel.kernel import logWrapper, log_system

@logWrapper
def saveData(path:str, data, key:str):
    log_system.addInfo("Saving data")
    json_str = json.dumps(data)
    encrypted = encryptData(json_str.encode(), key)
    with open(path, "wb+") as f:
        f.write(encrypted)

@logWrapper
def loadData(path:str, key:str):
    log_system.addInfo("Loading data")
    with open(path, "rb") as f:
        data = f.read()
    decrypted = decryptData(data, key)
    return json.loads(decrypted)
