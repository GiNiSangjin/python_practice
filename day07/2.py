import numpy as np
a=[1,3,2,8,4]
print(sum(a)/len(a))
x=np.array(a)
print(np.mean(x))

print(np.zeros(1) )
print(np.zeros(7))

print(np.zeros((3,4)))
print(np.ones((3,4)))

print(np.full(3,8))

print(np.full((3,4),8))

print(np.arange(10))

print(np.arange(4,20))

print(np.arange(2,152,2))

print(np.linspace(0,25,10))

print(np.linspace(0,25,10, endpoint=False))

x = np.arange(2,11)
print(x)
print(x.size)
print(x.shape)
print(x.ndim)
print(x.mean())
X = x.reshape(3,3)
print(X)
print(X.size)
print(X.shape)
print(X.ndim)
print(X.mean())

X= np.random.randint(1,100,(2,5))
print(X)

x = X.reshape(10)
print(x)
print(x.ndim)
x = X.reshape(1,10)

y = np.arange(5,5+25).reshape(5,5)
print(y)

print(np.random.random((2,3)))

print(np.random.randint(1,6))
 

x=np.random.randint(0,100,10)
print(x)
print(x[2])

X =np.array([[ 13,  22,  49,  42,  80],
       [ 91,  63,  58,  20,  34],
       [ 60,  40,  16,  37,  66],
       [  2,  44,  16,  87, 100]])

print(X)

Y=X[0:1+1,0:2+1]
print(Y)

#실습
# X=5x5 ndarray를 1~25까지 정수 / Y= Boolean indexing을 이용해서 홀수만 뽑아서 배열로 만들기
X = np.arange(1,26).reshape(5,5)  
Y= X[X%2==1]
print(Y)