#!/usr/bin/env python
# Python3


"""计算fibonacci数列，消耗多少时间"""


import time
import wmi


def fib(n):
    if n == 2 | n == 1:
        return 1
    first = 1
    second = 1
    loop = 3
    result = 2
    while loop <= n:
        result = first + second
        first = second
        second = result
        loop = loop + 1
    return result


def fib_recursion(n):
    if n == 2 | n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


c = wmi.WMI ()
for sys in c.Win32_OperatingSystem():
    print("Version:%s" % sys.Caption.encode("UTF8"),"Vernum:%s" % sys.BuildNumber)
    print(sys.OSArchitecture)
    # print(sys.NumberOfProcesses) #当前系统运行的进程总数

for processor in c.Win32_Processor():
    print("Process Name: %s" % processor.Name.strip())
for Memory in c.Win32_PhysicalMemory():
    print("Memory Capacity: %.fMB" %(int(Memory.Capacity)/1048576))


begin = time.time()
loop_result = fib(1000000)
end = time.time()
print("loop time: %f" % (end-begin))


begin = time.time()
recursion_result = fib_recursion(1000000)
end = time.time()
print("recursion time: %f" % (end-begin))

if loop_result == recursion_result:
    print("loop_result and recursion_result is equal")
    # print("result is:")
    # print(loop_result)
else:
    print("loop_result and recursion_result is not equal")
    # print("loop_result:")
    # print(loop_result)
    # print("recursion_result:")
    # print(recursion_result)
