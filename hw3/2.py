class PerpetualInventory:
    def __init__(self, beg_inv):
        #beg_inv 為期初存貨的變數
        self.inv = beg_inv
        self.payable = 0
        self.entries = []
    def purchases(self, x):
        self.inv += x
        self.payable += x
        self.entries.append([f"Inventory                   {x:,}", f"    Accounts Payable            {x:,}"])
    def purchases_return(self, x):
        self.inv -= x
        self.payable -= x
        self.entries.append([f"Accounts Payable            {x:,}", f"    Inventory                   {x:,}"])
    def sales(self, x, y):
        self.inv -= y
        self.entries.append([f"Accounts Receivable         {x:,}", f"    Sales Revenue               {x:,}", f"Cost of Goods Sold          {y:,}", f"    Inventory                   {y:,}"])
    def stock_take(self, x):
        diff = x - self.inv
        if (diff < 0):
            self.entries.append([f"Cost of Goods Sold          {abs(diff):,}", f"    Inventory                   {abs(diff):,}"])
        elif (diff > 0):
            self.entries.append([f"Inventory                   {abs(diff):,}", f"    Cost of Goods Sold          {abs(diff):,}", ])
        self.inv = x
    def inv_show(self):
        print(f"{self.inv:,}")
    def entry_show(self):
        for line in self.entries[-1]:
            print(line)

#We will judge your code using following scripts
while True:
    try:
        cmd, *args = input().split()
        if cmd == "beginning_inventory":
            beg_inv = int(args[0])
            inventory = PerpetualInventory(beg_inv)
        elif cmd == "purchases":
            inventory.purchases(int(args[0]))
        elif cmd == "purchases_return":
            inventory.purchases_return(int(args[0]))
        elif cmd == "sales":
            inventory.sales(int(args[0]),int(args[-1]))
        elif cmd == "stock_take":
            inventory.stock_take(int(args[0]))
        elif cmd == "inv_show":
            inventory.inv_show()    
        elif cmd == "entry_show":
            inventory.entry_show()
    except EOFError:
        break

