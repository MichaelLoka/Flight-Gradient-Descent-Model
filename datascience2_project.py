# -*- coding: utf-8 -*-
"""DataScience2 Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cpLdmGschJ8q3l-lMDOtCune0IuMiVIt

## **Describe Data**
"""

import pandas as pd
df = pd.read_csv('/content/Flight_Dataset.csv')
df

print(df.describe())
df.info()

"""## **Data visualization**"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset into a Pandas DataFrame
df = pd.read_csv("Flight_Dataset.csv")

# Compute the distribution of flight classes
class_counts = df['class'].value_counts()

# Create a horizontal bar chart
colors = ['tab:blue', 'tab:red']

plt.barh(class_counts.index, class_counts.values,color=colors)
plt.title('Class Type')
plt.xlabel('Count')
plt.ylabel('Class')
plt.show()

# chart 2 Pie Chart
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/content/Flight_Dataset.csv')
arrival_counts = df['arrival_time'].value_counts()
labels = arrival_counts.index.tolist()
sizes = arrival_counts.tolist()
colors = ['#ff9999', '#66b3ff', '#99ff99',"#F7DC6F", '#ffcc99', '#ffb3e6']
plt.pie(sizes, labels=labels,colors=colors, autopct='%1.1f%%')
plt.show()

# chart 3
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('Flight_Dataset.csv')

# Sort the DataFrame by flight duration in descending order
df_sorted = df.sort_values(by='price', ascending=False)

# Extract the flight duration and price columns for the top, bottom, and middle flights
top_flights = df_sorted.head(200)
bottom_flights = df_sorted.tail(200)
middle_flights = df_sorted.iloc[int(
    len(df_sorted)/4)-100:int(len(df_sorted)/4)+100]

# Extract flight duration and price for the top, bottom, and middle flights
top_duration = top_flights['duration']
top_price = top_flights['price']/1000
bottom_duration = bottom_flights['duration']
bottom_price = bottom_flights['price']/1000
middle_duration = middle_flights['duration']
middle_price = middle_flights['price']/1000

# Create a scatter plot
plt.scatter(bottom_duration, bottom_price,
            color='red', alpha=0.5, label='Bottom 200')
plt.scatter(top_duration, top_price,
            color='blue', alpha=0.5, label='Top 200')
plt.scatter(middle_duration, middle_price,
            color='green', alpha=0.5, label='Middle 200')

# Add labels and title to the plot
plt.xlabel('Flight Duration (In Hours)')
plt.ylabel('Flight Price (In Thousands)')
plt.title('Flight Duration vs. Price')

# Set the step size for the price axis to 5000
plt.yticks(range(0, int(max(df['price']/1000))+10, 10))

# Set the step size for the duration axis to 2
plt.xticks(range(0, int(max(df['duration']))+2, 2))
plt.xlim(xmax=30)

# Add a legend to the bottom right corner
plt.legend(loc='lower right', fontsize=10)

# Add gridlines
plt.grid(True, linestyle='--', alpha=0.5)

# Set a background color
plt.gca().set_facecolor('#f2f2f2')

# Remove the top and right spines
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Adjust the plot layout
plt.tight_layout()

# Display the plot
plt.show()

# chart 4 two histograms
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Flight_Dataset.csv")
fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(12, 5), sharey=True)
ax1.hist(df['source_city'], bins=30, alpha=0.99, label='Source City')
ax2.hist(df['destination_city'], bins=30, alpha=0.99, label='Dstination City')
ax1.legend(loc='upper right')
ax1.set_xlabel('source city')
ax1.set_xticks([1, 2, 3, 4, 5,6])
ax1.tick_params(axis='x', labelsize=8, pad=10)
ax1.set_ylabel('source city')
ax2.legend(loc='upper right')
ax2.set_xticks([1, 2, 3, 4, 5,6])
ax2.tick_params(axis='x',labelsize=8, pad=10)
ax2.set_xlabel('distnation city')
ax2.set_ylabel('distnation city')
plt.title('Source And Distnation City Distribution')
plt.show()

# chart 5
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('Flight_Dataset.csv')

# Create a box plot of flight prices by airline
plt.figure(figsize=(10, 6))  # Set the figure size

# Use seaborn for improved aesthetics
sns.boxplot(data=df, x='airline', y='price', palette='Set3')

# Add labels and title to the plot
plt.xlabel('Airline', fontsize=12)
plt.ylabel('Price', fontsize=12)
plt.title('Flight Prices by Airline', fontsize=14)

# Customize the plot aesthetics
sns.set_style("whitegrid")  # Set the style of the plot
sns.despine()  # Remove the top and right spines
plt.grid(axis='y', linestyle='--', alpha=0.5)  # Add horizontal gridlines
plt.ylim(bottom=0)  # Set the y-axis lower limit to 0

# Adjust the plot layout
plt.tight_layout()

# Display the plot
plt.show()

"""## **Data Wrangling And Cleaning**"""

!pip install category_encoders
import pandas as pd
import category_encoders as ce

# Load the dataset into a Pandas DataFrame
df = pd.read_csv('/content/Flight_Dataset.csv')
df = df.rename(columns={'Unnamed: 0': 'ID'}) # rename the 'Unnamed: 0' column to 'ID'
print(df)

