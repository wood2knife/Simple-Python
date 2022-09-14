def buy_coffee(material):
    print('What do you want to buy?')
    print('1 - espresso,')
    print('2 - latte,')
    print('3 - cappuccino,')
    coffee = input('back - to main menu: ')
    flag = True
    water_espresso = 250
    coffee_beans_espresso = 16
    money_espresso = 4
    water_latte = 350
    milk_latte = 75
    coffee_beans_latte = 20
    money_latte = 7
    water_cappuccino = 200
    milk_cappuccino = 100
    coffee_beans_cappuccino = 12
    money_cappuccino = 6
    if coffee == '1':
        if material[0] - water_espresso >= 0:
            if material[2] - coffee_beans_espresso >= 0:
                if material[3] - 1 >= 0:
                    material[0] -= water_espresso
                    material[2] -= coffee_beans_espresso
                    material[3] -= 1
                    material[4] += money_espresso
                else:
                    flag = False
                    print('Sorry, not enough disposable cups!')
            else:
                flag = False
                print('Sorry, not enough coffee beans!')
        else:
            flag = False
            print('Sorry, not enough water!')
        if flag:
            print('I have enough resources, making you a coffee!')
    elif coffee == '2':
        if material[0] - water_latte >= 0:
            if material[1] - milk_latte >= 0:
                if material[2] - coffee_beans_latte >= 0:
                    if material[3] - 1 > 0:
                        material[0] -= water_latte
                        material[1] -= milk_latte
                        material[2] -= coffee_beans_latte
                        material[3] -= 1
                        material[4] += money_latte
                    else:
                        flag = False
                        print('Sorry, not enough disposable cups!')
                else:
                    flag = False
                    print('Sorry, not enough coffee beans!')
            else:
                flag = False
                print('Sorry, not enough milk!')
        else:
            flag = False
            print('Sorry, not enough water!')
        if flag:
            print('I have enough resources, making you a coffee!')
    elif coffee == '3':
        if material[0] - water_cappuccino >= 0:
            if material[1] - milk_cappuccino >= 0:
                if material[2] - coffee_beans_cappuccino >= 0:
                    if material[3] - 1 > 0:
                        material[0] -= water_cappuccino
                        material[1] -= milk_cappuccino
                        material[2] -= coffee_beans_cappuccino
                        material[3] -= 1
                        material[4] += money_cappuccino
                    else:
                        flag = False
                        print('Sorry, not enough disposable cups!')
                else:
                    flag = False
                    print('Sorry, not enough coffee beans!')
            else:
                flag = False
                print('Sorry, not enough milk!')
        else:
            flag = False
            print('Sorry, not enough water!')
        if flag:
            print('I have enough resources, making you a coffee!')
    return material


def fill_coffee(material):
    water_fill = int(input('Write how many ml of water do you want to add: '))
    milk_fill = int(input('Write how many ml of milk do you want to add: '))
    coffee_beans_fill = int(input('Write how many grams of coffee beans do you want to add: '))
    disposable_cups_fill = int(input('Write how many disposable cups of coffee do you want to add: '))
    material[0] += water_fill
    material[1] += milk_fill
    material[2] += coffee_beans_fill
    material[3] += disposable_cups_fill
    return material


def money_coffee(material):
    print('I gave you $%d' % material[4])
    material[4] = 0
    print()
    return material[4]


def remaining_coffee(material):
    print('The coffee machine has:')
    print('%d of water' % material[0])
    print('%d of milk' % material[1])
    print('%d of coffee_beans' % material[2])
    print('%d of disposable cups' % material[3])
    print('$%d of money' % material[4])


material = [400, 540, 120, 9, 550]
action = input('Write action (buy, fill, take, remaining, exit): ')
while action != 'exit':
    if action == 'buy':
        buy_coffee(material)
    elif action == 'fill':
        fill_coffee(material)
    elif action == 'take':
        money_coffee(material)
    elif action == 'remaining':
        remaining_coffee(material)
    action = input('Write action (buy, fill, take, remaining, exit): ')
