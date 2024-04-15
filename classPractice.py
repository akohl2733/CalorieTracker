class Nutrition:
    def __init__(self, name, fat, carb, protein, servings):
        self.name = name
        self.fat = fat
        self.carb = carb
        self.protein = protein
        self.servings = servings

    def cals(self):
        return (int(self.fat) * 9 + int(self.carb) * 4 + int(self.protein) * 4) * int(self.servings)
    
def check(n):
        try:
             n = int(n)
        except:
            print('please use only numbers.')

calories = 0
lst = []
while True:
    name = input('food\n')
    f = int(input('How many grams of FAT are there per serving?\n'))
    check(f)
    c = input('How many grams of CARBS are there per serving?\n')
    check(c)
    p = input('How many grams of PROTEIN are there per serving?\n')
    check(p)
    s = int(input('how many servings did you have?\n'))
    food = Nutrition(name, f, c, p, s)
    lst.append(food)
    print('Press enter for next food, type "done" to end.')
    if input().lower() == 'done':
        break
for x in lst:
    calories = calories + x.cals()
print(calories)