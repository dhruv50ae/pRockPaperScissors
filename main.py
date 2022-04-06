import random

namesString = input("Give me everybody's names, seperated by a comma. ")
names = namesString.split(',')

numItems = len(names)
randomChoice = random.randint(0, numItems-1)
personWhoWillPay = names[randomChoice]
print(f"{personWhoWillPay} is going to buy the meal today.")
