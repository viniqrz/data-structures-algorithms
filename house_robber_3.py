# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def solution_dp(treeRoot):
    
    def dp(root):
        if not root:
            return [0,0]
        
        left = dp(root.left)
        right = dp(root.right)
        
        res = [0,0]
        
        res[0] = max(left[0], left[1]) + max(right[0], right[1])
        res[1] = root.val + left[0] + right[0]
        
        return res
    
    res = dp(treeRoot)
    
    return max(res[0], res[1])

##      3
##      /\
##     2  3
##    /\  /\
##   0  3 0 1 


# Input: root = [3,2,3,null,3,null,1]
# Output: 7
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

print(solution_dp(TreeNode(3, TreeNode(2, 0, TreeNode(3)), TreeNode(3, 0, TreeNode(1)))))
