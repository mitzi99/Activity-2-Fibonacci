import time
import matplotlib.pyplot as plt

FibArray = [0, 1]

n1 = 100
n2 = 200
n3 = 300
n4 = 400

x = []
y = []

def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n <= len(FibArray):
        return FibArray[n - 1]
    else:
        temp_fib = fibonacci(n - 1) + fibonacci(n - 2)
        FibArray.append(temp_fib)
        return temp_fib


def loop1():
    for i in range(n1):
        print(fibonacci(i))

def loop2():
    for i in range(n2):
        print(fibonacci(i))

def loop3():
    for i in range(n3):
        print(fibonacci(i))

def loop4():
    for i in range(n4):
        print(fibonacci(i))

# Driver Function
def run():
    start1 = time.time()
    loop1()
    end1 = time.time()
    runtime1 = end1 - start1
    x.append(n1)
    y.append(runtime1)
    print('Runtime of 100 terms: ', runtime1)
    print('')

    start2 = time.time()
    loop2()
    end2 = time.time()
    runtime2 = end2 - start2
    x.append(n2)
    y.append(runtime2)
    print('Runtime of 200 terms: ', runtime2)
    print('')

    start3 = time.time()
    loop3()
    end3 = time.time()
    runtime3 = end3 - start3
    x.append(n3)
    y.append(runtime3)
    print('Runtime of 300 terms: ', runtime3)
    print('')

    start4 = time.time()
    loop4()
    end4 = time.time()
    runtime4 = end4 - start4
    x.append(n4)
    y.append(runtime4)
    print('Runtime of 40000 terms: ', runtime4)
    print('')

run()
print(x)
print(y)

plt.plot(x,y, label='Fibonacci Sequence using Dynamic Programming')
plt.xlabel('No. of Terms')
plt.ylabel('Execution Time in Seconds')
plt.title('Fibonacci Sequence')
plt.legend()
plt.show()