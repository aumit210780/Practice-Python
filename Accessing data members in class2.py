class Card:
    def __init__(self,num,color):
        self.number = num
        self.color = color
card1 = Card(1,"red")
print(card1.number,card1.color)
card1.number = 7
print("New value = ",card1.number)
card2 = Card(2,"green")
print(card2.number,card2.color)
        
       