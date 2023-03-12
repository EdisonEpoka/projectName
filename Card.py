class Card:

    def __init__(self,number,color):
        if number>0 and number<=10 and (color is "black" or color is "red"):
            self.number=number
            self.color=color