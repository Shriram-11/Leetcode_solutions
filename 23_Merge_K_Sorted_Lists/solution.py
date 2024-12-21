# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if lists==[]:
            return None
        if len(lists)==1:
            return lists[0]
        l=[]
        for a in lists:
            while a:
                l.append(a.val)
                a=a.next
        l.sort()
        r=ListNode(0)
        res=r
        for a in l:
            res.next=ListNode(a)
            res=res.next
        return r.next
