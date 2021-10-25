import pandas as pd

data = pd.read_csv("MyData.csv")

df = data.sort_values(by = ["User_ID","Date"], ascending=[False,True])
sorted_user = df[["User_ID"]]
user_arr = sorted_user.values

step = []
j = 1
for i in range(0, len(user_arr)):
    if i == 0:
        step.append(j)
    else:
        user = user_arr[i]
        if user == user_arr[i-1]:
            j +=1
            step. append(j)
        else:
            j = 1
            step.append(j)
df["step"] = step