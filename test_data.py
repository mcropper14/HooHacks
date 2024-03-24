import pandas as pd

data = {
    'name': ['John', 'Jane', 'Alice', 'Bob', 'Harry'],
    'gender': ['male', 'female', 'female', 'male', 'male']
}
df = pd.DataFrame(data)
df.to_csv('training_data.csv', index=False)
