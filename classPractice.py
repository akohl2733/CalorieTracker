# create class to handle variables
class Nutrition:
    def __init__(self, name, fat, carb, protein, servings):
        self.name = name
        self.fat = fat
        self.carb = carb
        self.protein = protein
        self.servings = servings

    def cals(self):
        return (int(self.fat) * 9 + int(self.carb) * 4 + int(self.protein) * 4) * int(self.servings)
    

# create function to check for appropriate responses
macros = []   
def check(macro):
        while True:
            n = input(f"How many grams of {macro} did you consume?\n")
            try:
                  macros.append(int(n))
                  break
            except:
                print('Please only use whole numbers!')

# initialize final list and calories       
calories = 0
lst = []

# create loop to continuously ask for inputs of foods and macros
while True:
    name = input('\nWhat item of food did you eat?\n(enter "done" to end)\n')
    if name == 'done':
         break
    check('fat')
    check('carbs')
    check('protein')
    s = int(input('how many servings did you have?\n'))
    food = Nutrition(name, macros[0], macros[1], macros[2], s)
    lst.append(food)

# figure out total calories and macros
for x in lst:
    print(x.name)
    calories = calories + x.cals()
print('Total Calories: ' + str(calories))