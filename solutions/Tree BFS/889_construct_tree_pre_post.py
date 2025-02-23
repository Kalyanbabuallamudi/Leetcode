# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(pre_start, pre_end, post_start, post_end):
            if pre_start > pre_end:
                return None
            if pre_start == pre_end:
                return TreeNode(preorder[pre_start])

            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            left_root_val = preorder[pre_start + 1]
            left_subtree_size = postorder.index(left_root_val) - post_start + 1

            root.left = build(pre_start + 1, pre_start + left_subtree_size, post_start, post_start + left_subtree_size - 1)
            root.right = build(pre_start + left_subtree_size + 1, pre_end, post_start + left_subtree_size, post_end - 1)

            return root

        n = len(preorder)
        return build(0, n - 1, 0, n - 1)


# This Code is Contributed by Kalyan Babu Allamudi