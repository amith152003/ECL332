import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0,10,0.1)
v=np.sin(t)
b=v+1
plt.plot(t,b)
plt.grid()
plt.xlabel("time")
plt.ylabel("amp")
plt.suptitle("SINE WAVE")





