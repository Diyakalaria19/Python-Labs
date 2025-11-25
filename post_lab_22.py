#question 1
# import pandas as pd 
# df = pd.read_csv("sample_data.csv")   
# print(df.dtypes) 

#question 2
import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [30, None, 35, None]
}
df = pd.DataFrame(data)
print("Original Data:")
print(df)
df['Age'] = df['Age'].fillna(df['Age'].mean())

print("\nData After Filling Missing Values:")
print(df)
