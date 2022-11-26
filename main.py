# Code By Ishan Srivastava - Classic Chatbot 
# Python3
import time

y = []

#################### Sorting Algorithm Below ####################
def sort():
    #x = words.index(i)
   # print(x)
    if i == 'and':
        y.append(i)
        print( "removing word 'and' ") 

    elif i == 'please':
        y.append(i)
        print( "removing word 'please' ")

    elif i == 'tell':
        y.append(i)
        print( "removing word 'tell' ")

    elif i == 'can':
        y.append(i)
        print( "removing word 'can' ")

    elif i == 'you':
        y.append(i)
        print( "removing word 'you' ")

    elif i == 'is':
        y.append(i)
        print( "removing word 'is' ")

    elif i == 'a':
        y.append(i)
        print( "removing word 'a' ")
        
    elif i == 'an':
        y.append(i)
        print( "removing word 'an' ")
    else:
        print(f"no worries in word '{i}'")
    print("ignored words list: ", y)


def format_list():
    print("")
    print("Sorting..")
    for i in y:
        try:
            words.remove(i)
        except ValueError:
            pass


#################### Taking INPUT Below ####################

user_inp = input("Input: ")
#print(f"input = {user_inp}")
user_low = user_inp.lower()
print(f"lower_case: {user_low}")

user_split = user_low.split()
print(f"split: {user_split}")

words = user_split
print(words)

for i in user_split:
   # print(i)
    print(" ")
    print("Validating")
    time.sleep(0.8)
    sort()
    #print(words)

format_list()
time.sleep(3)
#print("split = ",user_split)

#################### Comparision Starts ####################

if words[0] == 'what':
    time.sleep(3)
    print("")
    print("FOUND THE WORD 'what'")
    time.sleep(2)
    #print(words[0]," ",words[1])
    print("Bag Of Words = ",words)
    print("")
    print("Will send To Main loop of What Now...... Under Construction ;)")
else:
    time.sleep(2)
    print("I Don't Know that :(")

