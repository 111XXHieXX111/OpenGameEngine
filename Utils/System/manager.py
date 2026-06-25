class Manager:
    def _find(self, name):
        for index, obj in enumerate(self.objs):
            if obj[0] == name:
                return index, obj
        return None, None