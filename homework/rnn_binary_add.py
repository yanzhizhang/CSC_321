import numpy as np

U = np.array([[1, 1], [1, 1], [1, 1]])
V = np.array([1, -2., 2]).reshape((1, 3))
W = np.array([[0,1,0], [0,1.,0], [0,1,0]])
bh = np.array([-0.5,-1.5,-2.5]).reshape((3, 1))
by = -0.5



def act(x):
    return (x >= 0) * 1.

def add(x, y, c1, c2):
    h = None
    if c1 == 0 and c2 == 0:
        h = np.array([0, 0, 0])
    elif c1 == 0 and c2 == 1:
        h = np.array([1.0, 0, 0])
    elif c1 == 1 and c2 == 0:
        h = np.array([1.0, 1, 0])
    elif c1 == 1 and c2 == 1:
        h = np.array([1.0, 1, 1])
    h = h.reshape((3, 1))
    x = np.array([x, y]).reshape((2, 1))
    result = U.dot(x) + W.dot(h) + bh
    # print(result)
    result = act(result)
    # print(result)
    result = V.dot(result) + by
    # print(result)
    result = act(result)
    # print(result)
    return np.sum(result)

print(add(0,0,0,0) == 0)
print(add(0,0,0,1) == 0)
print(add(0,0,1,0) == 1)
print(add(0,0,1,1) == 1)
print(add(0,1,0,0) == 1)
print(add(0,1,0,1) == 1)
print(add(0,1,1,0) == 0)
print(add(0,1,1,1) == 0)
print(add(1,0,0,0) == 1)
print(add(1,0,0,1) == 1)
print(add(1,0,1,0) == 0)
print(add(1,0,1,1) == 0)
print(add(1,1,0,0) == 0)
print(add(1,1,0,1) == 0)
print(add(1,1,1,0) == 1)
print(add(1,1,1,1) == 1)
