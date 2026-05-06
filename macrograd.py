# import math
# import numpy as np
# import matplotlib.pyplot as plt

# def f(x):
#     return x**2 - 3*x + 5

# f(3)
# print(f(3))

# xs = np.arange(-10, 10, 0.1)
# print(xs)
# ys = f(xs)
# print(ys)
# plt.plot(xs, ys)
# plt.show()

### derivative formula applied to f(x) = x^2 - 3x + 5
# h = 0.0000000001
# x = 3
# print("f(x) =", f(x))
# print("f(x + h) =", f(x + h))
# print("f(x + h) - f(x) =", (f(x + h) - f(x))) ### function responded in positive direction, so the slope is positive
# print("Derivative =", (f(x + h) - f(x)) / h)

### making things little complex

a = 2.0
b = -3.0
c = 10.0
d = a * b + c
# print("d =", d)

h = 0.0001
# Input values
a = 2.0
b = -3.0
c = 10.0

d1 = a * b + c

# # looking at derivative of a with respect to d
# a += h

# d2 = a * b + c

# print("d1 =", d1) # d1 is the original value of d
# print("d2 =", d2) # d2 is the new value of d after a has been increased by h. The change in d (d2 - d1) is how much d changed when a changed by h. Dividing this change by h gives us the rate of change of d with respect to a, which is the derivative.
# print("Slope/Derivative =", (d2 - d1) / h) # (d2 - d1) means how much d changed when a changed by h. Dividing by h gives us the rate of change of d with respect to a, which is the derivative.

# # looking at derivative of a with respect to d
# b += h

# d2 = a * b + c

# print("d1 =", d1) # d1 is the original value of d
# print("d2 =", d2) # d2 is the new value of d after a has been increased by h. The change in d (d2 - d1) is how much d changed when a changed by h. Dividing this change by h gives us the rate of change of d with respect to a, which is the derivative.
# print("Slope/Derivative =", (d2 - d1) / h) # (d2 - d1) means how much d changed when a changed by h. Dividing by h gives us the rate of change of d with respect to a, which is the derivative.

# looking at derivative of a with respect to d
# c += h

# d2 = a * b + c

# print("d1 =", d1) # d1 is the original value of d
# print("d2 =", d2) # d2 is the new value of d after a has been increased by h. The change in d (d2 - d1) is how much d changed when a changed by h. Dividing this change by h gives us the rate of change of d with respect to a, which is the derivative.
# print("Slope/Derivative =", (d2 - d1) / h) # (d2 - d1) means how much d changed when a changed by h. Dividing by h gives us the rate of change of d with respect to a, which is the derivative.


class value:
    def __init__(self, data, _children=(), _op='', label='', grad=0.0):
        self.data = data
        self.grad = 0.0
        self._prev = _children
        self._op = _op
        self.label = label
        self.grad = 0.0
    
    def __repr__(self): # helps to print the value instance in a readable format. When we print an instance of the value class, it will show the data attribute instead of the default object representation.
        return f"value(data={self.data})"
    
    def __add__(self, other):
        if not isinstance(other, value):
            other = value(other)
        return value(self.data + other.data, (self, other), '+')

    def __radd__(self, other):
        return self + other
    
    def __mul__(self, other):
        if not isinstance(other, value):
            other = value(other)
        return value(self.data * other.data, (self, other), '*')

    def __rmul__(self, other):
        return self * other
    
    def __pow__(self, other):
        if not isinstance(other, value):
            other = value(other)
        return value(self.data ** other.data, (self, other), '**')
    
    def __truediv__(self, other):
        if not isinstance(other, value):
            other = value(other)
        return value(self.data / other.data, (self, other), '/')

    def __rtruediv__(self, other):
        if not isinstance(other, value):
            other = value(other)
        return other / self
    
    def __neg__(self):
        return value(-self.data, (self,), 'neg')
    
    def __sub__(self, other):
        if not isinstance(other, value):
            other = value(other)
        return value(self.data - other.data, (self, other), '-')

    def __rsub__(self, other):
        if not isinstance(other, value):
            other = value(other)
        return other - self
    
