def func():
 list1=[1, 3, 4, 2, 3, 4, 5, 7, 9, 4, 3]
 list2=[]

 for i in list1:
     if list1.count(i)==1:
         list2.append(i)
 print(list2)

def func1():
 list=[1, 5, 0, 7, 0, 3, 0]
 for i in range(len(list)):
     if list[i]!=0:
         print(list[i], end=' ')
 for i in range(list.count(0)):
         print(0,end=' ')

def func2():
 my_num = {num:num**3 for num in range(1, 21)}
 print(my_num)

def func3():
 a = [i for i in range(1, 150)if i%15 == 0]
 print(a)

def runner(*args):
    if len(args) == 0:
        func()
        func1()
        func2()
        func3()
    else:
        for i in args:
            globals()[i]()

runner()
runner('func1')
runner('func2', 'func3')