# python protocols demo

class ExampleMappingType(object):
    def __init__(self):
        self._dataStore = {}

    def __getitem__(self, k):
        v = self._dataStore[k]
        print('Fetching: %s, Value is: %s'%(k, v))
        return v

    def __setitem__(self, k, v):
        print('Setting: %s to %s'%(k, v))
        self._dataStore[k] = v

    def __delitem__(self, k):
        print('Deleting: %s'%k)
        del self._dataStore[k]


mapping = ExampleMappingType()
mapping['key1'] = 'value1'

x = mapping['key1']

print(x)

del mapping['key1']