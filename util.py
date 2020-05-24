import math
import random
import copy

class Object(object):
    def __init__(self, elem):
        self.elem = elem 

    def __repr__(self):
        return '%s'%self.elem

    def __hash__(self):
        return hash(self.elem)

    def __eq__(self, other):
        return (isinstance(other, Object) and (self.elem == other.elem))

    def __lt__(self, other):
        return (isinstance(other, Object) and (self.elem < other.elem))

    def __le__(self, other):
        return (isinstance(other, Object) and (self.elem <= other.elem))

    def __ne__(self, other):
        return (isinstance(other, Object) and (self.elem != other.elem))

    def __gt__(self, other):
        return (isinstance(other, Object) and (self.elem > other.elem))

    def __ge__(self, other):
        return (isinstance(other, Object) and (self.elem >= other.elem))

    def get_elem(self):
        return self.elem

def create_object_array(array):
    ls = []
    for a in array:
        ls.append(Object(a))
    return ls


class Bar(Object):
    def __init__(self, elem, index=0, width=20, color='OrangeRed2'):
        super().__init__(elem)
        self.color = color
        self.width = width
        self.index = index

    def set_index(self, index):
        self.index = index

    def set_color(self, color):
        self.color = color

    
    