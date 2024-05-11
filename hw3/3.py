#附註為一些小幫助，不使用全刪除也不會影響答案
from collections import deque
class Node:
    def __init__(self, value=None):
        #Node的屬性
        self.value = value
        self.left = None
        self.right = None

class Binary_search_tree:
    def __init__(self, nums: list) -> None:
        #建構樹
        self.root = Node(nums[0])
        def add(val, node):
            if (val < node.value):
                if (node.left):
                    add(val, node.left)
                else:
                    node.left = Node(val)
            else:
                if (node.right):
                    add(val, node.right)
                else:
                    node.right = Node(val)
        for num in nums[1:]:
            add(num, self.root)

    def traverse(self):
        if (self.root):
            Q = deque([self.root])
            levels = [[self.root.value]]
            temp = deque()

            while Q:
                node = Q.popleft()
                if node.left: temp.append(node.left)
                if node.right: temp.append(node.right)
                
                if not Q:
                    if temp:
                        levels.append([n.value for n in temp])
                    Q = temp
                    temp = deque()

            return levels
#處理輸入
    
nums = [int(x) for x in input().split()]
tree = Binary_search_tree(nums)
print(tree.traverse())
