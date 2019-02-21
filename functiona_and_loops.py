
#functions eg:

'''
 1. define a function
 2. call a function
'''

# deifining a function
def addition(a, b):
    if a != '' and b != '':
        return a + b
    else:
        print("found null values")


#. calling a function
sum = addition(3, 4)
print(sum)



#while loops

counter = 0

while counter < 10:
    print("in while loop")
    counter += 1


#for loops

for value in range(0, 10):
    print("in for loop")



# as I was talking in the class about global variables
# we should use a global keyword in order to use that
# variable in spacific funcitons.


balance = 0

def deposit(money):
    # The below declaration lets the function know that we
    # mean the global 'balance' when we refer to that variable, not
    # any local variable

    global balance
    balance += money
    print("successfully deposited money: " + money)



deposit(100)

