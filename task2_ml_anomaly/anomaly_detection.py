import numpy as np
from sklearn.ensemble import IsolationForest

response_time=[120, 125, 118, 130, 122,
    127, 124, 121, 129, 126,
    123, 128, 125, 122, 131,
    700, 127, 119, 650, 124]

X=np.array(response_time).reshape(-1,1) #as its in 1 d
model=IsolationForest(contamination=0.1,random_state=42)

model.fit(X)
predictions=model.predict(X)

print("-----response time anomaly detection------")
for val,p in zip(response_time,predictions):
    if p==-1:
        print("ANAMOLY DETECTED",val)
    else:
        print("Normal",val)


#-----------matplotlib-----------------
