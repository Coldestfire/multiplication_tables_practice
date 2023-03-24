import time

x = input("Tables of Which Number: ")
print(" ")



i=1
correct_answers = 0
wrong_answers = 0



while i<11:
    print(str(x) + " X " + str(i) + " = ")

    answers = int(input())

    if answers == int(i)*int(x):
        print("Correct")
        print("-------------------")
        correct_answers += 1
    else:
        print("Wrong")
        print("Answer is " + str(int(i)*int(x)))
        print("-------------------")
        wrong_answers += 1

    i = i + 1


#Results
if correct_answers == 10:
    print("Awesome!!! You got all of them Correct!!!")

else:
    print("You got " + str(correct_answers) + " Correct and " + str(wrong_answers) + " Wrong")
    
time.sleep(3)
