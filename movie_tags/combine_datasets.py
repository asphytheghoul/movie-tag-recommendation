import pandas as pd
df1 = pd.read_csv("mpst_full_data_001.csv")
df2 = pd.read_csv("mpst_full_data_002.csv")
df = pd.concat([df1, df2], ignore_index=True)
df.to_csv("mpst_full_data_v1.csv", index=False)
if len(df)==14828:
    print("Success!")
else:
    print("Error!")
    
