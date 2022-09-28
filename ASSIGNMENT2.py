#1.Wapp to find those numbers which are divisible by 7 and multiple of 5,
#between 1500 and 2700 (both included).
'''
for i in range(1500,2700):
    if i%7==0 and i%5==0:
        print(i)
'''
#2. We are having 3 list like this
#Colors = [“Yellow”,”Green”,”White”,”Black”]
#Fruits=[“Apple”,”Papaya”,”Mango”,”Orange”]
#Animals=[“Tiger”,”Lion”,”Deer”,”Zebra”]
#i. Write a program that asks user to enter a Color/Fruit/Animal name and it should tell which category belongs to , like its is a fruit or color or Animal
#ii. Write a program that asks user to enter two items and it tells you if they both are in same category or not.
#For example if I enter yellow and Black, it will print "Both are colors" but if I enter yellow and Tiger it should print "They don't belong to same category"
'''
Colors = ['Yellow','Green','White','Black']
Fruits=['Apple','Papaya','Mango','Orange']
Animals=['Tiger','Lion','Deer','Zebra']

user=input('enter a colours,fruits and animals name:')
if user in Colors:
    print('it is a colour')
elif user in Fruits:
    print('it is a fruit')
elif user in Animals:
    print('it is a animal')
else:
    print('please choose from the catagorey,thank u')
'''

#3.Write a python program that can tell you if your grade score good or not . Normal Score range is 40 to 60.
  #i. Ask user to enter his score.
  #ii. If it is below 40 to 60 range then print that score is low
  #iii. If it is above 60 then print that it is good otherwise print that it is normal
'''
user=eval(input('enter ur grade score mark :'))
if user<40:
    print(f'{user} that mark is low')
elif user>60:
    print(f'{user} that mark is good')
else:
    print(f'{user}that is normal score')
'''
#4.After appearing in exam 10 times you got this result,
#result = ["Pass","Fail","Fail","Pass","Fail","Pass","Pass","Fail","Fail","Fail"]
#Using for loop figure out how many times you got Pass
'''
count=0
result = ["Pass","Fail","Fail","Pass","Fail","Pass","Pass","Fail","Fail","Fail"]
for i in result:
    if i=='Pass':
        count=count+1
print(count)
'''

#5.Lets say you are running a 50 km race. Write a program that,
#Upon completing each 10 km asks you "are you tired?"
#If you reply "yes" then it should break and print "you didn't finish the race"
#If you reply "no" then it should continue and ask "are you tired" on every km
#if you finish all 50 km then it should print congratulations message
'''
for i in range(1,51):
    if i%10==0:
        n=input('are you tired :')
        if n=='yes':
            print('you did not finish the race')
            break
    if i==50:
        print('congratulations')
'''

#6.Print square of all numbers between 10 to 20 except even numbers
'''
for i in range(10,21):
    if i%2==0:
        continue
    print(i*i)
'''

#7.Your Marks for five Test(test1 to test5) looks like this,
#marks_list = [65, 75, 2100, 95, 83]
#Write a program that asks you to enter marks and program should tell you in which test that marks occurred. If marks is not found then it should print that as well.
'''
test_list=['test1','test2','test3','test4','test5']
marks_list = [65, 75, 2100, 95, 83]
marks=int(input('enter ur mark:'))
for i in range(5):
    if marks==marks_list[i]:
        print('this is the marks of',test_list[i])
        break
else:
 print('does not match the marks')
'''


































