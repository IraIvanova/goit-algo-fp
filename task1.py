from linked_list import LinkedList, Node


def reverse_linked_list(llist):
    curr = llist.head
    prev = None

    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    llist.head = prev

def insertion_sort(llist):
    curr = llist.head
    sorted_head = None

    while curr is not None:
        curr_next = curr.next
        sorted_head = sorted_insert(sorted_head, curr)
        curr = curr_next

    llist.head = sorted_head


def sorted_insert(sorted_head, item):
    if sorted_head is None or sorted_head.data >= item.data:
        item.next = sorted_head
        return item

    current = sorted_head

    while current.next is not None and current.next.data < item.data:
        current = current.next

    item.next = current.next
    current.next = item

    return sorted_head

def merge_sorted_linked_lists(llist1: LinkedList, llist2: LinkedList):
    new_llist = LinkedList()

    curr1 = llist1.head
    curr2 = llist2.head

    while curr1 is not None and curr2 is not None:
        if curr1.data <= curr2.data:
            new_llist.insert_at_end(curr1.data)
            curr1 = curr1.next
        else:
            new_llist.insert_at_end(curr2.data)
            curr2 = curr2.next

    while curr1 is not None:
        new_llist.insert_at_end(curr1.data)
        curr1 = curr1.next

    while curr2 is not None:
        new_llist.insert_at_end(curr2.data)
        curr2 = curr2.next

    return new_llist


if __name__ == "__main__":
    llist = LinkedList()

    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)
    llist.insert_at_end(20)
    llist.insert_at_end(25)

    print("\nInitial Linked List: ")
    llist.print_list()

    print("\nReversed Linked List: ")
    reverse_linked_list(llist)
    llist.print_list()

    print("\nInsertion sort: ")
    insertion_sort(llist)
    llist.print_list()

    print("\nMerging Sorted Linked Lists: ")
    list1 = LinkedList()
    list2 = LinkedList()

    list1.insert_at_beginning(5)
    list1.insert_at_end(10)
    list1.insert_at_end(15)

    list2.insert_at_beginning(4)
    list2.insert_at_end(8)
    list2.insert_at_end(9)
    list2.insert_at_end(10)
    list2.insert_at_end(25)
    list2.insert_at_end(30)
    merged_list = merge_sorted_linked_lists(list1, list2)
    merged_list.print_list()