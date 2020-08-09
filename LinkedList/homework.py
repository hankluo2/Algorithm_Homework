"""
@file homework.py
@author hankluo2
@date 2020-8-9
@desc homework to linked list
"""
import NodeClass

def length(head: NodeClass.Node) -> int:
    cursor = head
    count = 0
    while cursor != None:
        count += 1
        cursor = cursor.next
    return count


def deleteKth(head: NodeClass.Node, k: int):
    if k > length(head):
        print('error: k out of range')
        return None
    cursor = NodeClass.Node('', head)
    i = 0
    while cursor != None:
        if i + 1 == k:
            break
        cursor = cursor.next
        i += 1
    probe = cursor.next
    cursor.next = probe.next
    del probe


def visitList(head: NodeClass.Node):
    cursor = head
    while cursor != None:
        yield cursor.data
        cursor = cursor.next


if __name__ == '__main__':
    dataList = list(input().split())
    k = int(input())
    head = NodeClass.LinkedBag(dataList)
    head = head._items
    # print(type(head))
    print(length(head))
    deleteKth(head, k)
    iter = visitList(head)
    for i in iter:
        print(i, end=' ')
    print()
    
    lb = NodeClass.LinkedBag(dataList)
    print(type(lb), type(head))