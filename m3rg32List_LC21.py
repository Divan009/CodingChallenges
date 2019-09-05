#defn for singly linked list

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def merge2List(self, l1, l2):
		#create a new LL ptr  
		curr = dummy = ListNode(0)

		while l1 and l2:
			if l1.val < l2.val:
				curr.next = l1
				l1 = l1.next
			else:
				curr.next = l2
				l2 = l2.next
			curr = curr.next
		curr.next = l1 or l2

		return dummy.next

# Runtime: 28 ms, faster than 31.53% of Python online submissions for Merge Two Sorted Lists
# Memory Usage: 11.7 MB, less than 89.66% of Python online submissions for Merge Two Sorted Lists.

#NEW BETTER


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(None)
        prev = l3

    # while both ll arent empty
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                prev.next = l1
                #print(prev.next)
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        #once we reach the end of a ll, append the other list
        #because we know its already sorted

        if l1 == None:
            prev.next = l2
        elif l2 == None:
            prev.next = l1

        return l3.next