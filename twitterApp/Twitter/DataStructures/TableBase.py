import pickle as pk

from twitterApp.Twitter.DataStructures.Tables.Table import Table


class TableBase:

    FILE_NAME='TABLE'

    def __init__(self):
        self.users = Table()
        self.tweets = Table()

    def save_table(self):
        pk.dump(self, open(self.FILE_NAME, 'wb'))

    def load_table(self):
        self.__dict__ = pk.load(open(self.FILE_NAME, 'rb')).__dict__
