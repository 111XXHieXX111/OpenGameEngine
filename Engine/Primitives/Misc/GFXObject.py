_used_ids = set()

def generate_id():
    i = 0
    while i in _used_ids:
        i += 1
    _used_ids.add(i)
    return i

def delete_id(id):
    _used_ids.discard(id)

class GFXObject:
    def InitObject(self):
        self.id = generate_id()

    def __del__(self):
        delete_id(self.id)
