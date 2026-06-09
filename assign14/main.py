import sys
import gc

class Node:
    def __init__(self, name):
        self.name = name
        self.link = None
    
    def __repr__(self):
        return f"Node({self.name})"

print("Create Circular Reference")
A = Node("A")
B = Node("B")

A.link = B
B.link = A

print(f"A: {A}, refcount = {sys.getrefcount(A)}")
print(f"B: {B}, refcount = {sys.getrefcount(B)}")
print("(Both have refcount > 1 due to cycle)")

print("\nDelete Variables")
del A
del B
print("A and B deleted from code")
print("But they still exist in memory due to circular reference!")

print("\nForce Garbage Collection")
collected = gc.collect()
print(f"Unreachable objects collected: {collected}")
print("Memory freed!")