a = value(2.0, label='a')
b = value(-3.0, label='b')

# If we try to add a and b, it will call the a.__add__(b) method, which will return a new value instance with the data attribute equal to the sum of a.data and b.data. So, a + b will return value(data=-1.0).
c = value(10.0, label='c', grad=1.0)
d = a * b + c; d.label = 'd'; d.grad = 1.0
f = a * a * b; f.label = 'f'; f.grad = 1.0
e = f + c; e.label = 'e'; e.grad = 1.0

# print(e)

from graphviz import Digraph

def trace(root):
    # builds a set of all nodes and edges in a graph
    nodes, edges = set(), set()
    def build(v):
        if v not in nodes:
            nodes.add(v)
            for child in v._prev:
                edges.add((child, v))
                build(child)
    build(root)
    return nodes, edges

def draw_dot(root):
    dot = Digraph(format='svg', graph_attr={'rankdir': 'LR'}) # LR = left to right
    
    nodes, edges = trace(root)
    for n in nodes:
        uid = str(id(n))
        # for any value in the graph, create a rectangular node
        dot.node(name=uid, label = "{ %s | data %.4f | grad %.4f }" % (n.label, n.data, n.grad), shape='record')
        if n._op:
            # if this value is a result of some operation, create an op node
            dot.node(name=uid + n._op, label=n._op)
            # and connect this node to it
            dot.edge(uid + n._op, uid)
    
    for n1, n2 in edges:
        # connect n1 to the op node of n2
        dot.edge(str(id(n1)), str(id(n2)) + n2._op)
    
    return dot

# draw_dot(e).render('graph', view=True, cleanup=True) ## the output of the forward path with will be shown in the graph. The graph will show the operations and the values of each node in the computation graph. The data attribute will show the value of each node, and the grad attribute will show the gradient of each node, which is initially set to 0.0. The label attribute will show the name of each node, which we have set for a, b, c, d, e, and f.

# So, now we gonna do a backpropogation to calculate the gradients of each node in the graph. We will start from the output node e and propagate the gradients back to the input nodes a, b, and c. The gradient of the output node e will be set to 1.0, and then we will use the chain rule to calculate the gradients of the other nodes in the graph.

# In backprogation we gonna start from the output node e and propagate the gradients back to the input nodes a, b, and c. The gradient of the output node e will be set to 1.0, and then we will use the chain rule to calculate the gradients of the other nodes in the graph.

# Also, we gonna compute the derivate of the node w.r.t e

# so the derivative of e w.r.t e is 1.0, because e is the output node and we are interested in how much e changes with respect to itself. So, we set e.grad = 1.0.

# derivative of f w.r.t e is 1.0, because e is the output node and f is one of the inputs to e. So, we set f.grad = 1.0.

# so we gonna do derivative of e with respect to all the nodes in the graph

# output.grad = 1.0  # always set by hand

# So, we also need to know how the weights are impacting the output. derivative of the output and sum of the weights is 1.0, because the output is a linear combination of the weights. So, we set w.grad = 1.0.

# filling gradients e.grad = 1.0 - what's derivate of e w.r.t e - means what if I cahange e by a little bit, how much will e change - the answer is 1.0 because e is the output node and we are interested in how much e changes with respect to itself. So, we set e.grad = 1.0.

def lol():
    h = 0.0001

    a = value(2.0, label='a')
    b = value(-3.0, label='b')
    c = value(10.0, label='c')
    d = a * b + c; d.label = 'd'
    f = a * a * b; f.label = 'f'
    e = f + c; e.label = 'e'
    e1 = e.data

    a = value(2.0 , label='a')
    b = value(-3.0, label='b')
    c = value(10.0, label='c')
    d = a * b + c; d.label = 'd'
    f = a * a * b; f.label = 'f'
    e = f + c + h; e.label = 'e'
    e2 = e.data

    print((e2-e1)/h) # rise over run - how much e changed when a changed by h. Dividing by h gives us the rate of change of e with respect to a, which is the derivative.
    
lol()