class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next
        self.previous=prev
    def set_data(self,newdata):
        self.data=newdata
    def get_data(self):
        return self.data
    def set_next(self,newnext):
        self.next=newnext
    def get_next(self):
        return self.next
    def set_previous(self,newprev):
        self.previous=newprev
    def get_previous(self):
        return self.previous
    def has_previous(self):
        return self.previous !=None
    def has_next(self):
        return self.next !=None
    
class linked_List:
    def __init__(self):
        self.head=None
        self.tail=None
    def add_at_begging(self,item):
        newnode=Node(item)
        if self.head==None:
            self.head=self.tail=newnode
        else:
            newnode.set_previous(None)
            newnode.set_next(self.head)
            self.head.set_previous(newnode)
            self.head=newnode
    def add_end(self,item):
        newnode=Node(item)
        current=self.head
        while current.get_next() != None:
            current=current.get_next()
        current.set_next(newnode)
        self.tail=newnode
    def add_at_position(self,item,pos):
        if pos<0:
           return None #error 
        else:                 
             newnode=Node(item)
             current=self.head
             count=0
             while count<pos-1:
                   count+=1
                   current= current.get_next()
             newnode.set_next(current.get_next())
             newnode.set_previous(current)
             current.get_next().set_previous(newnode)
             current.get_next(newnode)      
    def remove(self,item):
        current=self.head
        found=False
        while current !=None or not found:
              if current.get_data()==item:
                  found=True
              else:
                  current=current.get_next()
        if current.get_previous()==None:
           self.head=current.get_next()
        else:
            current.get_previous().set_next(current.get_next())
            current.get_next().set_previous(current.get_previous())
    def size(self):
        current=self.head
        count=0
        while current !=None:
            count+=1
            current=current.get_next()
        return count 
    def is_empty(self):
        return self.head==self.tail==None
    def print_list(self):
        current=self.head
        print("list item : ")
        while current !=None:
            print(current.get_data(),end=" ")
            current=current.get_next()
        
l=linked_List()
#print(l.is_empty())
#l.add_end("5")
l.add_at_begging("2")
l.add_at_begging("1") 
l.add_at_position("3",2)
l.add_at_position("4",3)
l.print_list()




       