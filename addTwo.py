# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
      
        dummy = p = ListNode(None)
        s = 0
        # 当l1和l2都为空时，若s>10,则s//10=1需进位，不写s!=0，会少一位数
        while l1 or l2 or s != 0:
            # 更新s
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            # 取余数
            p.next = ListNode(s % 10)
            # 移动p到下一个位置
            p = p.next
            # 若l1非空，移动到下一个位置
            if l1: l1 = l1.next
            # 若l2非空，移动到下一个位置
            if l2: l2 = l2.next
            # s更新，向下取整
            s = s // 10

        return dummy.next
