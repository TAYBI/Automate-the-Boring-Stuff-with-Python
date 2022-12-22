import pyinputplus as pyip


menu = {
    'wheat': 7,
    'white': 8,
    'sourdough': 9,
    'chicken': 37,
    'turkey': 40,
    'ham': 42,
    'tofu': 30,
    'cheddar': 2,
    'Swiss': 2,
    'mozzarella': 2,
    'mayo': 1,
    'mustard': 1,
    'lettuce': 1,
    'tomato': 1
}
order = []
price = 0

bread = pyip.inputMenu(['wheat', 'white',  'sourdough'])
order.append(bread)

protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])
order.append(protein)

cheeseYesNo = pyip.inputYesNo("Do want cheese?\n>")
if cheeseYesNo == 'yes' or cheeseYesNo == 'y':
    cheeseType = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'])
    order.append(cheeseType)

mayoYesNo = pyip.inputYesNo("Do want mayo?")
if mayoYesNo == 'yes' or mayoYesNo == 'y':
    mayoType = pyip.inputMenu(['mayo', 'mustard', 'lettuce', 'tomato'])
    order.append(mayoType)

print('-------------Your Order-------------')
for item in order:
    print(item, ': ', menu[item], '$')
    price += menu[item]

print('--------------------------')
print('Total: ', price, '$')
print('--------------------------')
