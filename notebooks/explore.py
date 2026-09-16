import pandas as pd
sep = r'\s+'

df = pd.read_csv("data/train_FD001.txt", sep = r'\s+', header = None)

print(df.shape)


names = ["units", "cycle", "setting_1", "setting_2", "setting_3"]

for i in range(21):
    names.append(f"sensor_{i+1}")

df.columns = names

noChangeStdColumns = []

for i in df.columns:

    # if a sensors std is less than 0.00000000001 than add it to the noChangeStdColumns list
    if df[i].std() < 1e-10:
        noChangeStdColumns.append(i)
print(f"{noChangeStdColumns}\n")
df = df.drop(columns=noChangeStdColumns)

#print(df.head)
#print(df.info)
#print(df.describe())
print(f"new columns \n \n{df.std()}")