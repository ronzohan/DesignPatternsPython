from datetime import timedelta
from datetime import datetime
import pickle


class Cache(object):
    def __init__(self, filename):
        self.filename = filename

    def save(self, obj):
        with open(self.filename, 'w') as file:
            dct = {'obj': obj,
                   'expired': datetime.utcnow() + timedelta(hours=3)
                   }
            pickle.dump(dct, file)

    def load(self):
        try:
            with open(self.filename) as file:
                result = pickle.load(file)
                if result['expired'] > datetime.utcnow():
                    return result['obj']
        except IOError:
            pass
