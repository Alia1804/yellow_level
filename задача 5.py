class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersection(headA: ListNode, headB: ListNode) -> ListNode:
    if not headA or not headB:
        return None

    pA, pB = headA, headB

    while pA is not pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA

    return pA

