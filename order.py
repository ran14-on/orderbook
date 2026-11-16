class Order:
    def __init__(self, side,item,amount,price,user,sequence):
        self.side = side
        self.item = item
        self.amount = amount
        self.price = price
        self.user = user
        self.sequence = sequence
o = Order("buy", "apple",1,5, "alice",1)
print(o.side)