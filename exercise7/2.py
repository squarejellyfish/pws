class Student:
    def __init__(self, name, next):
        # TODO: set attributes
        self.name = name
        self.next = next
        
    def __str__(self):
        return f'{self.name} {self.next or ""}' 
      
def remove_naughty(head, target):
    # TODO: finish function return Student object
    if (head.name == target and not head.next):
        return ""
    if (head.name == target):
        return head.next

    prev, curr = head, head.next
    while curr:
        if (curr.name == target):
            prev.next = curr.next
            break
        prev = curr
        curr = curr.next
        
    return head
    
# the class and function will be used as follows:
lst = input().split()
target = input()
tail = Student(lst[-1], None)
for i in range(len(lst) - 2, -1, -1):
    head = Student(lst[i], tail)
    tail = head
if len(lst) == 1:
    head = tail
print(remove_naughty(head, target))

