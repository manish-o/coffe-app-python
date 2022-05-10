
print('Welcome to coffee shop')
print('Choose your item by entering it\'s number, for multiple itmes, enter it with a space ')
items = [

	'0 - Burger',
	'1 - Cookies',
	'2 - Latte Frappucino',
	'3 - Mocha Cafe',
	'4 - Tea',
	'5 - Brownies'

]
extra = [

	'0 - Hazel Nut dust',
	'1 - Extra foam',
	'2 - Whipped cream',
	'3 - Choco swirl',
	'4 - Expresso Blast',
	'5 - Cinnamon dust'

]
size = [

	'0 - Large',
	'1 - Medium',
	'2 - Small'

]

for i in items:
	print(i)

user = input("Your item numbers - ")
order = user.split()
for j in range(0, len(order)):
	order[j] = int(order[j])
bill = []
for k in order:
	print('Your order ', items[k])
	bill.append(items[k])
print('Choose your extras in the same way')
for o in extra:
	print(o)

user1 = input("Your item numbers - ")
order1 = user1.split()
for c in range(0, len(order1)):
	order1[c] = int(order1[c])

for q in order1:
	print('Your extras ', extra[q])
	bill.append(extra[q])

print('Choose your coffee size')
for p in size:
	print(p)

order2 = int(input('Enter your cup size '))
print('Your cup size', size[order2])
bill.append(size[order2])
print(bill)
total = []
price = {'0 - Burger': 30, '1 - Cookies': 10, '2 - Latte Frappucino':70, '3 - Mocha Cafe':60, '4 - Tea':50, '5 - Brownies':40, '0 - Hazel Nut dust':5, '1 - Extra foam':2, '2 - Whipped cream':7, '3 - Choco swirl':8, '4 - Expresso Blast':10, '5 - Cinnamon dust':5, '0 - Large':20, '1 - Medium':10, '2 - Small':5}
for g in bill:
	print(price[g])
	total.append(price[g])
total1 = sum(total)
print('Your total bill amount is ', total1)
print("How many people do you want to split the bill for ?")
option = int(input())
print('Each of you have to pay', total1/option)
total2 = total1/option
print('Your token number is - ')
import random
token = random.randint(1, 99)
print(token)
customer =  {'Order':bill, 'Price':total1, 'Split price':total2, "Token":token}
print(customer) 