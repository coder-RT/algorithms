#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def hasSol(root, sum, curr):
    if root is None:
        return False
        
    curr += root.value
    
    if curr == sum and root.left is None and root.right is None:
        return True
    
    return hasSol(root.left, sum, curr) or hasSol(root.right, sum, curr)

def solution(t, s):
    return hasSol(t, s, 0)
