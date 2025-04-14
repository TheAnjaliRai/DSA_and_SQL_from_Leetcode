# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """

        if not preorder or not postorder:
            return None

        root = TreeNode(preorder[0])
        if len(preorder)==1:
            return root
        
        left_sub_root = preorder[1]
        left_sub_size = postorder.index(left_sub_root) +1
        root.left = self.constructFromPrePost(preorder[1:left_sub_size+1],postorder[:left_sub_size])
        root.right = self.constructFromPrePost(preorder[left_sub_size+1:],postorder[left_sub_size:-1])
        return root
        