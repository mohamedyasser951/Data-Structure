class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def set_data(self,item):
        self.data=item
    def get_data(self):
        return self.data
    def set_next(self,newnext):
        self.next=newnext
    def get_next(self):
        return self.next

class Linked_List():
      def __init__(self):
          self.head=None
      def is_empty(self):
          return self.head==None
      def add_at_beganing(self,item):
          newnode=Node(item)
          newnode.set_next(self.head)
          self.head=newnode
      def add_end(self,item):
          newnode=Node(item)
          current=self.head
          while current.get_next()!=None:
              current=current.get_next()
          current.set_next(newnode)
      def size(self):
          current=self.head
          count=0
          while current !=None:
              count+=1
              current=current.get_next()
          return count    
      def print_list(self):
          current=self.head
          print("list data : ")
          while current !=None:
              print(current.get_data(),end=" ")
              current=current.get_next()
      def search(self,item):
          current=self.head
          found=False
          while current !=None and not found:
             if current.get_data()==item:
                 found =True
             else:
                 current=current.get_next()
          return found   
      def remove(self,item):
          current=self.head
          previous=None
          found=False
          while not found:
              if current.get_data()==item:
                  found=True
              else:
                  previous=current
                  current=current.get_next()
              if previous==None:
                  self.head=current.get_next()
              else:
                  previous.set_next(current.get_next())
      def add_at_position(self,item,pos):
          if pos<0 or pos>self.size():
              return None
          else:
              newnode=Node(item)
              current=self.head
              count=0
              while count<pos-1:
                  count+=1
                  current=current.get_next()
              newnode.set_next(current.get_next())
              current.set_next(newnode)
      def delet(self):
          self.head=None
l=Linked_List()
l.add_at_beganing("mahamoud1")
l.add_at_beganing("yasser")
l.add_at_beganing("mohamed")
l.add_end("mosa")
l.add_at_position("mahamoud2",2)  
l.print_list()
#print(l.search(""))
