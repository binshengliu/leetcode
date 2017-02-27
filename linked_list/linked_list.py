class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def list_to_linked_list(val):
    if not val:
        return None

    ret = ListNode(0)
    current = ret
    for c in val:
        current.next = ListNode(c)
        current = current.next
    return ret.next

def linked_list_to_list(linked):
    l = []
    c = linked
    while c != None:
        l.append(c.val)
        c = c.next
    return l

def print_linked_list(msg, l):
    print(msg)
    while l != None:
        print(l.val, end=' ', flush=True)
        l = l.next
    print('\n')

