import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    heap = []
    # Initalize Heap - O(k * log(k))
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i))
    dummy = ListNode(-1)
    curr = dummy
    # let n be the number of all the elemnts. numeber of iterations = n
    # each iteration adding one element to heap - O(k) total O(n * log(k))
    while heap:
        minval, i = heapq.heappop(heap)
        newNode = ListNode(minval)
        curr.next = newNode
        curr = curr.next
        lists[i] = lists[i].next
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i))
    return dummy.next