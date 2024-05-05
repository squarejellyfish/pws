class Phonebook:
    def __init__(self):
        self.book = dict()

    def search(self, info):
        if (info in self.book):
            return self.book[info]
        else:
            return f"Cannot find {info}"

    def add(self, name, phone):
        self.book[name] = phone
        self.book[phone] = name

# We will judge your code with the following scripts

pbook = Phonebook()
while True:
    args = input().split()
    if args[0] == "end": break
   
    if args[0] == "s":
        print(pbook.search(args[1]))
    elif args[0] == "a":
        pbook.add(args[1], args[2])




