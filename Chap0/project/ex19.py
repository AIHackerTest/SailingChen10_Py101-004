# coding=utf-8

# creates a function called "cheese_and_crackers" with to arguments,
# "cheese_count" and "boxes_of_crackers"
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# prints the value of "cheese_count"
    print("You have %d cheeses!" % cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
# prints a string
    print("Man that's enough for a party!")
#prints a string
    print("Get a blanket.\n")
#prints a string
print ("We can just give the function number drectly:")
# calls the function "cheese_and_crackers" with argument value of 20 and 30
cheese_and_crackers(20, 30)

#prints a string
print ("OR, we can use variables from our script:")
# creates variable "amount_of_cheese" with value "10" and "amount_of_cracers" with value "50"
amount_of_cheese = 10
amount_of_crackers = 50
# call the function "cheese_and_crackers" with arguments set to the variables
# "amount_of_cheese" and "amount_of_crackers", whose values respectively arguments
# set to "10" and "50"
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print ("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print ("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
