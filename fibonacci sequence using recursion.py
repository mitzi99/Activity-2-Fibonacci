import time
import matplotlib.pyplot as plt

n1 = 15
n2 = 20
n3 = 25
n4 = 30

x = []
y = []

def fibo_recursion(n):
    if n <= 1:
        return n
    else:
        return (fibo_recursion(n-1)+fibo_recursion(n-2))

def recur1():
    print("")
    for i in range(n1):
        print(fibo_recursion(i))

def recur2():
    print("")
    for i in range(n2):
        print(fibo_recursion(i))

def recur3():
    print("")
    for i in range(n3):
        print(fibo_recursion(i))

def recur4():
    print("")
    for i in range(n4):
        print(fibo_recursion(i))

#Drive Function
def execution_time():
    start1 = time.time()
    print("Fibonacci Sequence of 15 terms:")
    recur1()
    stop1 = time.time()
    runtime1 = stop1 - start1
    print('Runtime of 15 terms: ', runtime1)
    x.append(n1)
    y.append(runtime1)
    print("")

    start2 = time.time()
    print("Fibonacci Sequence of 20 terms:")
    recur2()
    stop2 = time.time()
    runtime2 = stop2 - start2
    print('Runtime of 20 : ', runtime2)
    x.append(n2)
    y.append(runtime2)
    print("")

    start3 = time.time()
    print("Fibonacci Sequence of 25 terms:")
    recur3()
    stop3 = time.time()
    runtime3 = stop3 - start3
    print('Runtime of 25 terms: ', runtime3)
    x.append(n3)
    y.append(runtime3)
    print("")

    start4 = time.time()
    print("Fibonacci Sequence of 30 terms:")
    recur4()
    stop4 = time.time()
    runtime4 = stop4 - start4
    print('Runtime of 30 terms: ', runtime4)
    x.append(n4)
    y.append(runtime4)
    print("")

    print('Number of terms: ', x)
    print('Runtime of number of terms respectively: ', y)

execution_time()


plt.plot(x , y, label='Fibonacci Recursion')
plt.xlabel('No. of Terms')
plt.ylabel('Execution Time in Seconds')
plt.title('Fibonacci Sequence')
plt.legend()
plt.show()