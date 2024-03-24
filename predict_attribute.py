import csv
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import pandas as pd

#get values from csv
data = []
with open('training_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  #don't read first line
    for row in reader:
        data.append(row)


names = [row[0] for row in data]
genders = [row[1] for row in data]

X = [[len(name)] for name in names]

le = LabelEncoder()
y = le.fit_transform(genders)

#split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = RandomForestClassifier()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
data = pd.read_csv('/home/cropthecoder/Documents/HooHacks/twamp_data.csv')
X = [[len(name)] for name in data['name']]

#predict gender from csv
predicted_genders = clf.predict(X)
predicted_genders = le.inverse_transform(predicted_genders)

for name, predicted_gender in zip(data['name'], predicted_genders):
    print(f"Name: {name}, Predicted Gender: {predicted_gender}")

gender_val = 0 

def get_gender(predicted_gender):
    if predicted_gender == "male":
        gender_val = 0
        return gender_val
        
    else:
        gender_val = 1
        return gender_val

print(get_gender(predicted_gender))

