class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #Get the length of the listNode
        length, node = 0, head
        while node:
            length=length+1
            node = node.next
        
        #Perform the deletion operation
        index, node = length-n, head
        if index>0:
            while index>0:
                index=index-1
                lastnode=node
                node=node.next
            if node.next:
                node.val = node.next.val
                node.next = node.next.next
            else:
                lastnode.next=None
        else:
            if head.next:
                head.val = head.next.val
                head.next = head.next.next
            else:
                head=None
        
        return head