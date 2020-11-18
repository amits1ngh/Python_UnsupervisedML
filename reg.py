from statistics import mean
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
import random

style.use('fivethirtyeight')

# xs = np.array([1,2,3,4,5,6], dtype=np.float64)
# ys = np.array([5,4,6,5,6,7], dtype=np.float64)

def generate_data(hm, variance, step=2, correlation=False):
    val = 1
    ys = []
    for i in range(hm):
        y =  val + random.randrange(-variance, variance)
        ys.append(y)
        if correlation == 'pos':
            val+=step
        elif correlation == 'neg':
            val -= step
    xs = [i for i in range(len(ys))]
    print(ys)


    return np.array(xs, dtype=np.float64), np.array(ys, dtype=np.float64)



def get_slope(xs,ys):
    m = (mean(xs)*mean(ys) - mean(xs*ys))/((mean(xs))**2 - mean(xs**2))
    b = mean(ys) - m*mean(xs)
    return m, b

def calculate_coefficient(ys_orig, ys_line):
    mean_ys_line = [mean(ys_orig) for _ in ys_orig]
    squared_error_mean_ys = mean((ys_orig - mean_ys_line)**2)
    squared_error_reg_ys = mean((ys_orig - ys_line)**2)
    coefficient = 1 - (squared_error_reg_ys/squared_error_mean_ys)
    return coefficient

xs, ys = generate_data(40, 10, 2, correlation='neg')

m,b = get_slope(xs, ys)
regressionline = [(m*x)+b for x in xs]

coefficient = calculate_coefficient(ys, regressionline)
predict_x = 8
predict_y = (m*predict_x) + b


print(coefficient)


plt.plot(xs, regressionline)
plt.scatter(xs,ys)
plt.scatter(predict_x, predict_y, s=100, color='r')
plt.show()
