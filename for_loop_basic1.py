# Basic - Print all integers from 0 to 150.

for num in range (0,151):
   print(num)


# Multiples of Five - Print all the multiples of 5 from 5 to 1,000

for mult5 in range (5, 1001, 5):
   print(mult5)


# Counting, the Dojo Way - Print integers 1 to 100.
# If divisible by 5, print "Coding" instead.
# If divisible by 10, print "Coding Dojo".

for count in range (1,101):
    if count % 10 == 0:
        print("Coding Dojo")
    elif count % 5 == 0:
        print("Coding")


# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
countup = 0
while countup <= 500000:
    print(countup)
    countup += 1

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for countdown in range (2018,0,-4):
    print(countdown)

# Flexible Counter - Set three variables: lowNum, highNum, mult.
# Starting at lowNum and going through highNum, print only the integers that are a multiple of mult.
# For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

lowNum = 7
highNum = 50
mult = 4

for num in range (lowNum,highNum):
    if num % mult == 0:
        print(num)
