class Card:

    def __init__(self,number,color):
        if number>0 and number<=10 and (color is "black" or color is "red"):
            self.number=number
            self.color=color

    def to_String(self):
        return (str) self.number + self.color;

    def change_Card_Number(self,number):
        self.number=number

    def function_Test_Class(self):
        pass