from data import MENU, resources

profit = 0


def is_resource_sufficient(order_ingredients):
    #  Вовзращает Правду,если на заказ хватает ресурсов, ложь если нет
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f'-Sorry there is not enough {item}. Pleas come back later!')
            return False
    return True


def process_coins():
    # Фунция возвращает сумму всех вложенных монет
    print("Please insert coins. ")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How mane pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    # Функция проверки, хватает ли вложенных монет на покупку напитка, вовзращает Ложь если монет не хватает
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is $ {change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that is not enough money/ Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    # Отнимаем то количество продуктов, которое затратили на изготовление заказа
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️.Enjoy!")


is_on = True

# Запускаем кофе машину
while is_on:
    choice = input("-What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off" or choice == "stop":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])


