class myDict(object):
    """ Implements a dictionary without using a dictionary """
    def __init__(self):
        """ initialization of your representation """
        #FILL THIS IN
        self.keys = []
        self.values = []
        
    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        #FILL THIS IN
        if k not in self.keys:
            self.keys.append(k)
            self.values.append(v)
        else:
            self.values[self.keys.index(k)] = v
        
    def getval(self, k):
        """ k, immutable object  """
        #FILL THIS IN
        try:
            return self.values[self.keys.index(k)]
        except:
            raise KeyError
        
    def delete(self, k):
        """ k, immutable object """   
        #FILL THIS IN
        try:
            self.values.pop(self.keys.index(k))
            self.keys.remove(k)
        except:
            raise KeyError