#!/usr/bin/env python3

import numpy as  np
import scipy.stats as st
import sklearn.linear_model as lm
import matplotlib.pyplot as plt
def f(x):
    return np.exp(3*x)

x_tr = np.linspace(0., 2, 200)
y_tr = f(x_tr)

x = np.array([0,.1,.2,.5,.8, .9,1])
y = f(x) + 2 * np.random.randn(len(x))
# create model
lrp =  lm.LinearRegression()
fig, axs = plt.subplots(1,1,figsize=(6,3))
ax = axs[0]
ax.plot(x_tr, y_tr, '--k')

for deg, s in zip([2,5], ['-', '.']):
    lrp.fit(np.vander(x, deg+1),y)
    y_lrp = lrp.predict(np.vander(x_tr,deg+1))
    ax.plot(x_tr, y_lrp, s, label=f'degree {deg}')
    ax.legend(loc=2)
    ax.set_xlim(0, 1.5)
    ax.set_ylim(-10, 80)
    print(f'Coefficients,degree {deg}:\n\t', ' '.join(f'{c:.2f}' for c in lrp.coef_))
ax.plot(x,y,'ok',ms=10)
ax.set_title("Linear regresson")
plt.show()
