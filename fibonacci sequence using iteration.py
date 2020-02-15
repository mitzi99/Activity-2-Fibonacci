import time
import matplotlib.pyplot as plt

i1 = 15
i2 = 20
i3 = 25
i4 = 30

x2 = []
y2 = []

def fibo(nterms):
    # first two terms
    fs = 0
    ss = 1
    count = 0
    # check if the number of terms is valid
    if nterms == 1:
       print("Fibonacci sequence upto", nterms, ":")
       print(fs)
    else:
       print("Fibonacci sequence:")
       while count < nterms:
           print(fs)
           nth = fs + ss
           # update
           fs = ss
           ss = nth
           count += 1

def iteration1():
    print("")
    for i in range(i1):
        print(fibo(i))

def iteration2():
    print("")
    for i in range(i2):
        print(fibo(i))

def iteration3():
    print("")
    for i in range(i3):
        print(fibo(i))

def iteration4():
    print("")
    for i in range(i4):
        print(fibo(i))

#Driver Function
def execution_iteration():
    ite_start1 = time.time()
    print("Fibonacci Sequence of 15 terms:")
    iteration1()
    ite_stop1 = time.time()
    ite_runtime1 = ite_stop1 - ite_start1
    print('Runtime of 15 terms: ', ite_runtime1)
    x2.append(i1)
    y2.append(ite_runtime1)
    print("")

    ite_start2 = time.time()
    print("Fibonacci Sequence of 20 terms:")
    iteration2()
    ite_stop2 = time.time()
    ite_runtime2 = ite_stop2 - ite_start2
    print('Runtime of 20 : ', ite_runtime2)
    x2.append(i2)
    y2.append(ite_runtime2)
    print("")

    ite_start3 = time.time()
    print("Fibonacci Sequence of 25 terms:")
    iteration3()
    ite_stop3 = time.time()
    ite_runtime3 = ite_stop3 - ite_start3
    print('Runtime of 25 terms: ', ite_runtime3)
    x2.append(i3)
    y2.append(ite_runtime3)
    print("")

    ite_start4 = time.time()
    print("Fibonacci Sequence of 30 terms:")
    iteration4()
    ite_stop4 = time.time()
    ite_runtime4 = ite_stop4 - ite_start4
    print('Runtime of 30 terms: ', ite_runtime4)
    x2.append(i4)
    y2.append(ite_runtime4)
    print("")

    print('Number of terms: ', x2)
    print('Runtime of number of terms respectively: ', y2)

execution_iteration()

plt.plot(x2,y2, label='Fibonacci Iteration')
plt.xlabel('No. of Terms')
plt.ylabel('Execution Time in Seconds')
plt.legend()
plt.show()
