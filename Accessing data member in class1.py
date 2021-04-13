class Cards:
    def __init__(self):
        print("I am called")
        print(self)
        self.a = 5
        self.number = 1
        self.color = "Blue"
        print(self)
card1 = Cards()
print(card1)
print(card1.number,card1.color,card1.a)
        