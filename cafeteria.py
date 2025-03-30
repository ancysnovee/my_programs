class Node:
    def __init__(self,data):
        self.data = data
        self.link= None

class add_order:
    def __init__ (self):
        self.head = None
        self.orders=[]
        
    def add_order(self,order):
        self.orders.append(order)

    def receive(self):
        if not self.orders:
            return None
        return self.orders.pop(0)
    
    def history(self,order):
        if order is None:  # ✅ Prevent adding None to history
            return "No orders left to store in history."
        new_node = Node(order)
        if self.head is None:
            self.head = new_node
        else:
           new_node.link = self.head
           self.head = new_node
        n = self.head
        while n is not None:
            print(f"{n.data} -->", end = " ")
            n = n.link
        print("None")


ord = add_order()
ord.add_order("apple")
ord.add_order("banana")
ord.add_order("coffee")
received_order = ord.receive()
print("Received:", received_order)
print("history:")
ord.history(received_order)
received_order = ord.receive()
print("Received:", received_order)
print("history:")
ord.history(received_order)
received_order = ord.receive()
print("Received:", received_order)
print("history:")
ord.history(received_order)
