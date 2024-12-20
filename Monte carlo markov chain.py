import numpy as np
import random
import matplotlib.pyplot as plt

# read user input
n = int(input('Number of states: '))
V = [0] * n
for i in range(n):
    V[i] = float(input(f'The probability of being in state {i + 1} initially is: '))
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == j: a[i][j] = float(input(f'The probability of staying in state {i + 1} is: '))
        else: a[i][j] = float(input(f'The probability of transitioning from state {i + 1} to state {j + 1} is: '))

m = int(input('Number of transitions: '))

# matrix multiplication
t = tm = np.array(a, dtype = float).T
for i in range(m - 1):
    tm = np.dot(tm, t)

res = tm.dot(np.array(V, dtype = float))

print('Results of matrix multiplication')
for i in range(n):
    print('The probability of being in state {} is {:.10f}'.format(i + 1, res[i]))

# monte carlo simulation
SIZE = 100000
v = V[:]
for i in range(m):
    state = 0
    freq = [0] * n
    for j in range(SIZE):
        cur = 0
        s = random.random()
        for k in range(n):
            cur += v[k]
            if s < cur:
                state = k
                break
        
        cur = 0
        s = random.random()
        for k in range(n):
            cur += a[state][k]
            if s < cur:
                state = k
                break
        freq[state] += 1
    for j in range(n):
        v[j] = freq[j] / SIZE

print('Result of Monte Carlo simulation')
for i in range(n):
    print('The probability of being in state {} is {:.10f}'.format(i + 1, v[i]))

# graph
SIZE = 100000
x, y = [[0] * (m + 1) for i in range(n)], [[0] * (m + 1) for i in range(n)]
v = V[:]
for i in range(m+1):
    state = 0
    freq = [0] * n
    for j in range(SIZE):
        cur = 0
        s = random.random()
        for k in range(n):
            cur += v[k]
            if s < cur:
                state = k
                break

        cur = 0
        s = random.random()
        for k in range(n):
            cur += a[state][k]
            if s < cur:
                state = k
                break
        freq[state] += 1
    for j in range(n):
        x[j][i] = i
        y[j][i] = v[j]
        v[j] = freq[j] / SIZE

x = np.array(x)
y = np.array(y)
for i in range(n):
  plt.plot(x[i], y[i])
  plt.ylim(0,1)
  plt.title('State ' + str(i + 1))
  plt.xlabel('Number of transitions')
  plt.ylabel("Probability of being in state " + str(i+1))
  plt.show()
