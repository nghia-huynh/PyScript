#!/usr/bin/env python

class Circle:
    pi = 3.14156 #class variable

    def __init__(self, radius=5):
        self.radius = radius #instance variable

    def area(self):
        return self.radius * self.radius * Circle.pi

def main():
    cir1 = Circle(10)
    print cir1.area()
    cir2 = Circle()
    print cir2.area()

if __name__ == "__main__":
    main()
