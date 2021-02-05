#!/usr/bin/env python
# coding: utf-8

# In[36]:


import random

class Node:
    def __init__(self, key, value):
        self.key = key
        self.p = random.random()
        self.value = value
        self.left = None
        self.right = None

    def leftrotate(self):
        x = self
        y = x.right
        x.right = y.left
        y.left = x
        x = y
        y = x.left
        
        return x

    def rightrotate(self):
        x = self
        y = x.left
        x.left = y.right
        y.right = x
        x = y
        y = x.right

        return x

    
    def __repr__(self):
        return "(node key:%s )" % (str(self.key))


class Treap:
    def __init__(self):
        self.root = None

    #Func to add node
    def __add(self, node, key, value):
        if node is None:
            node = Node(key, value)
            return node
       
        #if ky less than node key add in left subtree, else in right subtree
        if key < node.key:
            node.left = self.__add(node.left, key, value)
            if node.left.p < node.p:
                node = node.rightrotate()
        elif key >= node.key:
            node.right = self.__add(node.right, key, value)
            if node.right.p < node.p:
                node = node.leftrotate()
        
        return node

    def add(self, key, value):
        self.root = self.__add(self.root, key, value)
    
    #finds node
    def __find(self, node, key):
        if node == None:
            return None
        if node.key == key:
            return node
        if key < node.key:
            return self.__find(node.left, key)
        else:
            return self.__find(node.right, key)

    def find(self, key):
        return self.__find(self.root, key)

    #func to remove node
    def __remove(self, node, key):
        #if tree is empty
        if node is None:
            return False
        if node.key == key:
            
            #case 1: leaf node
            if node.left is None and node.right is None:
                return None
            
            #case 2: has right child
            elif node.left is None:
                return node.right
            
            #case 3: has left child
            elif node.right is None:
                return node.left
            else:
                if node.left.p < node.right.p:
                    node = node.rightrotate()
                    node.right = self.__remove(node.right, key)
                else:
                    node = node.leftrotate()
                    node.left = self.__remove(node.left, key)
        elif key < node.key:
            node.left = self.__remove(node.left, key)
        else:
            node.right = self.__remove(node.right, key)

        return node

    def remove(self, key):
        if self.find(key) is None: 
            return False
        self.root = self.__remove(self.root, key)
        return True

    

    
    #traverse the tree
    def __traverse(self, node):
        if node == None: 
            return
        self.__traverse(node.left)
        print (node.key)
        self.__traverse(node.right)

    def traverse(self):
        self.__traverse(self.root)
    
    def __repr__(self):
        return str(self.root)
    

