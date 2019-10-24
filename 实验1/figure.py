from math import pi
from math import sqrt
import abc
class figure(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod#抽象方法
    def girth(self):
        pass

    @abc.abstractmethod
    def area(self):
        pass


class circle(figure):
    def __init__(self,r):
        self.r = r


    def girth(self):
        return 2*pi*self.r


    def area(self):
        return pi*self.r*self.r



class rectangle(figure):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def area(self):
        return self.a*self.b
    def girth(self):
        return 2*(self.a+self.b)


class triangle(figure):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c)/2
        return sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))


    def girth(self):
        return self.a+self.b+self.c



class ellipse(figure):
    def __init__(self,a,b):
        self.a = a 
        self.b = b

    def area(self):
        return self.a*self.b*pi

    def girth(self):
        return self.b*2*pi + 4*(self.a - self.b)