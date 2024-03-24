import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from display import display
import sprites 
import predict_attribute


data = pd.read_csv('/home/cropthecoder/Documents/HooHacks/twamp_data.csv')


data['is_stem'] = data['maj'].apply(lambda x: 1 if x.lower() == 'stem' else 0)

X = data[['is_stem']].values  #stem majors or not
y = data[['happiness', 'twampness', 'd_dollars', 'clubs', 'health', 'hygiene', 'caffinate', 'sleep',
          'stres', 'hours', 'study', 'clases', 'rec', 'days']].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#noramlize input features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#convert data into tensors
X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train, dtype=torch.float32)
X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
y_test_tensor = torch.tensor(y_test, dtype=torch.float32)


class NeuralNet(nn.Module):
    def __init__(self, input_size, output_size):
        super(NeuralNet, self).__init__()
        self.fc1 = nn.Linear(input_size, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, output_size)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x


input_size = X_train.shape[1]
output_size = y_train.shape[1]
model = NeuralNet(input_size, output_size)

criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

num_epochs = 100
batch_size = 32
train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

for epoch in range(num_epochs):
    for inputs, targets in train_loader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()
    #print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')


with torch.no_grad():
    predicted = model(X_test_tensor)
    test_loss = criterion(predicted, y_test_tensor)
   
#do something maybe with input
is_stem = 1  

#happiness,twampness,d_dollars,clubs,health,hygiene,name,caffinate,sleep,stres,hours,study,clases,maj,rec,days

maj_values = data['maj']
maj = maj_values[0]

caf_values = data['caffinate']
caf = caf_values[0]

health_values = data['health']
health = health_values[0]

sleep_values = data['sleep']
sleep = sleep_values[0]




#take stem or not stem majors and then play game accordingly 
def predict():
    input_data = torch.tensor(scaler.transform(np.array([[is_stem]])), dtype=torch.float32)
    predicted_attributes = model(input_data)
    print("Predicted Attributes:", predicted_attributes.detach().numpy())



def major(major):
    if maj == "stem":
        return True
        
        #display coffee
    else:
        return False
        #don't display coffee 

#Given a major predict different major "attributes"
#display a character that represents the given major 


def main():
    predict()
    #major(maj)
    #print("running")
    #display(sprites.boy_1)

    if major(maj):

        
        if predict_attribute.gender_val == 1:
            display(sprites.girl_1, sprites.tom)
        else:
            display(sprites.boy_2, sprites.tom)
    else:

        if predict_attribute.gender_val == 1:
            display(sprites.girl_1)
        else:
            display(sprites.boy_2)
            #display(sprites.tom)

if __name__ == "__main__":
    main()

