class Student:
    def __init__(self, name, next):
        self.name = name
        self.next = next
        
    def __str__(self):
        return f'{self.name} {self.next or ""}' 
      
def reverse_students(head):
    # TODO: finish function return Student object
    prev, curr = None, head
    while (curr):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev
    
    
# the class and function will be used as follows:
lst = input().split()
tail = Student(lst[-1], None)
for i in range(len(lst) - 2, -1, -1):
    head = Student(lst[i], tail)
    tail = head
if len(lst) == 1:
    head = tail
print(reverse_students(head))

