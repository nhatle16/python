class Burger:
    def __init__(self, ingredients):
        self.ingredients = ingredients
        
    def printBurger(self):
        print(self.ingredients)

# ABSTRACT FACTORY      
class BurgerFactory:
    def createBeefBurger(self):
        ingredients = ["beef-patty", "bun", "salad"]        
        return Burger(ingredients)
    
    def createCheeseBurger(self):
        ingredients = ["cheese", "bun", "salad", "beef-patty"]
        return Burger(ingredients)
    
    def createChickenBurger(self):
        ingredients = ["chick-patty", "bun", "hot-sauce", "salad"]
        return Burger(ingredients)
    
    def createVeganBurger(self):
        ingredients = ["veggie-patty", "bun", "mayonnaise", "tomato"]    
        return Burger(ingredients)
    
burgerFactory1 = BurgerFactory()

chicken_burger = burgerFactory1.createChickenBurger()
chicken_burger.printBurger()