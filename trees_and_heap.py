from collections import deque
class Node():
    def __init__(self,data,left= None,right=None):
        self.data = data
        self.left = left
        self.right = right
    
    #insert element in tree   
    def insert(self,value):
        if self.data:
            if value<self.data:
                if  not self.left:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value>self.data:
                if not self.right:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.data = value
    
    #inorder traversal       
    def inorder(self, root):
        self.res = []
        if root:
            self.res = self.inorder(root.left)
            self.res.append(root.data)
            self.res+= self.inorder(root.right)
        return self.res
    
    #postorder traversal   
    def postorder(self,root):
        self.res = []
        if root:
            self.res = self.inorder(root.left)
            self.res+= self.inorder(root.right)
            self.res.append(root.data)
        return self.res
    
    #preorder traversal    
    def preorder(self,root):
        self.res = []
        if root:
            self.res.append(root.data)
            self.res+=self.preorder(root.left)
            self.res+=self.preorder(root.right)
        return self.res
    
    #levelorder traversal    
    def levelorder(self, root):
        res = []
        level=0
        deq = deque([root,])
        while deq:
            res.append([])
            for i in range(len(deq)):
                
                node = deq.popleft()
                res[level].append(node.data)
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
            level+=1
                
        return res
        
    #reverse levelorder traversal
    def reverselevelorder(self, root):
        res = []
        level=0
        deq = deque([root,])
        while deq:
            res.append([])
            for i in range(len(deq)):
                
                node = deq.popleft()
                res[level].append(node.data)
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
            level+=1
                
        result = []
        for i in range(len(res)-1,-1,-1):
            result.append(res[i])
        return result
        
    #size of the tree   
    def size(self, root):
        if not root:
            return 0
        a = self.size(root.left)
        b = self.size(root.right)
        return a+b+1
        
    #maximum depth of the tree   
    def maxdepth(self, root):
        if not root:
            return 0
        a = self.maxdepth(root.left)
        b = self.maxdepth(root.right)
        return 1 + max(a,b)
    
    #minimum depth of the tree   
    def mindepth(self,root):
        if not root:
            return 0 
        a = self.mindepth(root.left)
        b = self.mindepth(root.right)
        if not root.left or not root.right:
            return a+b+1 
        else:
            return 1 +min(a,b)
            
    #same tree    
    """def sametree(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 and root2:
            return False
        if root1.data != root2.data:
            return False
        if root1.data == root2.data: 
            return self.sametree(root1.left, root2.left) and self.sametree(root1.right, root2.right)
            
obj1 = Node(10)
obj1.insert(11)
obj1.insert(9)
obj2 = Node(10)
obj2.insert(11)
obj2.insert(9)
obj2.insert(8)
print(obj1.sametree(obj1,obj2))"""


    #level order in spiral order
    def spirallevelorder(self,root):
        if not root:
            return
        res = []
        res1 = []
        res2 =[]
        res1.append(root)
        
        while res1 or res2:
            
            while res1:
                
                node = res1.pop()
                res.append(node.data)
                if node.right:
                    res2.append(node.right)
                if node.left:
                    res2.append(node.left)
            
            while res2:
                
                node = res2.pop()
                res.append(node.data)
                if node.left:
                    res1.append(node.left)
                if node.right:
                    res1.append(node.right)
        return str(res) + " is the Spiral Level order"

    
        
        
object1 = Node(10)
object1.insert(11)
object1.insert(12)
object1.insert(9)
object1.insert(8)
object1.insert(7)
object1.insert(13)
print(object1.inorder(object1))
print(object1.postorder(object1))
print(object1.preorder(object1))
print(object1.levelorder(object1))
print(object1.spirallevelorder(object1))
print(object1.reverselevelorder(object1))
print(object1.size(object1))
print(object1.maxdepth(object1))
print(object1.mindepth(object1))

#hashtable implementation

class hashtable():
    
    #insertion in hashtable
    def hashmap(self, hash_table, key, value):
        hash_key = hash(key)%len(hash_table)
        bucket = hash_table[hash_key]
        key_exists = False
        for i , kv in enumerate(bucket):
            k,v =kv
            if key==k:
                key_exists= True
                break
        if key_exists:
            bucket[i]= ((key,value))
        else:
            bucket.append((key,value))
    
    #search for a key and if key exists then return value        
    def search(self,key):
        hash_key = hash(key)%len(hash_table)
        bucket = hash_table[hash_key]
        key_exists = False
        for i , kv in enumerate(bucket):
            k,v =kv
            if key==k:
                key_exists= True
                break
        if key_exists:
            return bucket[i][1]
            
    def delete(self,key):
        hash_key = hash(key)%len(hash_table)
        bucket = hash_table[hash_key]
        key_exists = False
        for i , kv in enumerate(bucket):
            k,v =kv
            if key==k:
                key_exists= True
                del bucket[i]
    
hash1 = hashtable()
hash_table = [[] for i in range(10)]
hash1.hashmap(hash_table,20,"INDIA")
hash1.hashmap(hash_table,30,"BHARAT")
hash1.hashmap(hash_table,25,"ENGLAND")
print(hash_table)
print(hash1.search(20))
print(hash1.search(30))  
print(hash1.search(25)) 
hash1.delete(25)
print(hash_table)

#heap
class maxheap():
    def __init__(self, items = []):
        self.heap =[0]
        for i in items:
            self.heap.append(i)
            self.floatup(len(self.heap)-1)
            
    def insertinheap(self,value):
        self.heap.append(value)
        self.floatup(len(self.heap)-1)
        
    def floatup(self,index):
        parent = index//2 
        if index<2:
            return
        if index>=2:
            if self.heap[index]>self.heap[parent]:
                self.swapfunction(index,parent)
                self.floatup(parent)
    
    def swapfunction(self,i,j):
        self.heap[i], self.heap[j]= self.heap[j], self.heap[i]
        
    def movebottom(self, index):
        largest= index
        left = index*2
        right = index*2 + 1
        if len(self.heap)>left and self.heap[largest]<self.heap[left]:
            largest = left
        if len(self.heap)>right and self.heap[largest]<self.heap[right]:
            largest = right
        if largest!=index:
            self.swapfunction(index,  largest)
            self.movebottom(largest)
    
    def deleteinheap(self):
        if len(self.heap)>2:
            self.swapfunction(1, len(self.heap)-1)
            max1 = self.heap.pop()
            self.movebottom(1)
        elif len(self.heap)==2:
            max1 = self.heap.pop()
        else:
            max1 = False
        return max1

heapobj = maxheap()
heapobj.insertinheap(1)
heapobj.insertinheap(3)
heapobj.insertinheap(4)
heapobj.insertinheap(5)
heapobj.insertinheap(8)
print(heapobj.heap)
heapobj.deleteinheap()
print(heapobj.heap)












