import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

# Step 1: Load the data from the CSV file
data = pd.read_csv('/home/cropthecoder/Documents/HooHacks/twamp_data.csv')

# Step 2: Preprocess the data if necessary
# Assuming the 'maj' column contains information about the major
# Create a new column indicating whether the major is STEM or not
data['is_stem'] = data['maj'].apply(lambda x: 1 if x.lower() == 'stem' else 0)

# Step 3: Select features and target variable
X = data[['is_stem']].values  # Feature: whether the major is STEM or not
y = data[['happiness', 'twampness', 'd_dollars', 'clubs', 'health', 'hygiene', 'caffinate', 'sleep',
          'stres', 'hours', 'study', 'clases', 'rec', 'days']].values

# Step 4: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Normalize the input features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Convert data into PyTorch tensors
X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train, dtype=torch.float32)
X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
y_test_tensor = torch.tensor(y_test, dtype=torch.float32)

# Step 6: Define the neural network model
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

# Step 7: Initialize the model
input_size = X_train.shape[1]
output_size = y_train.shape[1]
model = NeuralNet(input_size, output_size)

# Step 8: Define loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Step 9: Train the model
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
    print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# Step 10: Evaluate the model
with torch.no_grad():
    predicted = model(X_test_tensor)
    test_loss = criterion(predicted, y_test_tensor)
    print('Test Loss:', test_loss.item())

# Step 11: Make predictions
# For example, to predict multiple attributes for a student with a STEM major:
is_stem = 1  # Assume the major is STEM
input_data = torch.tensor(scaler.transform(np.array([[is_stem]])), dtype=torch.float32)
predicted_attributes = model(input_data)
print("Predicted Attributes:", predicted_attributes.detach().numpy())



