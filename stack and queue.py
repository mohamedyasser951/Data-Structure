# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 23:44:58 2020

@author: DELL
"""

class Queue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def size(self):
        return len(self.items)
    def en_queue(self,item):
        self.items.insert(0,item)
    def de_queue(self):
        self.items.pop()
    def peek(self):
        return self.items[-1]
q=Queue()
#print(q.is_empty())
q.en_queue(1)
q.en_queue(2)
q.en_queue(3)

print(q.peek())


       