# -*- coding: utf-8 -*-
class Solution:
    def removeZeroSumSublists(self, head):
        """
        Initialise dummy head with current head
        Initialise cummulative sum variable
        A dictionary to keep track of cumsum across all the heads
        """
        curr = head
        cumsum = 0
        sum_dict = {}
        while curr:
            cumsum += curr.val
            if cumsum == 0:
                """
                If cummulative sum is 0 so we have to delete all the nodes
                previous to this including the current node
                so we set current to next 
                and delete all the nodes starting from the orignal head to the current head
                
                and reinitialise all the variables and the dictionary
                """
                curr = curr.next
                while head != curr:
                    delNode = head
                    head = head.next
                    del delNode
                curr = head
                cumsum = 0
                sum_dict = {}
            elif cumsum in sum_dict:
                """If current cummulative sum is already present in the dictionary that means we have to
                   delete all the nodes between previous occurance of current sum and current node including 
                   
                   So first we start from the previous node, assign current to the next
                   and we start deleting from previous until we have reached the current
                """
                prv = sum_dict[cumsum]
                curr = curr.next
                while prv.next != curr:
                    delNode = prv.next
                    prv.next = delNode.next
                    del delNode
                curr = head
                cumsum = 0
                sum_dict = {}
            else:
                """
                If the sum is not present we store it with respect to the current node
                """
                sum_dict[cumsum] = curr
                curr = curr.next
        return head