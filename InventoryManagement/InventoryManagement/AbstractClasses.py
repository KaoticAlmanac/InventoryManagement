import abc
#
class IInventory:
    __metaclass__ = abc.ABCMeta
    
    OurInventory = dict()
    @abc.abstractmethod
    def hash(self):
        self.name
    @abc.abstractmethod
    def insert(self,item):
        if isinstance(item,IItem):
            print "Not yet instantiated"
        else:
            print "Err not using Item"

     

class IItem:#Abstract class for items, all created items must be based on this class
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod 
    def __init__(self,name,**kwargs):
        self.name = name
        for key in kwargs:
            self.key = kwargs

    @abc.abstractmethod
    def hash(self):
        self.name
class Inventory(IInventory):
    OurInventory
    def __init__(self):
        self.OurInventory=dict()
        return
    
    def hash(self):
        super().hash()
    def insert(self, item):
        hold = {item.name,item}
        self.OurInventory.update(hold)
