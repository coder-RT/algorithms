#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def isIdentical(t1, t2):
    if t1 is None and t2 is None:
        return True
    if t1 is not None and t2 is not None:
        if t1.value == t2.value and isIdentical(t1.left, t2.left) and isIdentical(t1.right, t2.right):
            return True
        # else:
        #     return False
    return False
    
def solution(t1, t2):
    if t1 is None and t2 is None:
        return True
    if t1 is None:
        return False
    if t2 is None:
        return True
    if isIdentical(t1, t2):
        return True
    return (solution(t1.left, t2) or solution(t1.right, t2))
