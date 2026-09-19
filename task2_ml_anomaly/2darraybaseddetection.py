import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

response_time=[[30, 45], [32, 46], [31, 44], [33, 47], [32, 45],
               [95, 99], [34, 48], [31, 44], [33, 46], [91, 95],
               [30, 47], [34, 46], [31, 45], [33, 46]]

X=np.array(response_time)
model=IsolationForest(contamination=0.1,random_state=42)
model.fit(X)
predictions=model.predict(X)

for val,p in zip(response_time,predictions):
    if p==-1:
        print("Anomaly detected",val)
    else:
        print("Normal",val)

plt.plot(response_time,label="response_time")
plt.title("Response Time Anomaly Detection (2D Array)")
plt.xlabel("index")
plt.ylabel("response_time")
plt.legend()
plt.savefig("response_time_anomaly_detection_2darray.png")
plt.show()


