import pandas as pd

data = pd.read_csv("C:/Users/yuno/Desktop/데이터시각화/MyData_final.csv")

a = input("이전 Veune입력: ")
b = input("이후 Venue입력: ")
c = a+"-"+b
d = ''
df = data[["Loc_Plus","shape"]]
for i in range(0,len(df)):
    if (c==df.iloc[i,0]):
        d = df.iloc[i,1]
        break
my_frame = pd.DataFrame({"shape_count":data["shape"].value_counts()})
df3 = data[["shape","Post_Venue","next_venue"]]
df4 = df3[df3['shape'] ==d]
print(d)
shape_count = my_frame.loc[d]
print(shape_count)
print(df4["next_venue"].value_counts(normalize=True)*100)