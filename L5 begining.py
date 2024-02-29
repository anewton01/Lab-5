#the authors' names are Abby Newton and Sydney Eidelbes
x = 2
if x < 3:
 print("Small")
x=5
if x < 3:
 print("Small")
score = 8 #A score on a 10 point quiz
if score > 6:
 print("Nice work!")

 #predict: 3,6,9,12,15
for i in range(1,16):
 if i % 3 == 0:
     print(i, " is divisible by 3.")
#adapt
number=int(input("What is your number?"))
if number%2 == 0:
           print("Even")

x = 2
if x < 3:
    print("Small")
else:
    print("Large")
x=5
if x < 3:
    print("Small")
else:
    print("Large")
score = 8 #A score on a 10 point quiz
if score < 6:
    print("Needs improvement")
elif score < 9:
    print("Nice work!")
else:
    print("Excellent!")

#predict: -1 and -2 neg, 0 zero, 1 and 2 pos
for i in range(-2,3):
    if i < 0:
        print(i, " is negative.")
    elif i == 0:
        print(i, " is zero.")
    else:
        print(i, " is positive.")

#adapt
number=int (input("What is your number?"))
if number%2==0:
    print("Even")
else:
    print("Odd")

print(3<4)
print(4>2)
type(True)

if True:
    print("This text will always appear.")
if False:
    print("This text will not appear.")
#predict: Bool, False
type(False)
print(3==5)

#adapt
number=int(input("What is your number?"))
def greaterthan10(number):
    if number>10:
        return True
    else:
        return False
