master_dict = {}

total_fat = 0
total_carbs = 0
total_pro = 0


def fat_func():
    while True:
        fat = input('How many grams of fat were there in this food item?\n')
        if fat.isnumeric():
            macro_lst.append(int(fat))
            break
        else:
            print('Please only use numbers')
def carbs_func():
    while True:
        carbs = input('How many grams of carbs were there in this food item?\n')
        if carbs.isnumeric():
            macro_lst.append(int(carbs))
            break
        else:
            print('Please only use numbers')
def protein_func():
    while True:
        protein = input('How many grams of protein were there in this food item?\n')
        if protein.isnumeric():
            macro_lst.append(int(protein))
            break
        else:
            print('Please only use numbers')

        
while True:
    macro_lst = []
    food_item = input('What is the name of the food you ate?\nWrite "done" to stop\n')
    if food_item.lower() == 'done':
        break 
    fat_func()
    carbs_func()
    protein_func()
    while True:
        servings = float(input('How many servings did you consume?\n'))
        if isinstance(servings, float) == True:
            res = [i * servings for i in macro_lst]
            break
        else:
            print('Please use a value number of servings/n')
    master_dict[food_item] = res

for v in master_dict.values():
    for q in v:
        if v.index(q) == 0:
            total_fat += int(q)
        elif v.index(q) == 1:
            total_carbs += int(q)
        else:
            total_pro += int(q)


total_fat = total_fat * 9
total_carbs = total_carbs * 4
total_pro = total_pro * 4
total_cal = total_fat + total_carbs + total_pro
print('Total Calories: {0}'.format(total_cal))
print('Intake Percentages:\nFat {0}% Carbs {1}% Protein {2}%'.format((total_fat / total_cal)*100, (total_carbs / total_cal)*100, (total_pro / total_cal)*100))



# add way to check if already in dictionary
    
    


    
