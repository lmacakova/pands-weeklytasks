import matplotlib.pyplot as plt
import numpy as np
def h(n):
    return n**3
x=np.arange(0,11)
y=h(x)

normalThousand = np.random.normal(5, 2, 1000)

plt.hist(normalThousand, bins=50, alpha=0.5, color='b', edgecolor='black', linewidth=1.2, label='Normal Distribution of 1000 numbers, mean=5, stand. dev.= 2')
plt.plot(y, label="h(x)=x^3", color='r')
plt.ylabel("Frequency")

plt.legend()
plt.grid(True)
plt.show()


