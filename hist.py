import numpy as np
import matplotlib.pyplot as plt

golf = np.array([110,107,121,137,87,92,104,129,98,99,139,82,105,100,114,122,109,94,106,111])

plt.hist(golf, range=[80,140], bins=6)
plt.grid(True)
plt.show()