class Burger:
    def __init__(self):
        self.bun = None
        self.cheese = None
        self.patty = None
        
    def setBun(self, bunStyle):
        self.bun = bunStyle
        
    def setPatty(self, pattyStyle):
        self.patty = pattyStyle
        
    def setCheese(self, cheeseStyle):
        self.cheese = cheeseStyle
        
# BUILDER PATTERN
class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()
        
    def addBun(self, bunStyle):
        self.burger.setBun(bunStyle)
        return self
    
    def addPatty(self, pattyStyle):
        self.burger.setPatty(pattyStyle)
        return self
    
    def addCheese(self, cheeseStyle):
        self.burger.setCheese(cheeseStyle)
        return self
    
    def builder(self):
        return self.burger
    
burger = BurgerBuilder().addBun("sesame").addCheese("swiss cheese").addPatty("chick-patty").builder()