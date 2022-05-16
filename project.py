import pandas as pd
import plotly_express as pe
import numpy as np

data = pd.read_csv("project.csv")

score = data["TOEFL Score"].tolist()
chance = data["Chance of Admit "].tolist()

graph = pe.scatter(x = score , y = chance)
#graph.show()

# ---------------------------- Hit & Trial -------------------

# -------------------- assuming m = 1 & c = 0 ----------------------------------

m = 1
c = 0
y = []

for x in score :
    yValue = (m * x ) + c
    y.append(yValue)

graph = pe.scatter( x = score , y = chance)
graph.update_layout(shapes = [
    dict(
        type = "line",
        y0 = min(y), y1 = max(y),
        x0 = min(score), x1 = max(score)
    )
    
])

#graph.show()

x = 166
y = m * x + c

print("------------------------------------------------------")
print("Chance Of Admission of a person of Score using Hit & Trial Method - ", x , " is : " , y)


# ---------------------------- Will find m & c using Algorithm -------------------

score_array = np.array(score)

chance_array = np.array(chance)

m , c = np.polyfit(score_array , chance_array , 1)

print("-----------------------------------------")
print("m - " , m , " c - " , c)


y = []

for x in score :
    yValue = (m * x ) + c
    y.append(yValue)

graph = pe.scatter( x = score_array , y = chance_array)
graph.update_layout(shapes = [
    dict(
        type = "line",
        y0 = min(y), y1 = max(y),
        x0 = min(score_array), x1 = max(score_array)
    )
    
])

graph.show()

x = 166
y = m * x + c

print("------------------------------------------------------")
print("Chance Of Admission of a person of Score using Algorithm - ", x , " is : " , y)

























































