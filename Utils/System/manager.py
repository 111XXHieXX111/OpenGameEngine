class Manager:
    def _find(self, name):
        for index, obj in enumerate(self.objs):
            if obj[0] == name:
                return index, obj[1]
        return None, None