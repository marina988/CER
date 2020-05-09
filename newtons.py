import math
def f(x):  ##原函数
    return(3*x + math.exp(-2*(x**2)) + 3*math.sin(x))
def g(x):  ##原函数求导
    return(3 -4*x*math.exp(-2*(x**2))+3*math.cos(x))

x=-0.15880237358200003
while (1):
    a=x
    x1=x-f(x)/g(x)
    if (abs(x-a)<(1e-8)):  ##abs()函数返回绝对值，1e-5为10的负5次方
        break
print("方程的解为：")
print(x1)
