import math
import random
import pytest





class Node(object):
    #each Node exists as its own component
    def __init__(self, k, d):
        self.key  = k
        self.data = d
        
        
    def __str__(self): 
        return "(" + str(self.key) + "," + repr(self.data) + ")"
    
class Heap(object):
    
    def __init__(self, size):
        #because a heap with size smaller than three cannot posses the heap quality
        #attempts to create heaps of a smaller size will create a heap of size three
        #this ensures that all integers inputed as size will allow for the creation of some heap
        if size < 3:
            #should i add a print statement to tell the client
            size = 3        
        self.__arr = [None] * size          #the underlying heap
        self.__nElems = 0                   #number of elements currently in heap

   
            
    #insert a (key, data) pair into the heap       
    def insert(self,k,d):
        #if the heap is full, False is returned
        if self.__nElems == len(self.__arr): return False
        
        #place new node at the end, push it up into correct position, increment nElems
        self.__arr[self.__nElems] = Node(k,d)
        self.pushUp()
        self.__nElems +=1
        #return true after successfull insertion
        return True
    
    #push up a Node from the bottom of the heap into its proper position
    #by comparing it's key's value with other Nodes' keys' values
    #ensuring that that the heap keeps the minmaxheap quality
    def pushUp(self):
        #check that more than one element is in the heap/ it's possible to push up elements 
        if self.__nElems <= 0: return
        
        #check if the lowest level of the heap is a min level
        if (math.floor(math.log(self.__nElems+1,2)))%2 ==0:
            
            
            #the parent key is the lowest key in the heap on a max level on the
            #path between the newly inserted Node and the root
            #therefore comparing their key values determines whether to continue 
            #pushing up through min levels of max levels
            #check if the last element's key is greater than his parent's key
            if self.__arr[self.__nElems].key > self.__arr[(self.__nElems-1)//2].key:
                #swap them
                temp = self.__arr[(self.__nElems-1)//2]
                self.__arr[(self.__nElems-1)//2] = self.__arr[self.__nElems]
                self.__arr[self.__nElems] = temp
                #continue pushing up the Node through the max levels
                self.__pushUpMax((self.__nElems-1)//2)
                
            else:
                #push up the Nodes through the min levels
                self.__pushUpMin(self.__nElems)
                
        #it's in a max level        
        else:
            
            #the parent key is the highest key in the heap on a min level on the
            #path between the newly inserted Node and the root
            #therefore comparing their key values determines whether to continue 
            #pushing up through min levels of max levels  
            #if key is less than parent's key swap them
            if self.__arr[self.__nElems].key < self.__arr[(self.__nElems-1)//2].key:
                temp = self.__arr[(self.__nElems-1)//2]
                self.__arr[(self.__nElems-1)//2] = self.__arr[self.__nElems]
                self.__arr[self.__nElems] = temp
                #push up the node through min levels
                self.__pushUpMin((self.__nElems-1)//2) 
            
            else:
                #push up the Node through the max levels
                self.__pushUpMax(self.__nElems)
        
    
    #push up a node starting at position cur through the min levels of a minmaxheap   
    #by comparing it's key's value with other Nodes' keys' values
    #ensuring that that the heap keeps the minmaxheap quality    
    def __pushUpMin(self,cur):
        #check if the key being pushed up is at least in the third index of the 
        #the minman heap which means the minmax heap has at least three generations
        #of nodes between and including what's in position cur and the root
        #and check if the node at position cur's key is less than then key in cur's
        #grandparent position in the minmax heap
        if cur >2 and\
           self.__arr[cur].key < self.__arr[((((cur-1)//2)-1)//2)].key:
            
            #swap the node in position cur with grandparent
            temp = self.__arr[((((cur-1)//2)-1)//2)] 
            self.__arr[((((cur-1)//2)-1)//2)] = self.__arr[cur]
            self.__arr[cur] = temp
            #push up what was in position cur through the next min level
            self.__pushUpMin(((((cur-1)//2)-1)//2))
        
    #push up a node starting at position cur through the max levels of a minmaxheap   
    #by comparing it's key's value with other Nodes' keys' values
    #ensuring that that the heap keeps the minmaxheap quality      
    def __pushUpMax(self,cur):
        #check if the key being pushed up is at least in the third index of the 
        #the minman heap which means the minmax heap has at least three generations
        #of nodes between and including what's in position cur and the root
        #and check if the node at position cur's key is less than then key in cur's
        #grandparent position in the minmax heap        
        if cur > 2 and\
           self.__arr[cur].key > self.__arr[((((cur-1)//2)-1)//2)].key:
           
            #swap inserted with grandparent
            temp = self.__arr[((((cur-1)//2)-1)//2)] 
            self.__arr[((((cur-1)//2)-1)//2)] = self.__arr[cur]
            self.__arr[cur] = temp
            #push up what was in position cur through the next max level
            self.__pushUpMax((((cur-1)//2)-1)//2) 
        
    #i should probably remove display because I didnt writde these methods
    def __display(self,cur,indent):
        if cur < self.__nElems:
            leftChild  = 2*cur + 1      
            print((" " * indent) + str(self.__arr[cur]))
            if leftChild < self.__nElems:
                self.__display(leftChild,   indent+4)
                self.__display(leftChild+1, indent+4) 
                
    def display(self): 
        self.__display(0, 0)    
        for i in range(self.__nElems):
            print(str(self.__arr[i].key))
            
    #find the node who's key contains the lowest value in the minmax heap
    #if the minmax heap is empty the tuple (None, None) is returned
    #otherwise the Node at index 0's key is the minimum value
    #the tuple of its key and data is returned
    #this method is take O(1) runtime
    def findMin(self):
        if self.__nElems == 0: return (None,None)
        if self.__nElems > 0:
            return (self.__arr[0].key, self.__arr[0].data)
    
    #find the node who's key contains the greatest value in the minmax heap
    #if the minmax heap is empty the tuple (None, None) is returned
    #if there is only one or two elements in the minmax heap, a tuple containing 
    #the key and data for the last element in the heap is returned
    #otherwise the second and third elements' keys in the minmax heap are compared and 
    #the tuple containing the greater one's key and data is returned
    #the tuple of its key and data is returned
    #this method is take O(1) runtime    
    def findMax(self):
        if self.__nElems == 0: return (None,None)
        if self.__nElems == 1: return (self.__arr[0].key, self.__arr[0].data)
        if self.__nElems == 2: return (self.__arr[1].key,self.__arr[1].data)
        if self.__arr[1].key > self.__arr[2].key:
            return (self.__arr[1].key,self.__arr[1].data)
        return (self.__arr[2].key, self.__arr[2].data)
    
    #remove a node from the minman heap at a position index 
    # invokes pushDown to preserve the minmaxheap quality 
    def __remove(self,index):
        
        #if index in heap is empty return (None, None)
        if self.__nElems <= index: return (None,None)
        
        #tuple for key, data of node at the index
        returnThis = (self.__arr[index].key,self.__arr[index].data)
        #move the node from the last position in the minmax heap to position index
        self.__arr[index] = self.__arr[self.__nElems-1]
        self.__arr[self.__nElems-1] = None
    
        
        #decrement number of elements
        self.__nElems -= 1
        
        #pushDown to maintain minmax heap quality
        self.__pushDown(index)
        #return the tuple containing the key and data for the removed node
        return returnThis
    
        
    #remove the node with the minimun key value from the minmax heap by invoking
    #__remove on the first position
    def removeMin(self):
       
        if self.__nElems == 0: return (None,None)
       
        return self.__remove(0)
    
    #remove the node with the minimun key value from the minmax heap by invoking
    #__remove on the node on the prooper position
    def removeMax(self):
        if self.__nElems == 0: return (None,None)
        elif self.__nElems == 1: return self.__remove(0)
        elif self.__nElems == 2: return self.__remove(1)
        elif self.__arr[1].key > self.__arr[2].key:
            return self.__remove(1)
        else: return self.__remove(2) 
        
    #push down a Node from position i in the heap into its proper position
    #by comparing it's key's value with other Nodes' keys' values
    #ensuring that that the heap keeps the minmaxheap quality   
    #by invoking the correct _______ method
    def __pushDown(self,i):
        #check if it's on a min level
        if (math.floor(math.log(i+1,2)))%2 ==0:
            self.__pushDownMin(i)
        #if on max level
        else:
            self.__pushDownMax(i)
            
            
    #push down a node from position i in a min level in the heap into
    #its proper position comparing its key with the smallest key from its children and grandchilden's key
    #by comparing it's key's value with other Nodes' keys' values
    #ensuring that that the heap keeps the minmaxheap quality   
    #by invoking the correct _______ method           
    def __pushDownMin(self,i):
        #check if i has children
        if self.__nElems > 2*i +1:
           #make a list of indexes of children and grandchildren
            progeny = [2*i+1, 2*i +2, 2*(2*i+1)+1, 2*(2*i+1)+2,2*(2*i+2)+1,2*(2*i+2)+2]
            small = progeny[0]
            still = True
            count = 0
            #find the index of the smallest child in progeny
            for child in progeny:
                #is this part needed self.__nElems > child
                if self.__nElems > child and still == True and self.__arr[child] is not None:
                    if self.__arr[child].key <= self.__arr[small].key:
                        small = child
                    count+=1
                    
                else: still == False
            #the index of the smallest child is small
            #check if small is a grandchild
            
            if small> (2*i+2) and self.__arr[small] is not None:
                
                #if the new grandchild found is smaller, swap them
                if self.__arr[small].key < self.__arr[i].key:
                    temp = self.__arr[small]
                    self.__arr[small] = self.__arr[i]
                    self.__arr[i] = temp
                    #if the key in small is now greater than the key in its parent swap them
                    if self.__arr[small].key > self.__arr[(small -1)//2].key:
                        temp = self.__arr[small]
                        self.__arr[small] = self.__arr[(small-1)//2]
                        self.__arr[(small-1)//2] = temp 
                        
                    #push down the key that's now in small
                    self.__pushDown(small)
                                     
            #if the child is less then i swap them    
            elif self.__arr[small].key < self.__arr[i].key:
                temp = self.__arr[small]
                self.__arr[small] = self.__arr[i]
                self.__arr[i] = temp
                        
    #push down a node from position i in a mac level in the heap into
    #its proper position comparing its key with the largest key from its children and grandchilden's key
    #by comparing it's key's value with other Nodes' keys' values
    #ensuring that that the heap keeps the minmaxheap quality   
    #by invoking the correct _______ method                   
    def __pushDownMax(self,i):
        #check if i has children
       
        #if i has a child
        if self.__nElems > 2*i +1:
            progeny = [2*i+1, 2*i +2, 2*(2*i+1)+1, 2*(2*i+1)+2,2*(2*i+2)+1,2*(2*i+2)+2]
            large = progeny[0]
            still = True
            count = 0
            #find the index of the greatest key child or grandchild of i
            for child in progeny:
                if self.__nElems > child and still == True and self.__arr[child] is not None: 
                    if self.__arr[child].key >= self.__arr[large].key:
                        large = child    
                    count+=1
                else: still == False
            #check large is a grandchild
            if large > (2*i+2) and self.__arr[large] is not None:
                #if the key of the node in large is larger than the key of the node in position i, swap tham
                if self.__arr[large].key > self.__arr[i].key:
                    temp = self.__arr[large]
                    self.__arr[large] = self.__arr[i]
                    self.__arr[i] = temp
                    #if the key in position large is smaller than its parent swap them
                    if self.__arr[large].key < self.__arr[(large -1)//2].key:
                        temp = self.__arr[large]
                        self.__arr[large] = self.__arr[(large-1)//2]
                        self.__arr[(large-1)//2] = temp 
                    #push down position large of the minmanheap
                    self.__pushDown(large)
                    
            #if the large is a child position of i ans its key is less then i,
            #swap them    
            elif self.__arr[large].key > self.__arr[i].key:
                temp = self.__arr[large]
                self.__arr[large] = self.__arr[i]
                self.__arr[i] = temp 
           
    #check that the minmanheap preserves the heap quality            
    def isMinMaxHeap(self):
        #edge cases
        #if 1 element or 0 it's a minmaxheap
        if self.__nElems == 1 or self.__nElems == 0: return True         
        #the first element's must be less than the second and third elements' keys
        if self.__arr[0].key > self.__arr[1].key\
        or (self.__nElems > 2 and self.__arr[0].key > self.__arr[2].key):
            return False
               
        #loop through the elements of the minmax heap starting from the 4th element
        for i in range(self.__nElems):   #go through each level starting from root
            if i > 2:
                #check if it's a min level
                if (math.floor(math.log(i+1,2)))%2 ==0:
                    #if the key is less than grandparent, it's not a heap
                    #if the key is greater than parent, it's not a heap
                    if self.__arr[i].key < self.__arr[(((i-1)//2)-1)//2].key \
                    or self.__arr[i].key > self.__arr[(i-1)//2].key:
                        return False
                #max levels
                else:
                    #if the key is greater than grandparent or less than parent,
                    #it's not a minmax heap
                    if self.__arr[i].key > self.__arr[(((i-1)//2)-1)//2].key\
                       or self.__arr[i].key < self.__arr[(i-1)//2].key:
                        return False
           
            
        #if passed all the statements above it's a minman heap 
        return True
            
                        
#fake heap class for testing  
class fakeHeap(object):
    
    
    #initiate the fakeHeap
    #if try to initiate a heap with underlying size of less than 3
    #, an underlying data structure of size 3 is created
    def __init__(self,size):
        if size <= 2:
            size = 3
        self.__data = [] 
        self.__size = size
        
        
    #if there's available space left in the minmax heap,
    #append a tuple containing the data and key to the data list 
    def insert(self,d,k):
        if len(self.__data) < self.__size:
            self.__data += [(d,k)]
        #if no available space and tuple not inserted, return False
        else: return False
        
    #return the tuple containing the data and key for the node containing
    #the miniman valued key in the array
    #if array is empty return the tuple (None,None) 
    def findMin(self):
        if len(self.__data) == 0: return (None,None)
        return min(self.__data,key=lambda item: item[1])
    
    #return the tuple containing the data and key for the node containing
    #the maximum valued key in the array
    #if array is empty return the tuple (None,None)     
    def findMax(self):
        if len(self.__data) ==0: return (None, None)
        return max(self.__data, key=lambda item: item[1])  
    
    #remove the tuple returned by findMin by looping through the array to find it
    #if array is empty return the tuple (None,None)     
    def removeMin(self):
        if len(self.__data) == 0: return (None,None)
        little = self.findMin()
   
        for i in range(len(self.__data)):
            if self.__data[i] == little:
                return self.__data.pop(i)
                
       
                
    #remove the tuple returned by findMaax by looping through the array to find it
    #if array is empty return the tuple (None,None)  
    def removeMax(self):
        if len(self.__data) == 0: return (None,None)
        big = self.findMax()
        
        for i in range(len(self.__data)): 
            if self.__data[i] == big:
                return self.__data.pop(i) 
        return big

 
 
 

#test the find min on an empty minmax heap
def test_emptyFindMin():
    #empty heap with 0 space
    h = Heap(0)
    f = fakeHeap(0)
    assert h.findMin() == f.findMin()
    #empty heap with alotted storage of thirty
    h = Heap(30)
    f = fakeHeap(30)
    assert h.findMin() == f.findMin()

#empty heap find max
def test_emptyFindMax():
    #empty heap with 0 space
    h = Heap(0)
    f = fakeHeap(0)
    assert h.findMax() == f.findMax()
    #empty heap with alotted storage of thirty
    h = Heap(30)
    f = fakeHeap(30)
    assert h.findMax() == f.findMax()

#empty heap remove max
def test_emptyRemoveMax():
    #empty heap 0 alotted storage
    h = Heap(0)
    f = fakeHeap(0)
    assert h.removeMax() == f.removeMax()
    #empty heap with 30 allotted storage
    h = Heap(30)
    f = fakeHeap(30)
    assert h.removeMax() == f.removeMax()

#empty heap remove min
def test_emptyRemoveMin():
    #empty heap with 0 alotted storage
    h = Heap(0)
    f = fakeHeap(0)
    assert h.removeMin() == f.removeMin()
    #empty heap with 30 allotted storage
    h = Heap(30)
    f = fakeHeap(30)
    assert h.removeMin() == f.removeMin()
    
#test inserting into a heap that was created to have zero alotted storage 
def test_emptyInsert():
    h = Heap(0)
    assert h.insert(3, chr(ord('A') + 1 + 3)) == True
    assert h.isMinMaxHeap() == True
    
#test large heap find min
def test_largeHeapFindMin():
    h = Heap(100)
    f = fakeHeap(100)
    for i in range(75):  # insert 30 items
        h.insert(int(i), chr(ord('A') + 1 + i))
        f.insert(int(i), chr(ord('A') + 1 + i))
    assert h.findMin() == f.findMin()
    
#testing large heap find max
def test_largeHeapFindMax():
    h = Heap(100)
    f = fakeHeap(100)
    for i in range(75):  # insert 30 items
        h.insert(int(i), chr(ord('A') + 1 + i))
        f.insert(int(i), chr(ord('A') + 1 + i))
    assert h.findMax() == f.findMax()
    
#testing large heap remove min
def test_largeHeapRemoveMin():
    h = Heap(100)
    for i in range(75):  # insert 30 items
        h.insert(int(i), chr(ord('A') + 1 + i))
    assert h.isMinMaxHeap() == True
    h.removeMin()
    assert h.isMinMaxHeap() == True    
    
#testing large heap remove max
def test_largeHeapRemoveMax():
    h = Heap(100)
    for i in range(75):  
        h.insert(int(i), chr(ord('A') + 1 + i))
    assert h.isMinMaxHeap() == True
    h.removeMax()
    assert h.isMinMaxHeap() == True 
    
#test large heap insert
def test_largeHeapInsert():
    h = Heap(100)
    h.insert(int(2),chr(ord("u")+1))
    assert h.isMinMaxHeap() == True
    for i in range(75): 
        h.insert(int(i), chr(ord('A') + 1 + i))  
    assert h.isMinMaxHeap() == True
    
#test inserting more than the capacity of the minmax heap
def test_insertOverLimit():
    h = Heap(30)
    for i in range(30): 
        h.insert(int(i), chr(ord('A') + 1 + i))  
    assert h.isMinMaxHeap() == True   
    
    assert h.insert(40, chr(ord('j'))) == False

#test small heap find min
def test_smallHeapFindMin():
    h = Heap(10)
    f = fakeHeap(10)
    for i in range(8):  
        h.insert(int(i), chr(ord('A') + 1 + i))
        f.insert(int(i), chr(ord('A') + 1 + i))
    assert h.findMin() == f.findMin()
#test small heap find max
def test_smallHeapFindMax():
    h = Heap(10)
    f = fakeHeap(10)
    for i in range(8):  
        h.insert(int(i), chr(ord('A') + 1 + i))
        f.insert(int(i), chr(ord('A') + 1 + i))
    assert h.findMax() == f.findMax()
#test small heap remove min
def test_smallHeapRemoveMin():
    h = Heap(10)
    f = fakeHeap(10)
    for i in range(8):  
        h.insert(int(i), chr(ord('A') + 1 + i))
        f.insert(int(i), chr(ord('A') + 1 + i))
    
    assert h.isMinMaxHeap() == True
    assert h.removeMin() == f.removeMin()
    
    assert h.isMinMaxHeap() == True
    
#test small heap remove max
def test_smallHeapRemoveMax():
    h = Heap(10)
    f = fakeHeap(10)
    for i in range(8):  # insert 30 items
        h.insert(int(i), chr(ord('A') + 1 + i))
        f.insert(int(i), chr(ord('A') + 1 + i))
    assert h.isMinMaxHeap() == True
    assert h.removeMax() == f.removeMax()
    assert h.isMinMaxHeap() == True


#test only root find min
def test_onlyRootFindMin():
    h = Heap(3)
    f = fakeHeap(3)
    h.insert(int(1), chr(ord('A') + 1 + 1))
    f.insert(int(1), chr(ord('A') + 1 + 1))
    assert h.findMin() == f.findMin()
    
#test only root find max
def test_onlyRootFindMax():
    h = Heap(3)
    f = fakeHeap(3)
    h.insert(int(1), chr(ord('A') + 1 + 1))
    f.insert(int(1), chr(ord('A') + 1 + 1))  
    
    assert h.findMax() == f.findMax()
    
#test only root remove max
def test_OnlyRootHeapRemoveMax():
    h = Heap(10)
    f = fakeHeap(10)
    h.insert(int(1), chr(ord('A') + 1))
    f.insert(int(1), chr(ord('A') + 1))  
    assert h.isMinMaxHeap() == True
    assert h.removeMax() == f.removeMax()
    assert h.isMinMaxHeap() == True
#test only root remove min
def test_OnlyRootHeapRemoveMin():
    h = Heap(10)
    f = fakeHeap(10)
    h.insert(int(1), chr(ord('A') + 1))
    f.insert(int(1), chr(ord('A') + 1))  
    assert h.isMinMaxHeap() == True
    assert h.removeMin() == f.removeMin()
    assert h.isMinMaxHeap() == True

#test only two elements find min
def test_twoElemsFindMin():
    h = Heap(3)
    f = fakeHeap(3)
    h.insert(int(1), chr(ord('A') + 1 + 1))
    f.insert(int(1), chr(ord('A') + 1 + 1))
    h.insert(int(2), chr(ord('A') + 1 + 2))
    f.insert(int(2), chr(ord('A') + 1 + 2)) 
    assert f.findMin() == h.findMin()
#test only two elements find max
def test_twoElemsFindMax():
    h = Heap(3)
    f = fakeHeap(3)
    h.insert(int(1), chr(ord('A') + 1 + 1))
    f.insert(int(1), chr(ord('A') + 1 + 1))
    h.insert(int(2), chr(ord('A') + 1 + 2))
    f.insert(int(2), chr(ord('A') + 1 + 2)) 
    assert h.findMax() == f.findMax()
    
#test insert in ascending
def test_insertAscending():
    h = Heap(50)
    
    for i in range(30):  # insert 30 items
        h.insert(int(i), chr(ord('A') + 1 + i))
    assert h.isMinMaxHeap() == True  
    
#test insert in descending
def test_insertDescending():
    h = Heap(50)
    for i in range(30,1,-1):  # insert 30 items
        h.insert(int(i), chr(ord('A') + 1 + i))
    assert h.isMinMaxHeap() == True
   
#randomly test the methods insert, findMin, findMax, removeMax, and removeMax
#in a random order on different size minmax heaps
def test_torture():
    options = ["insert", "findMin", "findMax", "findMax", "removeMin", "removeMax"]
    #loop through this 50 times
    for i in range(50):
        #create a Heap and fakeHeap with underlying size randomly selected between 0 and 500
        size = random.randint(0,500)
        h = Heap(size)
        f = fakeHeap(size)
        
        #run 1000 tests
        for i in range(1000):
            #before each test assert that minmax heap property preserved
            assert h.isMinMaxHeap()
            
            #randomly select a test 
            #and check/ run the test chosen
            turn = random.choice(options)
            if turn == "findMin":                
                assert h.findMin() == f.findMin()
            
            elif turn == "findMax":
                assert h.findMax() == f.findMax()
              
            elif turn == "removeMin":
                assert h.removeMin() == f.removeMin()
                assert h.isMinMaxHeap()
        
            elif turn == "removeMax":
                assert h.removeMax() == f.removeMax()
                assert h.isMinMaxHeap()
                
            elif turn == "insert":
                for i in range(random.randint(0,100)):
                    newNum = i
                    h.insert(int(newNum), chr(ord('A') + 1 + i))
                    f.insert(int(newNum), chr(ord('A') + 1 + i))                    
                    
pytest.main(["-v", "-s", "minmaxheap.py"]) 


