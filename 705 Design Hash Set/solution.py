'''
class MyHashSet(object):

    def __init__(self):
        self.l=[]
        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.l.append(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.l:
            self.l.remove(key)
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return key in self.l
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
'''


class MyHashSet(object):
    # initialize an empty array
    def __init__(self):
        self.l = []
    # if the element does not exist, add it

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.l.append(key)
    # if the element exists remove it

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.l:
            self.l.remove(key)

    # return true if element exists in the set
    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return key in self.l


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