# Convert the array to a categorical data type
df['class'] = pd.Categorical(df['class'])
df['flight'] = pd.Categorical(df['flight'])
df['airline'] = pd.Categorical(df['airline'])
df['stops'] = pd.Categorical(df['stops'])
df['departure_time'] = pd.Categorical(df['departure_time'])
df['arrival_time'] = pd.Categorical(df['arrival_time'])
df['source_city'] = pd.Categorical(df['source_city'])
df['destination_city'] = pd.Categorical(df['destination_city'])


# Create TargetEncoder object for specific columns
te = ce.TargetEncoder(cols=['class','flight','airline','stops','departure_time','arrival_time','source_city','destination_city'])
# Fit and transform the selected columns
df[['class','flight','airline','stops','departure_time','arrival_time',"source_city",'destination_city']] = te.fit_transform(
    df[['class','flight','airline','stops','departure_time','arrival_time',"source_city",'destination_city']], df['price'])

print(df)

# Calculate the correlation matrix
corr_matrix = df.corr()
# Print the correlation matrix
print(corr_matrix)

"""## **Regression algorithm using Gradient Descent**"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import r2_score

class MyGradient:
    def __init__(self, X_matrix, Y_vector, Weight):
        self.X_matrix = X_matrix
        self.Y_vector = Y_vector
        self.Weight = Weight

    def gradient_descent(self, Learning_rate, num_iters):
            # Number of training examples
            m = len(self.Y_vector)
            # History of cost function values during optimization
            J_history = {}
            for i in range(num_iters):
                # Calculate the hypothesis
                h = self.X_matrix.dot(self.Weight)
                # Calculate the error between the hypothesis and the target values
                errors = h - self.Y_vector
                # Calculate the gradient
                gradient = self.X_matrix.T.dot(errors) / m
                # Update the parameters
                self.Weight -= Learning_rate * gradient
                # Calculate the cost function
                J = np.sum((self.X_matrix.dot(self.Weight) - self.Y_vector) ** 2) / (2 * m)
                # Store cost function value and weight vector in history
                J_history[J] = self.Weight.copy()

            lowest_J = min(J_history)
            self.Weight = J_history[lowest_J]

            return self.Weight, J_history



# Extract the relevant features and target variable
y = df['price'].values
df = df.drop(['price', 'ID'], axis=1)
X = df.values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the input features and target variable using MinMaxScaler
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
y_train_scaled = scaler.fit_transform(y_train.reshape(-1, 1)).ravel()
y_test_scaled = scaler.transform(y_test.reshape(-1, 1)).ravel()
#The ravel() method flattens the 2D array and we must reshape bec. its 1D array

# Add a column of ones to X for the bias term
X_train_scaled = np.hstack((np.ones((len(X_train_scaled), 1)), X_train_scaled))
X_test_scaled = np.hstack((np.ones((len(X_test_scaled), 1)), X_test_scaled))

# Set up hyperparameter tuning

learning_rates = [0.1 , 0.01 , 0.001]
num_iters_list = [100 , 1000 , 10000]

best_r2 = 0
best_hyperparams = None

# Loop over hyperparameters and fit models
for lr in learning_rates:
    for n_iters in num_iters_list:
        # Initialize the parameters
        theta = np.zeros(X_train_scaled.shape[1])

        # Create a MyGradient instance
        my_g = MyGradient(X_train_scaled, y_train_scaled, theta)

        # Fit the model to the scaled training set
        theta, J_history = my_g.gradient_descent(lr, n_iters)

        # Make predictions on the scaled test set
        y_pred_scaled = np.dot(X_test_scaled, theta)

        # Unscale the predicted and true values
        y_pred = scaler.inverse_transform(y_pred_scaled.reshape(-1, 1)).ravel()
        y_test = scaler.inverse_transform(y_test_scaled.reshape(-1, 1)).ravel()

        # Compute the coefficient of determination (R^2)
        r2 = r2_score(y_test, y_pred)

        # Update the best hyperparameters if necessary
        if r2 > best_r2:
            best_r2 = r2
            best_hyperparams = {'learning_rate': lr, 'num_iters': n_iters, 'theta': theta}

# Fit the final model to the scaled training set using the best hyperparameters
my_g = MyGradient(X_train_scaled, y_train_scaled, best_hyperparams['theta'])
theta, J_history = my_g.gradient_descent(best_hyperparams['learning_rate'], best_hyperparams['num_iters'])

# Make predictions on the scaled test set
y_pred_scaled = np.dot(X_test_scaled, theta)

# Unscale the predicted and true values
y_pred = scaler.inverse_transform(y_pred_scaled.reshape(-1, 1)).ravel()
y_test = scaler.inverse_transform(y_test_scaled.reshape(-1, 1)).ravel()

print(f'Best hyperparameters: {best_hyperparams}','\n')
print(f'Coefficient of Determination : {best_r2*100:.3f} %')


# Display the predicted and true values for the test set with € sign 3l4an ana gamed awy
data = []
for  pred, true in zip( y_pred, y_test):
    data.append({ 'Predicted Value': round(pred), 'True Value': round(true)})
data = pd.DataFrame(data)

def convert_value(value):
    if value >= 1000000:
        return f'€{value/1000000:.2f}M'
    elif value >= 1000:
        return f'€{value/1000:.2f}K'
    else:
        return f'€{value:.0f}'

data['Predicted Value'] = data['Predicted Value'].apply(convert_value)
data['True Value'] = data['True Value'].apply(convert_value)
print("The Length of testing data : " + str(len(data)))
print(data.head(20))