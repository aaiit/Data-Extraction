class Table:

    def __init__(self):
        self.table = {}

    def add_row(self, id: str, row):
        assert isinstance(row, dict)
        self.table[id] = row

    def __contains__(self, id):
        return id in self.table

    def get_row(self, id):
        try:
            return self.table[id]
        except Exception:
            return {}

    def __getitem__(self, key):
        '''
        Get all the values of the attribute 'item'.
        :param key: attribute.
        :return: dictionary: id,value for every user.
        '''
        return {k: v[key] for k, v in self.table.items()}
