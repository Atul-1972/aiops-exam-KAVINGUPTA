import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

free_memory = [2048, 2040, 2050, 2035, 2045, 2038, 2042, 2040, 2046, 2039, 120, 2044, 2041, 2043, 2037, 85, 2045, 2039, 2042, 2040]
X=np.array(free_memory).reshape(-1,1)

model=IsolationForest(contamination=0.1,random_state=42)
model.fit(X)
predictions=model.predict(X)

for val,p in zip(free_memory,predictions):
    if p==-1:
        print("yes anomaly",val)
    else:
        print("Normal",val)

plt.plot(free_memory,label="free_memory")
plt.title("Free Memory Anomaly Detection")
plt.xlabel("index")
plt.ylabel("free_memory")
plt.legend()
plt.show()
plt.savefig("free_memory_anomaly_detection.png")


