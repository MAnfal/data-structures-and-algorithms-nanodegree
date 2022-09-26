class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def convert_list_linked_list(_list):
    _llist = LinkedList()

    for item in _list:
        _llist.append(item)

    return _llist


def convert_list_to_set(llist, _set=None):
    if _set is None:
        _set = set()

    temp_head = llist.head

    _set.add(temp_head.value)

    while temp_head.next:
        temp_head = temp_head.next
        _set.add(temp_head.value)

    return _set


def union(llist_1, llist_2):
    union_set = convert_list_to_set(llist_1)
    union_set = convert_list_to_set(llist_2, union_set)

    return convert_list_linked_list(union_set)


def intersection(llist_1, llist_2):
    _set_1 = convert_list_to_set(llist_1)
    _set_2 = convert_list_to_set(llist_2)

    _final_set = set()

    for item_1 in _set_1:
        if item_1 in _set_2:
            _final_set.add(item_1)

    return convert_list_linked_list(_final_set)


linked_list_1 = convert_list_linked_list([3, 2, 4, 35, 6, 65, 6, 4, 3, 21])
linked_list_2 = convert_list_linked_list([6, 32, 4, 9, 6, 1, 11, 21, 1])

print(union(linked_list_1, linked_list_2)) # 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 ->
print(intersection(linked_list_1, linked_list_2)) # 4 -> 21 -> 6 ->

linked_list_3 = convert_list_linked_list([3, 2, 4, 35, 6, 65, 6, 4, 3, 23]) # 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 ->
linked_list_4 = convert_list_linked_list([1, 7, 8, 9, 11, 21, 1]) # ''

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))
