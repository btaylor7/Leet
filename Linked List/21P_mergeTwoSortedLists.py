#Program to merge two sorted lists.


class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
     
def mergeLists(list1, list2):
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    if list1.val < list2.val:
        list1.next = mergeLists(list1.next, list2)#Sets list1.next as head of the merged list.
        return list1
    else:
        list2.next = mergeLists(list1, list2.next)
        return list2
     