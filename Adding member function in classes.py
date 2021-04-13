class Card:
    def __init__(self,num,color):
        self.number = num
        self.color = color
    def printer(self):
        print("Number: {} and Color: {}".format(self.number,self.color))
card1 = Card(1,"red")
card1.printer()
card1.number = 7
card1.printer()
card2 = Card(2,"green")
card2.printer()