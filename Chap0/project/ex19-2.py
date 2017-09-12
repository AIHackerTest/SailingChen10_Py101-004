# coding=utf-8

def order_stats(total_orders, total_returns):
    print ("You have %d orders" % total_orders)
    print ("You have %d returns" % total_returns)
    print ("You net sales are %d - %d" % (total_orders, total_returns))
    print ("Hopefully you had a good month!\n")

# simple arguments
order_stats(4321, 1234)

# math
order_stats(102+321, 456*4)

# variables
jims_sales = 395
sally_sales = 72
joan_sales = 5481
returns = 32
order_stats(jims_sales + sally_sales + joan_sales, returns)

# variables and math
order_stats((jims_sales*4) + (sally_sales % 4) + (joan_sales % 4), returns)

# assign the function to a variable?
order_totals = order_stats
order_totals(30, 1)

# with a variable number of arguments - a la *args?
var_stats = (560, 42)
order_stats(*var_stats)

# function to function?
def func_to_func():
    value1 = 20
    value2 = 30
    order_stats(value1, value2)
func_to_func()

# user input - Don't forget to specify a type of input! In this case an integer
print ("How much did you sell this month?")
user_sales = int(input('>>>'))
order_stats(user_sales, returns)
