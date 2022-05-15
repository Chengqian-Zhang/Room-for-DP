import pandas as pd
path = r'/root/li0new/1244681/000tri/lcurve1.out'
data = pd.read_csv(path)
df = pd.DataFrame(data)
a=[]
for i in range(0,len(df),20):##每隔20行取数据
    a.append(i)
file = df.iloc[a]
f = pd.DataFrame(file)
f.to_csv(r'/root/li0new/1244681/000tri/lcurve.copy.out', index=False,encoding='utf_8_sig')
print('ok')
