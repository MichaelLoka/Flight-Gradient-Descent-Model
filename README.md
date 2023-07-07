# Flight Gradient Descent Model
### The Dataset contains 12 columns and 300152 rows.
### It describes the departure time, arrival time, source city, destination city, flight number, name of the airline, class, duration, days left, and price of each flight.

## Data Visualization
1. Horizontal Bar Chart
2. Pie Chart
3. Histograms
4. Box Plot
5. Scatter Plot

## Data Preprocessing
- Rename the unnamed column to ID
- Covert all the Arrays to Categorical Data type
- Encode Specific columns with Target Encoder
- Calculates the correlation matrix that shows the correlation coefficient between a set of variables. This shows the strength of a relationship between two variables.

## Regression Using Gradient Descent
1. Use the Price as the Target variable
2. Remove the “Price” and “ID” columns from the Data Frame and use all the Data frame to predict the price
3. Split the data into training and testing sets
4. Scale the input features and target variable using MinMaxScaler
5. Add a column for the bias term
6. Fit the final model to the scaled training set using the best hyperparameters
7. Make predictions on the scaled test set
8. Unscale the predicted and true values
9. Display the predicted and true values for the test set with the “€” sign

